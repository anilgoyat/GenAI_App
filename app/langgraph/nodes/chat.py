from langchain_core.messages import AIMessage
from app.core.llm import get_llm

llm = get_llm("groq")

def chat_node(state):
    response = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}
