from .graph import build_agent_os

def main():
    app = build_agent_os()

    while True:
        user = input("\nUser: ")
        if user == "exit":
            break

        result = app.invoke({"input": user})

        print("\nPlan:\n", result["plan"])
        print("\nRoute:\n", result["route"])
        print("\nFinal Output:\n", result["output"])

if __name__ == "__main__":
    main()
