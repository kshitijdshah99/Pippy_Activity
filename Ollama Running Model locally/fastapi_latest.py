from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os

# Initialize FastAPI
app = FastAPI()

# Define the RAG Agent class
class RAG_Agent:
    def __init__(self, model="llama3.1"):
        self.model = OllamaLLM(model=model)
        self.retriever = None
        self.prompt = ChatPromptTemplate.from_template("""
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
        """)

    def setup_vectorstore(self, file_paths):
        """
        Set up a vector store using the provided document paths.
        """
        all_documents = []
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

        for file_path in file_paths:
            if os.path.exists(file_path):
                if file_path.endswith(".pdf"):
                    loader = PyMuPDFLoader(file_path)
                else:
                    loader = TextLoader(file_path)

                documents = loader.load()
                for doc in documents:
                    chunks = text_splitter.split_text(doc.page_content)
                    for chunk in chunks:
                        all_documents.append(Document(page_content=chunk, metadata=doc.metadata))

        embeddings = HuggingFaceEmbeddings()
        vector_store = FAISS.from_documents(all_documents, embeddings)
        return vector_store.as_retriever()

    def run(self, question):
        """
        Process a question and return a response using the loaded retriever and model.
        """
        if not self.retriever:
            raise ValueError("Retriever is not set up.")

        docs = self.retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        if context:
            response = self.model.invoke(self.prompt.format(context=context, question=question))
        else:
            response = self.model.invoke(self.prompt.format(context="", question=question))

        return response

# Define a query model for incoming POST requests
class QueryModel(BaseModel):
    question: str

# Load document paths
document_paths = [
    '/home/kshitij/Downloads/Sugarlabs/Pippy-Activity/Pygame Documentation.pdf',
    '/home/kshitij/Downloads/Sugarlabs/Pippy-Activity/1706.03762v7.pdf'
]

# Initialize the RAG Agent and set up the retriever
agent = RAG_Agent()
agent.retriever = agent.setup_vectorstore(document_paths)

# Define API routes
@app.get("/")
async def root():
    return {"message": "Welcome to the AI Coding Assistant!"}

@app.post("/query/")
async def handle_query(query: QueryModel):
    try:
        response = agent.run(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
