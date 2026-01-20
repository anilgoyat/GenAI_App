from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")

def research_agent(query: str):
    messages = [
        HumanMessage(content=f"You are a research agent.Collect factual, useful information about:\n{query}")
    ]
    return llm.invoke(messages).content
