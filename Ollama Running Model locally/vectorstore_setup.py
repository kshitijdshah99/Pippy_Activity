# vectorstore_setup.py

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader

def setup_vectorstore():
    try:
        # Load your documents
        file_path = 'C:/Users\Admin\Downloads\LLAMA_3.1\Microsoft.pdf'  # Replace with your document path
        print(f"Loading document from: {file_path}")
        loader = TextLoader(file_path)
        documents = loader.load()

        # Create embeddings
        embeddings = OpenAIEmbeddings()

        # Create a vector store
        vector_store = FAISS.from_documents(documents, embeddings)
        
        # Create a retriever
        retriever = vector_store.as_retriever()

        return retriever
    
    except Exception as e:
        print(f"Failed to setup vector store: {e}")
        return None
