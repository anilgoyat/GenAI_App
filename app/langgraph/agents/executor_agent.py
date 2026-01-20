from app.core.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

llm = get_llm("groq")

def executor_agent(step: str) -> str:
    messages = [
        SystemMessage(content="You are an executor. Perform the given step."),
        HumanMessage(content=step),
    ]

    response = llm.invoke(messages)
    return response.content
