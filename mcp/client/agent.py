# mcp/client/agent.py

import requests
import json
from app.core.llm import get_llm

MCP_BASE = "http://localhost:8000"

llm = get_llm("groq")


def fetch_tools():
    res = requests.get(f"{MCP_BASE}/tools")
    return res.json()


def call_tool(tool_name, args):
    res = requests.post(f"{MCP_BASE}/tools/{tool_name}", json=args)
    return res.json()


def agent_respond(user_input: str):
    tools = fetch_tools()

    system_prompt = f"""
You are an AI agent with access to external tools.

Tools available:
{json.dumps(tools, indent=2)}

If a tool is useful, respond ONLY in JSON like:
{{"tool": "tool_name", "arguments": {{...}}}}

If no tool needed, respond normally.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    response = llm.invoke(messages)

    text = response.content.strip()

    # Try parse JSON tool call
    try:
        tool_call = json.loads(text)
        tool = tool_call["tool"]
        args = tool_call["arguments"]

        tool_result = call_tool(tool, args)

        return f"Tool `{tool}` result: {tool_result}"

    except Exception:
        return text


if __name__ == "__main__":
    while True:
        q = input("\nUser: ")
        print("Agent:", agent_respond(q))
