from app.langgraph.planner.advance_planner_graph import build_planner_graph

def main():
    app = build_planner_graph()

    while True:
        goal = input("Goal: ")
        if goal == "exit":
            break

        result = app.invoke({"goal": goal})

        print("\n--- Final Output ---")
        print(result["final"])


if __name__ == "__main__":
    main()
