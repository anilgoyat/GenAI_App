import json
import requests
from app.core.llm import get_llm
from .registry import get_all_tools
from .auth import get_user
from .permissions import is_tool_allowed

llm = get_llm("groq")


def call_tool(server, tool, args):
    res = requests.post(f"{server}/tools/{tool}", json=args)
    return res.json()


def agent_respond(username: str, user_input: str):
    user = get_user(username)
    role = user["role"]

    tools = get_all_tools()

    system_prompt = f"""
You are an AI agent.

User role: {role}

Available tools:
{json.dumps(tools, indent=2)}

If you want to use a tool, respond ONLY as JSON:
{{"tool": "...", "arguments": {{...}}}}
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

        # 🔐 PERMISSION CHECK
        if not is_tool_allowed(role, tool):
            return f"⛔ Access denied: role `{role}` cannot use `{tool}`"

        server = tools[tool]["server"]
        result = call_tool(server, tool, args)

        return f"🛠 {tool} executed → {result}"

    except Exception:
        return text


if __name__ == "__main__":
    print("Login as: anil / guest / dev")
    username = input("Username: ")

    while True:
        q = input("\nUser: ")
        print("Agent:", agent_respond(username, q))
