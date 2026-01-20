from app.core.llm import get_llm
from .long_term_store import memory_store

llm = get_llm("groq")

def extract_and_store_memory(user_input: str):
    prompt = f"""
Extract important personal information about the user.
Only extract facts worth remembering long-term.

Text:
{user_input}

Return single sentence or say 'NONE'.
"""

    response = llm.invoke(prompt)

    text = response.content.strip()

    if text.upper() != "NONE":
        memory_store.add_memory(text)
        return text

    return None
