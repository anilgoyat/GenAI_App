# app/mcp_phase2/client.py

import requests

class MCPClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def discover_tools(self):
        res = requests.get(f"{self.base_url}/tools")
        return res.json()

    def call_tool(self, tool_name: str, args: dict):
        res = requests.post(f"{self.base_url}/tools/{tool_name}", json=args)
        return res.json()
