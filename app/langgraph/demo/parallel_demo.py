from app.langgraph.graphs.parallel_graph import build_parallel_graph

def main():
    app = build_parallel_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})
        print("\nAssistant:\n", result["final"])

if __name__ == "__main__":
    main()
