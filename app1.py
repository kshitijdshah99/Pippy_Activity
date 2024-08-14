import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyMuPDFLoader
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Set up Streamlit app
st.title("LangChain-RAG App")

# Path to your PDF document
file_path = 'C:/Users/Admin/Downloads/LLAMA_3.1/Microsoft.pdf'  # Replace with the correct path

def setup_vectorstore():
    try:
        # Load your PDF document
        loader = PyMuPDFLoader(file_path)
        documents = loader.load()
        st.write(f"Loaded {len(documents)} documents from the PDF.")

        # Create embeddings using HuggingFace
        embeddings = HuggingFaceEmbeddings()

        # Create a vector store
        vector_store = FAISS.from_documents(documents, embeddings)

        # Create a retriever
        retriever = vector_store.as_retriever()

        return retriever
    
    except Exception as e:
        st.error(f"Failed to set up the retriever: {e}")
        return None

# Set up the RAG model
template = """Question: {question}
Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")

# Initialize retriever
retriever = setup_vectorstore()

if retriever:
    # Combine the retriever and model into a Retrieval-Augmented Generation (RAG) chain
    rag_chain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=retriever)

    # Capture user input and display the response
    question = st.chat_input("Enter your question here")
    if question:
        # Determine if the question is general knowledge or specific to documents
        if any(keyword in question.lower() for keyword in ["python", "programming", "syntax", "code", "loop"]):
            # General programming or knowledge query, use the model directly
            response = model(question)
            st.write(response)
        else:
            # Document-specific query, use RAG approach
            response = rag_chain({"query": question})
            if 'result' in response:
                st.write(response['result'])
            else:
                st.write("No result found in documents, trying general knowledge...")
                response = model(question)
                st.write(response)
else:
    st.error("Unable to set up the retriever. Please check the document and try again.")
