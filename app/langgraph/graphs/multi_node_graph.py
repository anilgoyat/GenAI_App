from langgraph.graph import StateGraph, END
from app.langgraph.state import ChatState
from app.langgraph.nodes.router import router_node
from app.langgraph.nodes.chat import chat_node
from app.langgraph.nodes.tools import tool_node
# from app.langgraph.memory.memory_store import memory
from app.langgraph.chatbot.memory_store import memory

def build_multi_graph():
    graph = StateGraph(ChatState)

    graph.add_node("chat", chat_node)
    graph.add_node("tool", tool_node)

    graph.set_conditional_entry_point(
        router_node,
        {
            "chat": "chat",
            "tool": "tool",
        }
    )

    graph.add_edge("chat", END)
    graph.add_edge("tool", END)

    return graph.compile(checkpointer=memory)
