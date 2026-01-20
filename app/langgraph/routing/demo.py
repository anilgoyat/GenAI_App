from .conditional_graph import build_conditional_graph

def main():
    graph = build_conditional_graph()

    while True:
        user = input("\nUser: ")
        if user == "exit":
            break

        result = graph.invoke({"input": user})
        print("Assistant:", result["output"])


if __name__ == "__main__":
    main()
