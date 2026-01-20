from mcp.client.main import call_tool

def main():
    print("Calling MCP Tool: add_numbers(10, 20)")
    result = call_tool("add_numbers", {"a": 10, "b": 20})
    print("Result:", result)

if __name__ == "__main__":
    main()
