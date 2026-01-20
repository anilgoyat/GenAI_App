from .long_term_store import memory_store

def retrieve_memories(query: str):
    return memory_store.search(query)
