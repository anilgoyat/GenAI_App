from langchain_core.messages import HumanMessage
from .chatbot.chat_graph import build_persistent_chat_graph

def main():
    graph = build_persistent_chat_graph()
    thread_id = "user-1"

    while True:
        user = input("User: ")
        if user == "exit":
            break

        result = graph.invoke(
            {"messages": [HumanMessage(content=user)]},
            config={"configurable": {"thread_id": thread_id}}
        )

        print("Assistant:", result["messages"][-1].content)

if __name__ == "__main__":
    main()
