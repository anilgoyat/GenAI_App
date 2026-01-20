from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
import pickle

class LongTermMemoryStore:
    def __init__(self, path="memory_db"):
        self.path = path

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Load existing DB if exists
        if os.path.exists(f"{path}.pkl"):
            with open(f"{path}.pkl", "rb") as f:
                self.db = pickle.load(f)
        else:
            self.db = None

    def add_memory(self, text: str):
        if self.db is None:
            self.db = FAISS.from_texts([text], self.embeddings)
        else:
            self.db.add_texts([text])

        # Persist to disk
        with open(f"{self.path}.pkl", "wb") as f:
            pickle.dump(self.db, f)

    def search(self, query: str, k: int = 3):
        if self.db is None:
            return []
        results = self.db.similarity_search(query, k=k)
        return [r.page_content for r in results]


memory_store = LongTermMemoryStore()
