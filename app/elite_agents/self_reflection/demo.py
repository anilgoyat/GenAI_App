from .reflection_graph import build_reflection_graph

def main():
    app = build_reflection_graph()

    question = "Explain RAG in simple terms."

    result = app.invoke({
        "question": question
    })

    print("\n--- Draft ---\n")
    print(result["draft"])

    print("\n--- Critique ---\n")
    print(result["critique"])

    print("\n--- Final Improved Answer ---\n")
    print(result["final"])

if __name__ == "__main__":
    main()
