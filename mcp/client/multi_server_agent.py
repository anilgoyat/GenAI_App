import requests
import json
from app.core.llm import get_llm

llm = get_llm("groq")

SERVERS = {
    "math": "http://localhost:8000",
    "time": "http://localhost:8001",
}


def fetch_all_tools():
    all_tools = {}

    for name, base in SERVERS.items():
        res = requests.get(f"{base}/tools").json()

        for tool_name, meta in res.items():
            all_tools[tool_name] = {
                **meta,
                "server": base
            }

    return all_tools


def call_tool(server, tool, args):
    res = requests.post(f"{server}/tools/{tool}", json=args)
    return res.json()


def agent_respond(user_input: str):
    tools = fetch_all_tools()

    system_prompt = f"""
You are an agent with access to distributed tools.

Tools:
{json.dumps(tools, indent=2)}

If tool needed, respond ONLY in JSON:
{{"tool": "...", "arguments": {{...}}}}

Else respond normally.
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

        server = tools[tool]["server"]
        result = call_tool(server, tool, args)

        return f"Tool `{tool}` result: {result}"

    except Exception:
        return text


if __name__ == "__main__":
    while True:
        q = input("\nUser: ")
        print("Agent:", agent_respond(q))
