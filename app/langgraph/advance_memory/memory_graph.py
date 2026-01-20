from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver

from app.core.llm import get_llm
from .memory_node import memory_node

llm = get_llm("groq")
memory = MemorySaver()

# -----------------------------
# State
# -----------------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# -----------------------------
# Chat Node
# -----------------------------
def chat_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}


# -----------------------------
# Build Memory Test Graph
# -----------------------------
def build_memory_graph():
    graph = StateGraph(ChatState)

    graph.add_node("memory", memory_node)
    graph.add_node("chat", chat_node)

    graph.set_entry_point("memory")

    graph.add_edge("memory", "chat")
    graph.add_edge("chat", END)

    return graph.compile(checkpointer=memory)
