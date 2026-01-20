from app.langgraph.graphs.router_graph import build_router_graph

def main():
    app = build_router_graph()

    while True:
        q = input("User: ")
        if q == "exit":
            break

        result = app.invoke({"input": q})
        print("Assistant:", result["output"])

if __name__ == "__main__":
    main()
