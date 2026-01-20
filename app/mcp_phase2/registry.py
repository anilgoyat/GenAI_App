# app/mcp_phase2/registry.py

from .tools import TOOLS

def list_tools():
    tool_list = []
    for name, data in TOOLS.items():
        tool_list.append({
            "name": name,
            "description": data["description"],
            "schema": data["schema"]
        })
    return tool_list
