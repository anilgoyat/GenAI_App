# app/mcp_phase2/tools.py

def add_numbers(a: int, b: int) -> int:
    return a + b

def get_time() -> str:
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TOOLS = {
    "add_numbers": {
        "func": add_numbers,
        "description": "Add two numbers",
        "schema": {"a": "int", "b": "int"}
    },
    "get_time": {
        "func": get_time,
        "description": "Get current system time",
        "schema": {}
    }
}
