# Pippy's AI-Coding Assistant
# Uses Llama3.1 model from Ollama

import os
import warnings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Suppress future warnings related to deprecations
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Document paths
document_paths = [
    '/home/kshitij/Downloads/Sugarlabs/Pippy-Activity/1706.03762v7.pdf'
]

# Revised Prompt Template to avoid mentioning the source
PROMPT_TEMPLATE = """
You are a highly intelligent Python coding assistant built for kids. 
You are ONLY allowed to answer Python and GTK-based coding questions. 
1. Focus on coding-related problems, errors, and explanations.
2. Use the knowledge from the provided Pygame and GTK documentation without explicitly mentioning the documents as the source.
3. Provide step-by-step explanations wherever applicable.
4. If the documentation does not contain relevant information, use your general knowledge.
5. Always be clear, concise, and provide examples where necessary.
6. Your answer must be easy to understand for the kids.

Question: {question}
Answer: Let's think step by step.
"""

class RAG_Agent:
    def __init__(self, model="llama3.1"):
        """
        Initialize the RAG agent with a default model like Llama3.1.
        """
        self.model = OllamaLLM(model=model)
        self.retriever = None
        self.prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    def set_model(self, model="llama3.1"):
        """Set the Llama 3.1 model from Ollama."""
        self.model = OllamaLLM(model=model)

    def get_model(self):
        """Return the LLM model."""
        return self.model

    def setup_vectorstore(self, file_paths):
        """
        Set up a vector store from the provided document files.
        
        Args:
            file_paths (list): List of paths to document files.
        
        Returns:
            retriever: A retriever object for document retrieval.
        """
        all_documents = []
        for file_path in file_paths:
            if os.path.exists(file_path):
                if file_path.endswith(".pdf"):
                    loader = PyMuPDFLoader(file_path)
                else:
                    loader = TextLoader(file_path)

                documents = loader.load()
                all_documents.extend(documents)

        # Using HuggingFace embeddings
        embeddings = HuggingFaceEmbeddings()
        vector_store = FAISS.from_documents(all_documents, embeddings)
        retriever = vector_store.as_retriever()
        return retriever


    def get_relevant_document(self, query, threshold=0.5):
        """
        Check if the query is related to a document by using the retriever.
        
        Args:
            query (str): The user query.
            threshold (float): The confidence threshold to decide
                               if a query is related to the document.
        
        Returns:
            tuple: (top_result, score) if relevant document found, otherwise (None, 0.0)
        """
        results = self.retriever.invoke(query)

        if results:
            # Check the confidence score of the top result
            top_result = results[0]
            score = top_result.metadata.get("score", 0.0)

            if score >= threshold:
                return top_result, score
        return None, 0.0



    def run(self):
        """Run the main logic of the RAG agent."""
        
        # Format documents for context
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Create the LCEL chain
        qa_chain = (
            {
                "context": self.retriever | format_docs, 
                "question": RunnablePassthrough()  
            }
            | self.prompt  
            | self.model   
            | StrOutputParser()  
        )

        while True:
            question = input("Hey there, let me know your coding doubt").strip()

            # if not self.is_coding_query(question):
            #     response = "Sorry, I can only assist with coding-related questions. Please ask a programming question."
            #     return response

            # Check if the query is relevant to the document
            doc_result, relevance_score = self.get_relevant_document(question)

            if doc_result:
                print(f"Relevant document found with a score of {relevance_score:.2f}")
                response = qa_chain.invoke({"query": question, "context": doc_result.page_content})
            else:
                print(f"No relevant document found, using general knowledge.")
                response = qa_chain.invoke(question)
            
            print(response)

if __name__ == "__main__":
    agent = RAG_Agent()
    agent.retriever = agent.setup_vectorstore(document_paths)  
    agent.run()

