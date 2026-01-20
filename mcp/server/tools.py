# mcp/server/tools.py

from .schemas import ToolSchema

def add_numbers(a: int, b: int):
    return a + b

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")


TOOLS = {
    "add_numbers": {
        "function": add_numbers,
        "schema": ToolSchema(
            name="add_numbers",
            description="Add two numbers",
            parameters={
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"}
                },
                "required": ["a", "b"]
            }
        )
    },
    "get_time": {
        "function": get_time,
        "schema": ToolSchema(
            name="get_time",
            description="Get current time",
            parameters={"type": "object", "properties": {}}
        )
    }
}
