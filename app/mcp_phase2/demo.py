# app/mcp_phase2/demo.py

from .client import MCPClient

def main():
    client = MCPClient()

    print("\n🔍 Discovering tools...")
    tools = client.discover_tools()
    print(tools)

    print("\n⚡ Calling add_numbers...")
    result = client.call_tool("add_numbers", {"a": 10, "b": 20})
    print("Result:", result)

    print("\n⏰ Calling get_time...")
    result = client.call_tool("get_time", {})
    print("Result:", result)

if __name__ == "__main__":
    main()
