from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from app.core.llm import get_llm


# ---- LLM ----
llm = get_llm("groq")

# ---- Memory ----
memory = MemorySaver()


# ---- State ----
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    awaiting_approval: bool


# ---- Nodes ----

def classify_node(state: ChatState):
    """Detect dangerous intent"""
    last_msg = state["messages"][-1].content.lower()

    dangerous_words = ["delete", "drop", "destroy", "remove", "wipe"]

    if any(word in last_msg for word in dangerous_words):
        return {"awaiting_approval": True}
    return {"awaiting_approval": False}


def approval_node(state: ChatState):
    """Ask user for confirmation"""
    return {
        "messages": [
            AIMessage(content="⚠ This action looks dangerous. Do you approve? (yes/no)")
        ]
    }


def decision_node(state: ChatState):
    """Check yes/no response"""
    last_msg = state["messages"][-1].content.lower()

    if last_msg.strip() in ["yes", "y"]:
        return {"approved": True}
    else:
        return {"approved": False}


def chat_node(state: ChatState):
    """Normal LLM response"""
    response = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}


def cancel_node(state: ChatState):
    return {"messages": [AIMessage(content="❌ Action cancelled.")]}


# ---- Build Graph ----

def build_hitl_graph():
    graph = StateGraph(ChatState)

    graph.add_node("classify", classify_node)
    graph.add_node("approval", approval_node)
    graph.add_node("decision", decision_node)
    graph.add_node("chat", chat_node)
    graph.add_node("cancel", cancel_node)

    graph.set_entry_point("classify")

    graph.add_conditional_edges(
        "classify",
        lambda s: "approval" if s["awaiting_approval"] else "chat",
        {
            "approval": "approval",
            "chat": "chat"
        }
    )

    graph.add_edge("approval", "decision")

    graph.add_conditional_edges(
        "decision",
        lambda s: "chat" if s.get("approved") else "cancel",
        {
            "chat": "chat",
            "cancel": "cancel"
        }
    )

    graph.add_edge("chat", END)
    graph.add_edge("cancel", END)

    return graph.compile(checkpointer=memory)


# ---- CLI Demo ----

def main():
    app = build_hitl_graph()
    thread_id = "user-1"

    while True:
        user = input("User: ")
        if user == "exit":
            break

        result = app.invoke(
            {"messages": [HumanMessage(content=user)]},
            config={"configurable": {"thread_id": thread_id}}
        )

        print("Assistant:", result["messages"][-1].content)


if __name__ == "__main__":
    main()
