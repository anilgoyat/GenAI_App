import json
import requests
from app.core.llm import get_llm
from .registry import get_all_tools

llm = get_llm("groq")


def call_tool(server, tool, args):
    res = requests.post(f"{server}/tools/{tool}", json=args)
    return res.json()


def agent_respond(user_input: str):
    # 🔥 LIVE TOOL REFRESH EVERY REQUEST
    tools = get_all_tools()

    system_prompt = f"""
You are an intelligent AI agent with access to tools.

Tools available:
{json.dumps(tools, indent=2)}

If a tool is required, respond ONLY as JSON:
{{"tool": "...", "arguments": {{...}}}}

Otherwise respond normally.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    response = llm.invoke(messages)
    text = response.content.strip()

    try:
        call = json.loads(text)
        tool = call["tool"]
        args = call["arguments"]

        if tool not in tools:
            return f"⚠️ Tool '{tool}' not found"

        server = tools[tool]["server"]
        result = call_tool(server, tool, args)

        return f"🛠 Tool `{tool}` executed → {result}"

    except Exception:
        return text


if __name__ == "__main__":
    while True:
        q = input("\nUser: ")
        print("Agent:", agent_respond(q))
