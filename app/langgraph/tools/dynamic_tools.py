def create_tool_from_description(desc: str):
    # simplified mock tool creation
    def tool(input: str):
        return f"Tool created for: {desc}\nInput: {input}"

    return tool
