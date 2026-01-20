from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")

def coding_agent(query: str):
    messages = [
        HumanMessage(content=f"You are a senior software engineer. Provide code and explanation:\n{query}")
    ]
    return llm.invoke(messages).content
