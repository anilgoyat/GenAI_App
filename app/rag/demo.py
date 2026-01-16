from .loaders import load_documents
from .splitters import split_documents
from .vectorstore import create_vectorstore
from .retrievers import get_multi_query_retriever, get_filtered_retriever
from .rag_chain import build_rag_chain
from .parent_child_splitter import create_parent_child_chunks
from ..core.llm import get_llm
from .metadata_retriver import add_metadata
# from langchain_community.retrievers import BM25Retriever
# from .hybrid_retriever import build_hybrid_retriever
def test_rag():
    # 1. Load document
    docs = load_documents("data/sample.txt")
    docs = add_metadata(docs)
    # 2. Split into chunks
    chunks = split_documents(docs)
    #Parent child chunking example
    # children, parent_lookup = create_parent_child_chunks(docs)

    # 3. Create vectorstore
    #parent_child_chunking
    # vectorstore = create_vectorstore(children)
    vectorstore = create_vectorstore(chunks)

    # 4. Base retriever
    base_retriever = vectorstore.as_retriever()

    #for hybrid retriever example using BM25 + VectorStore
    # keyword_retriever = BM25Retriever.from_documents(chunks)
    # retriever = build_hybrid_retriever(
    # vector_retriever=vector_retriever,
    # keyword_retriever=keyword_retriever
    # )
    # 5. LLM (Groq)
    llm = get_llm("groq")

    # 6. Multi-query retriever (our custom implementation)
    retriever = get_multi_query_retriever(base_retriever, llm)

    # Alternatively, filtered retriever example using metadata
    # retriever = get_filtered_retriever(vectorstore, category="langchain")


    # 7. Build RAG chain
    rag_chain = build_rag_chain(retriever, llm)

    # 
    # results = retrieve_with_parent(
    # "What is LCEL in LangChain?",
    # vectorstore,
    # parent_lookup
    # )

    # for doc in results:
    #     print(doc.page_content)
    # 8. Ask question
    response = rag_chain.invoke("What is LCEL in LangChain?")
    print("\n--- RAG Answer ---")
    print(response)


if __name__ == "__main__":
    test_rag()
