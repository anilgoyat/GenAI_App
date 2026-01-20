from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")

def planner_agent(user_input: str) -> str:
    prompt = f"""
You are a planner AI.
Break the user's task into clear steps.

User task:
{user_input}

Return numbered plan.
"""
    return llm.invoke([HumanMessage(content=prompt)]).content


def router_agent(plan: str) -> str:
    prompt = f"""
You are a router.
Decide which agent should handle the plan.

Agents available:
- executor (general reasoning)
- tool (if math or function needed)
- memory (if recalling past info)

Plan:
{plan}

Return one word: executor, tool, or memory
"""
    return llm.invoke([HumanMessage(content=prompt)]).content.strip().lower()


def executor_agent(task: str) -> str:
    prompt = f"Execute this task:\n{task}"
    return llm.invoke([HumanMessage(content=prompt)]).content


def memory_agent(task: str) -> str:
    return f"(Memory lookup simulated) I remember related info about: {task}"


def tool_agent(task: str) -> str:
    # For now simulated
    return f"(Tool executed) Result for: {task}"
