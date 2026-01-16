from .reranker import get_reranker

def main():
    reranker = get_reranker("groq")

    query = "What is LCEL in LangChain?"

    docs = [
        "LangChain supports vector databases for retrieval.",
        "LCEL is LangChain Expression Language used for composing chains declaratively.",
        "Python is a popular programming language.",
        "RAG systems combine retrieval and generation."
    ]

    print("\n--- Original Docs ---")
    for d in docs:
        print("-", d)

    print("\n--- Reranked Docs ---")
    ranked = reranker.rerank(query, docs)
    for d in ranked:
        print("-", d)


if __name__ == "__main__":
    main()
