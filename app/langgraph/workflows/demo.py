from .multi_node_graph import build_multi_node_graph

def main():
    graph = build_multi_node_graph()

    while True:
        user = input("\nUser: ")
        if user == "exit":
            break

        result = graph.invoke({"input": user})

        print("\n--- PLAN ---")
        print(result["plan"])

        print("\n--- RESULT ---")
        print(result["result"])

        print("\n--- FINAL ---")
        print(result["final"])


if __name__ == "__main__":
    main()
