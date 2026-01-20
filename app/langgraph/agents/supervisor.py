from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")

def supervisor_decision(query: str) -> str:
    prompt = f"""
You are a supervisor AI.
Decide which agent should handle the task.

If question is about programming → respond ONLY: coding
If question is about knowledge, theory, explanation → respond ONLY: research

Question: {query}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip().lower()
