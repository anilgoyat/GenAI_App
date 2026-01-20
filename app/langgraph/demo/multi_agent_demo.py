from app.langgraph.graphs.multi_agent_graph import build_multi_agent_graph

def main():
    app = build_multi_agent_graph()

    while True:
        query = input("\nUser: ")
        if query == "exit":
            break

        result = app.invoke({"query": query})
        print("Assistant:", result["response"])

if __name__ == "__main__":
    main()
