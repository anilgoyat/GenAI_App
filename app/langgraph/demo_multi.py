from langchain_core.messages import HumanMessage
from app.langgraph.graphs.multi_node_graph import build_multi_graph

def main():
    app = build_multi_graph()
    thread_id = "user-1"

    while True:
        user = input("User: ")

        result = app.invoke(
            {"messages": [HumanMessage(content=user)]},
            config={"configurable": {"thread_id": thread_id}}
        )

        print("Assistant:", result["messages"][-1].content)

if __name__ == "__main__":
    main()
