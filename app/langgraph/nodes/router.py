def router_node(state):
    last_message = state["messages"][-1].content.lower()

    if "add" in last_message or "+" in last_message:
        return "tool"
    else:
        return "chat"
