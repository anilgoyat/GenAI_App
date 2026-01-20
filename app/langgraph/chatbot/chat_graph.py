from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from .memory_store import memory
from ...core.llm import get_llm
from ..state import ChatState, GraphState

llm = get_llm("groq")

def chat_node(state: GraphState):
    messages = state["messages"]

    response = llm.invoke(messages)

    messages.append(AIMessage(content=response.content))

    return {"messages": messages}

def build_chat_graph():
    graph = StateGraph(GraphState)

    graph.add_node("chat", chat_node)

    graph.set_entry_point("chat")
    graph.add_edge("chat", END)

    return graph

def build_persistent_chat_graph():
    graph = StateGraph(ChatState)

    graph.add_node("chat", chat_node)
    graph.set_entry_point("chat")
    graph.add_edge("chat", END)

    return graph.compile(checkpointer=memory)
