from app.langgraph.tools.dynamic_tools import create_tool_from_description

tool = create_tool_from_description("Analyze text sentiment")
print(tool("This product is amazing"))
