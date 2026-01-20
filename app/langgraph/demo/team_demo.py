from app.langgraph.collaboration.team_graph import build_team_graph

def main():
    app = build_team_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})

        print("\n--- Research ---")
        print(result["research"])

        print("\n--- Draft ---")
        print(result["draft"])

        print("\n--- Reviewed ---")
        print(result["review"])

        print("\n--- Final ---")
        print(result["final"])


if __name__ == "__main__":
    main()
