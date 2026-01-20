from app.langgraph.graphs.supervisor_graph import build_supervisor_graph

def main():
    app = build_supervisor_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})
        print("\nAssistant:\n", result["final"])

if __name__ == "__main__":
    main()
