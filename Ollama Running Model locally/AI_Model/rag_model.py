import os
import warnings
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Suppress future warnings related to deprecations
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Document paths
document_paths = [
    '/home/kshitij/Downloads/Sugarlabs/Pippy-Activity/Pygame Documentation.pdf',
    '/home/kshitij/Downloads/AI-model/Python GTK+3 Documentation.pdf',
]

# Prompt template for coding assistant
PROMPT = """
You are a highly intelligent Python coding assistant. 
You are ONLY allowed to answer Python and GTK-based coding questions. If the question is not related to coding or programming, politely remind the user that you only handle coding queries.
1. Focus on coding-related problems, errors, and explanations.
2. Prioritize answers based on the provided Pygame and GTK documentation.
3. Provide step-by-step explanations wherever applicable.
4. If the documentation does not contain relevant information, use your general knowledge.
5. Always be clear, concise, and provide examples where necessary.
"""

TEMPLATE = f"""{PROMPT}
Question: {{question}}
Answer: Let's think step by step.
"""

class RAG_Agent():
    def __init__(self):
        self.model = None
        self.retriever = None
        self.prompt = ChatPromptTemplate.from_template(TEMPLATE)

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

        embeddings = HuggingFaceEmbeddings()
        vector_store = FAISS.from_documents(all_documents, embeddings)
        retriever = vector_store.as_retriever()

        return retriever

    def is_coding_query(self, question):
        """
        Check if the question is coding-related by looking for specific keywords.
        
        Args:
            question (str): The user query.
        
        Returns:
            bool: True if the query is coding-related, False otherwise.
        """
        coding_keywords = [
    'code', 'Python', 'bug', 'error', 'exception', 'syntax', 'Pygame', 'debug', 
    'program', 'programming', 'variable', 'loop', 'if', 'function', 'print', 
    'input', 'string', 'number', 'list', 'tuple', 'dictionary', 'module', 
    'import', 'turtle', 'indentation', 'syntax', 'Pygame', 'math', 'shape', 
    'for', 'while', 'repeat', 'class', 'object', 'method', 'attribute', 
    'operator', 'condition', 'true', 'false', 'boolean', 'integer', 'float', 
    'error', 'bug', 'debug', 'fix', 'type', 'index', 'range', 'len', 'append', 
    'pop', 'remove', 'sort', 'reverse', 'random', 'sleep', 'time', 'pygame', 
    'turtle', 'function', 'variable', 'list', 'loop', 'error', 'syntax', 
    'module', 'import', 'return', 'break', 'continue', 'GTK', 'logic', 'numbers'
]

        return any(keyword.lower() in question.lower() for keyword in coding_keywords)

    def get_relevant_document(self, query, retriever, threshold=0.5):
        """
        Check if the query is related to the document by using the retriever.
        
        Args:
            query (str): The user query.
            retriever: The document retriever.
            threshold (float): The confidence threshold to decide
                               if a query is related to the document.
        
        Returns:
            result (dict): Retrieved document information and similarity score.
        """
        self.retriever = self.setup_vectorstore(document_paths)
        results = self.retriever.get_relevant_documents(query)
        if len(results) > 0:
            # Check the confidence score of the first result
            top_result = results[0]
            score = top_result.metadata.get("score", 0.0)

            if score >= threshold:
                return top_result, score
        return None, 0.0

    def run(self):
        """Run the main logic of the RAG agent."""
        # Using the latest version of RetrievalQA from LangChain
        rag_chain = RetrievalQA.from_llm(
            llm=self.get_model(),
            retriever=self.retriever,
            return_source_documents=True  # Optionally return source documents
        )

        while True:
            question = input("Enter your coding question (or type 'exit' to quit): ").strip()

            if question.lower() == 'exit':
                print("Exiting the application. Goodbye!")
                break

            # Check if the query is coding-related
            if not self.is_coding_query(question):
                print("Sorry, I can only assist with coding-related questions. Please ask a programming question.")
                continue

            # Check if the query is relevant to the documents
            doc_result, relevance_score = self.get_relevant_document(question, self.retriever)

            if doc_result:
                print(f"Document is relevant (Score: {relevance_score:.2f}). Using document-specific response...")
                response = rag_chain({"query": question})
                if 'result' in response:
                    print(f"Document Response: {response['result']}")
                else:
                    print("No result found in documents, trying general knowledge...")
                    response = self.model.invoke(question)
                    print(f"Response: {response}")
            else:
                print(f"Document is not relevant (Score: {relevance_score:.2f}). Using general knowledge response...")
                response = self.model.invoke(question)
                print(f"Response: {response}")

# Optional script onle required when you need to run in terminal using command python rag_model.py
if __name__ == "__main__":
    agent = RAG_Agent()
    agent.set_model("llama3.1")  # Setting the model to llama3.1 from Ollama
    agent.retriever = agent.setup_vectorstore(document_paths)  # Initialize the retriever with documents
    agent.run()
