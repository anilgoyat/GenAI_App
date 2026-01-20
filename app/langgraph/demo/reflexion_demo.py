from app.langgraph.reflexion.reflexion_graph import build_reflexion_graph

def main():
    app = build_reflexion_graph()

    while True:
        q = input("Question: ")
        if q == "exit":
            break

        result = app.invoke({"question": q})

        print("\n--- First Answer ---")
        print(result["answer"])

        print("\n--- Critique ---")
        print(result["critique"])

        print("\n--- Improved Answer ---")
        print(result["improved_answer"])


if __name__ == "__main__":
    main()
