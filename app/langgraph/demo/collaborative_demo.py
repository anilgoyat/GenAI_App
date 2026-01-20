from langchain_core.messages import HumanMessage
from app.langgraph.graphs.collaborative_graph import build_collaborative_graph

def main():
    app = build_collaborative_graph()

    thread_id = "collab-user"

    while True:
        user = input("User: ")
        if user == "exit":
            break

        result = app.invoke(
            {"messages": [HumanMessage(content=user)]},
            config={"configurable": {"thread_id": thread_id}}
        )

        print("\n--- Research ---")
        print(result.get("research"))

        print("\n--- Critique ---")
        print(result.get("critique"))

        print("\n--- Final Answer ---")
        print(result.get("final"))
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()
