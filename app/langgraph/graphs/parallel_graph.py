from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")

class ParallelState(TypedDict):
    input: str
    explanation: str
    examples: str
    code: str
    final: str


def explain_node(state):
    prompt = f"Explain this topic clearly: {state['input']}"
    return {"explanation": llm.invoke(prompt).content}


def examples_node(state):
    prompt = f"Give real-world examples for: {state['input']}"
    return {"examples": llm.invoke(prompt).content}


def code_node(state):
    prompt = f"Write Python code for: {state['input']}"
    return {"code": llm.invoke(prompt).content}


def merge_node(state):
    final = f"""
Explanation:
{state['explanation']}

Examples:
{state['examples']}

Code:
{state['code']}
"""
    return {"final": final}


def build_parallel_graph():
    graph = StateGraph(ParallelState)

    graph.add_node("explain", explain_node)
    graph.add_node("examples", examples_node)
    graph.add_node("code", code_node)
    graph.add_node("merge", merge_node)

    # Entry
    graph.set_entry_point("explain")

    # Parallel edges
    graph.add_edge("explain", "examples")
    graph.add_edge("explain", "code")

    # Join
    graph.add_edge("examples", "merge")
    graph.add_edge("code", "merge")

    graph.add_edge("merge", END)

    return graph.compile()
