from app.langgraph.graphs.planner_executor_graph import build_agent_graph

def main():
    app = build_agent_graph()

    while True:
        goal = input("\nUser Goal: ")
        if goal.lower() == "exit":
            break

        app.invoke({"goal": goal})


if __name__ == "__main__":
    main()
