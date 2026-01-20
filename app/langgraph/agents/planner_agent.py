from app.core.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

llm = get_llm("groq")

def planner_agent(goal: str) -> str:
    messages = [
        SystemMessage(content="You are a planner. Break the goal into clear steps."),
        HumanMessage(content=goal),
    ]

    response = llm.invoke(messages)
    return response.content
