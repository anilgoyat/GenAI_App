from langchain_community.vectorstores import FAISS
from .embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)
