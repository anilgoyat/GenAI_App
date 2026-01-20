from langchain_core.messages import HumanMessage
from ..advance_memory.memory_graph import build_memory_graph
from dotenv import load_dotenv
import os
load_dotenv()
def main():
    app = build_memory_graph()

    print("🧠 Memory-enabled assistant started (type 'exit' to quit)\n")

    while True:
        user = input("User: ")

        if user.lower() == "exit":
            break
        thread_id = "user-1"
        result = app.invoke({
            "messages": [HumanMessage(content=user)]
        }, config={"configurable": {"thread_id": thread_id}})

        print("Assistant:", result["messages"][-1].content)


if __name__ == "__main__":
    main()
