from langchain_core.messages import AIMessage

def tool_node(state):
    text = state["messages"][-1].content

    # Simple extraction
    numbers = [int(s) for s in text.split() if s.isdigit()]

    if len(numbers) == 2:
        result = sum(numbers)
        return {"messages": [AIMessage(content=f"The result is {result}")]}
    
    return {"messages": [AIMessage(content="Couldn't parse numbers")]}
