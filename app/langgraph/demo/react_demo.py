from langchain_core.messages import HumanMessage
from app.langgraph.graphs.react_graph import build_react_graph

def main():
    app = build_react_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({
            "messages": [HumanMessage(content=q)]
        })

        print("Assistant:", result["messages"][-1].content)

if __name__ == "__main__":
    main()
