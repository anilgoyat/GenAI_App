from langchain.retrievers import EnsembleRetriever

def build_hybrid_retriever(vector_retriever, keyword_retriever):
    return EnsembleRetriever(
        retrievers=[vector_retriever, keyword_retriever],
        weights=[0.7, 0.3]
    )
