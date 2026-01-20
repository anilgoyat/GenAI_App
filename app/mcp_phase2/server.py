# app/mcp_phase2/server.py

from fastapi import FastAPI, HTTPException
from .registry import list_tools
from .tools import TOOLS

app = FastAPI(title="MCP Server")

@app.get("/tools")
def get_tools():
    return list_tools()

@app.post("/tools/{tool_name}")
def execute_tool(tool_name: str, payload: dict):
    if tool_name not in TOOLS:
        raise HTTPException(status_code=404, detail="Tool not found")

    tool_func = TOOLS[tool_name]["func"]

    try:
        result = tool_func(**payload)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
