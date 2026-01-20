from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")

class ResearchState(TypedDict):
    input: str
    research: str


def research_node(state):
    prompt = f"Do deep research on: {state['input']}"
    return {"research": llm.invoke(prompt).content}


def build_research_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("research", research_node)
    graph.set_entry_point("research")
    graph.add_edge("research", END)
    return graph.compile()
