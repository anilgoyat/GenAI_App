from langchain.agents import create_agent
from app.core.llm import get_llm
from app.tools.basic_tools import add_numbers, get_current_time
from langchain.messages import AIMessage
from langchain_core.messages import HumanMessage

SYSTEM_PROMPT = """
You are a tool-using assistant.

You can only use these tools:
- add_numbers(a, b)
- get_current_time()

If a tool is not relevant, respond normally.
Never call tools that are not listed.
"""
# Simple in-memory session store
_SESSION_STORE = {}

def get_basic_agent(provider="groq"):
    llm = get_llm(provider)

    agent = create_agent(
        model=get_llm(provider),
        tools=[add_numbers, get_current_time],
        system_prompt=SYSTEM_PROMPT
    )

    return agent


def run_agent(agent, user_input: str, session_id: str = "default"):
    if session_id not in _SESSION_STORE:
        _SESSION_STORE[session_id] = []

    history = _SESSION_STORE[session_id]

    history.append(HumanMessage(content=user_input))

    result = agent.invoke({
        "messages": history
    })

    # Update memory with agent's messages
    _SESSION_STORE[session_id] = result["messages"]

    return result["messages"][-1].content

