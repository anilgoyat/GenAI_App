from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")

class CodeState(TypedDict):
    input: str
    code: str


def code_node(state):
    prompt = f"Write clean Python code for: {state['input']}"
    return {"code": llm.invoke(prompt).content}


def build_code_graph():
    graph = StateGraph(CodeState)
    graph.add_node("code", code_node)
    graph.set_entry_point("code")
    graph.add_edge("code", END)
    return graph.compile()
