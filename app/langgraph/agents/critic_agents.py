from app.core.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

llm = get_llm("groq")

def critic_agent(result: str) -> str:
    messages = [
        SystemMessage(content="You are a critic. Say APPROVED or IMPROVE with reason."),
        HumanMessage(content=result),
    ]

    response = llm.invoke(messages)
    return response.content
