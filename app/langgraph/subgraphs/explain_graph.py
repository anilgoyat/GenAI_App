from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")

class ExplainState(TypedDict):
    input: str
    explanation: str


def explain_node(state):
    prompt = f"Explain clearly: {state['input']}"
    return {"explanation": llm.invoke(prompt).content}


def build_explain_graph():
    graph = StateGraph(ExplainState)
    graph.add_node("explain", explain_node)
    graph.set_entry_point("explain")
    graph.add_edge("explain", END)
    return graph.compile()
