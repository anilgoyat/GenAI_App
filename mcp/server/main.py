from fastapi import FastAPI
from pydantic import BaseModel
from mcp.tools.math_tools import add_numbers
from .tools import TOOLS
app = FastAPI()

class ToolRequest(BaseModel):
    tool: str
    args: dict

@app.post("/invoke")
def invoke_tool(req: ToolRequest):
    if req.tool == "add_numbers":
        return {"result": add_numbers(**req.args)}

    return {"error": f"Unknown tool: {req.tool}"}

@app.get("/tools")
def list_tools():
    return [tool["schema"].dict() for tool in TOOLS.values()]

@app.post("/tools/{tool_name}")
def run_tool(tool_name: str, payload: dict):
    if tool_name not in TOOLS:
        return {"error": "Tool not found"}

    func = TOOLS[tool_name]["function"]
    result = func(**payload)
    return {"result": result}
