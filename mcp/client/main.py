import requests

SERVER_URL = "http://localhost:8000/invoke"

def call_tool(tool_name: str, args: dict):
    payload = {
        "tool": tool_name,
        "args": args
    }

    response = requests.post(SERVER_URL, json=payload)
    return response.json()
