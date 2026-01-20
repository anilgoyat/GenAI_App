from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph.message import add_messages
from app.core.llm import get_llm

llm = get_llm("groq")
memory = MemorySaver()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}

def main():
    graph = StateGraph(ChatState)
    graph.add_node("chat", chat_node)
    graph.set_entry_point("chat")
    graph.add_edge("chat", END)

    app = graph.compile(checkpointer=memory)

    thread_id = "test-user"

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
