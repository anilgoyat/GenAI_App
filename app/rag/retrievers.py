from langchain_core.documents import Document

def get_multi_query_retriever(retriever, llm):
    """
    Lightweight MultiQueryRetriever (production-style).
    Generates multiple query variants using LLM and retrieves docs.
    """

    def multi_query_search(query: str):
        # Step 1: Generate variations
        prompt = f"""
        Generate 3 different search queries for the following question:
        Question: {query}

        Return each query on a new line.
        """

        variations = llm.invoke(prompt).content.split("\n")
        variations = [v.strip("- ").strip() for v in variations if v.strip()]

        # Step 2: Collect docs
        all_docs = []
        for q in variations:
            all_docs.extend(retriever.invoke(q))

        # Step 3: Remove duplicates
        unique_docs = {doc.page_content: doc for doc in all_docs}
        return list(unique_docs.values())

    return multi_query_search

def get_filtered_retriever(vectorstore, category: str):
    return vectorstore.as_retriever(
        search_kwargs={
            "k": 4,
            "filter": {"category": category}
        }
    )

# Optional: Parent-Child retriever example
def retrieve_with_parent(query, vectorstore, parent_lookup, k=4):
    results = vectorstore.similarity_search(query, k=k)

    parent_ids = set(doc.metadata["parent_id"] for doc in results)
    return [parent_lookup[i] for i in parent_ids]
