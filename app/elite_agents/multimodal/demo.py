from .vision_graph import build_vision_graph

def main():
    app = build_vision_graph()

    image_desc = "A photo of a laptop with VS Code open and Python code on screen."
    question = "What is the person likely working on?"

    result = app.invoke({
        "image": image_desc,
        "question": question
    })

    print("\n🧠 Vision Agent Output:\n")
    print(result["answer"])

if __name__ == "__main__":
    main()
