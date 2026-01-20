# mcp/client/invoke.py

import requests

def call_tool(name, payload):
    url = f"http://localhost:8000/tools/{name}"
    return requests.post(url, json=payload).json()

if __name__ == "__main__":
    print(call_tool("add_numbers", {"a": 10, "b": 20}))
    print(call_tool("get_time", {}))
