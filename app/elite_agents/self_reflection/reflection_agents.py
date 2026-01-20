from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")

def draft_agent(question: str) -> str:
    prompt = f"Answer this question clearly:\n{question}"
    return llm.invoke([HumanMessage(content=prompt)]).content


def critic_agent(draft: str) -> str:
    prompt = f"""
You are a strict reviewer.
Critique the following answer and point out weaknesses, missing details, or inaccuracies.

Answer:
{draft}
"""
    return llm.invoke([HumanMessage(content=prompt)]).content


def improver_agent(draft: str, critique: str) -> str:
    prompt = f"""
You are an expert editor.
Improve the original answer using the critique.

Original answer:
{draft}

Critique:
{critique}

Return improved final answer.
"""
    return llm.invoke([HumanMessage(content=prompt)]).content
