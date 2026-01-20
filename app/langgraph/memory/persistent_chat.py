from typing import TypedDict, List
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, AIMessage
from app.core.llm import get_llm


# ---------------------------
# State schema
# ---------------------------
class ChatState(TypedDict):
    messages: List


# ---------------------------
# Chat node
# ---------------------------
def chat_node(state: ChatState):
    llm = get_llm("groq")
    messages = [
        {"role": "system", "content": "You are a helpful assistant with memory. Use previous conversation when answering."}
    ] + state["messages"]
    response = llm.invoke(messages)

    return {
        "messages": state["messages"] + [response]
    }


# ---------------------------
# Build graph with memory
# ---------------------------
def build_persistent_chat_graph():
    builder = StateGraph(ChatState)

    builder.add_node("chat", chat_node)
    builder.set_entry_point("chat")
    builder.set_finish_point("chat")

    # This is real memory
    memory = MemorySaver()

    return builder.compile(checkpointer=memory)
