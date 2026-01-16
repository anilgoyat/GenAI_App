# app/rag/router_demo.py

from ..core.llm import get_llm

from .loaders import load_documents
from .splitters import split_documents
from .vectorstore import create_vectorstore
from .rag_chain import build_rag_chain

from app.rag.router import build_router_chain


def main():
    # Step 1: Setup LLM
    llm = get_llm(provider="groq")

    # Step 2: Prepare RAG pipeline
    docs = load_documents("data/sample.txt")
    chunks = split_documents(docs)
    vectorstore = create_vectorstore(chunks)
    retriever = vectorstore.as_retriever()

    rag_chain = build_rag_chain(retriever, llm)

    # Step 3: Build router
    router_chain = build_router_chain(llm)

    # ---------------------------
    # Test queries
    # ---------------------------
    queries = [
        "What is LCEL in LangChain?",
        "Explain retrievers in LangChain",
        "Tell me a joke",
        "Who is Elon Musk?"
    ]

    for query in queries:
        print("\n" + "=" * 60)
        print(f"User: {query}")

        # Router decision
        route = router_chain.invoke({"input": query}).strip().upper()
        print(f"[Router decision] → {route}")

        if route == "RAG":
            result = rag_chain.invoke(query)
        else:
            result = llm.invoke(query)

        print(f"Assistant: {result.content}")


if __name__ == "__main__":
    main()
