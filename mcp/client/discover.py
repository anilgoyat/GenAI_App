# mcp/client/discover.py

import requests

def discover_tools():
    response = requests.get("http://localhost:8000/tools")
    return response.json()

if __name__ == "__main__":
    tools = discover_tools()
    print("\nDiscovered Tools:\n")
    for t in tools:
        print(t)
