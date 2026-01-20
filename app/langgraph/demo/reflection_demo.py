from app.langgraph.reflection.reflection_graph import build_reflection_graph

def main():
    app = build_reflection_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})

        print("\n--- Draft ---")
        print(result["draft"])

        print("\n--- Critique ---")
        print(result["critique"])

        print("\n--- Final Answer ---")
        print(result["final"])


if __name__ == "__main__":
    main()
