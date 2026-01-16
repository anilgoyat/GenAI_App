from langchain_core.documents import Document

def add_metadata(docs):
    enriched_docs = []

    for doc in docs:
        enriched_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={
                    "source": "internal_docs",
                    "topic": "langchain",
                    "level": "beginner"
                }
            )
        )

    return enriched_docs
