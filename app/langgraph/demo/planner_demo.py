from app.langgraph.planner.planner_graph import build_planner_graph

def main():
    app = build_planner_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})

        print("\n--- PLAN ---")
        for step in result["plan"]:
            print("-", step)

        print("\n--- EXECUTION ---")
        print(result["result"])


if __name__ == "__main__":
    main()
