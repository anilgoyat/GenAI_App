from langchain_community.document_loaders import TextLoader

def load_documents(path: str):
    loader = TextLoader(path, encoding="utf-8")
    documents = loader.load()

     # Add metadata manually (like production systems do)
    for doc in documents:
        doc.metadata["source"] = path
        doc.metadata["category"] = "langchain"

    return documents