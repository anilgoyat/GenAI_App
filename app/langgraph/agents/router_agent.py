from app.core.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

llm = get_llm("groq")

def route_query(query: str) -> str:
    messages = [
        SystemMessage(content="Classify query as math, research, or chat."),
        HumanMessage(content=query)
    ]
    return llm.invoke(messages).content.lower()
