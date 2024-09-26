# app.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.document_loaders import PyMuPDFLoader, TextLoader
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Path to your PDF document
file_path = '/home/kshitij/Downloads/AI-model/Pygame Documentation.pdf'  # Replace with the correct path

def setup_vectorstore(file_path):
    """
    Set up a vector store from the provided document file.
    
    Args:
        file_path (str): Path to the document file.
    
    Returns:
        retriever: A retriever object for document retrieval.
    """
    try:
        print(f"Loading document from: {file_path}")
        if file_path.endswith(".pdf"):
            # Load PDF document using PyMuPDFLoader
            loader = PyMuPDFLoader(file_path)
        else:
            # Load text document using TextLoader
            loader = TextLoader(file_path)

        documents = loader.load()
        print(f"Loaded {len(documents)} documents from the file.")

        # Create embeddings using HuggingFace or OpenAI embeddings
        embeddings = HuggingFaceEmbeddings()  # You can switch to OpenAIEmbeddings if needed

        # Create a vector store
        vector_store = FAISS.from_documents(documents, embeddings)

        # Create a retriever
        retriever = vector_store.as_retriever()
        return retriever

    except Exception as e:
        print(f"Failed to set up the retriever: {e}")
        return None

# Set up the RAG model
template = """Question: {question}
Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")

# Initialize the vector store retriever
retriever = setup_vectorstore(file_path)

if retriever:
    # Combine the retriever and model into a Retrieval-Augmented Generation (RAG) chain
    rag_chain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=retriever)

    print("RAG model setup completed successfully!")

    while True:
        # Capture user input from the terminal
        question = input("Enter your question (or type 'exit' to quit): ").strip()
        
        if question.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break

        # Determine if the question is general knowledge or specific to documents
        if any(keyword in question.lower() for keyword in ["python", "programming", "syntax", "code", "loop"]):
            # General programming or knowledge query, use the model directly
            print("Processing as a general knowledge question...")
            response = model(question)
            print(f"Response: {response}")
        else:
            # Document-specific query, use RAG approach
            print("Processing as a document-specific query...")
            response = rag_chain({"query": question})
            if 'result' in response:
                print(f"Document Response: {response['result']}")
            else:
                print("No result found in documents, trying general knowledge...")
                response = model(question)
                print(f"Response: {response}")

else:
    print("Unable to set up the retriever. Please check the document and try again.")
