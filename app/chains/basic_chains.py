from app.prompts.prompt_factory import get_prompt
from app.core.llm import get_llm


def get_basic_chain(provider: "groq"):
    llm = get_llm(provider)
    prompt = get_prompt("text_basic")
    chain = prompt | llm
    return chain

def batch_chain(provider: "groq"):
    llm = get_llm(provider)
    prompt = get_prompt("text_basic")
    chain = prompt | llm
    return chain

def streaming_chain(provider: "groq"):
    llm = get_llm(provider, streaming=True)
    prompt = get_prompt("chat_basic")
    chain = prompt | llm
    return chain