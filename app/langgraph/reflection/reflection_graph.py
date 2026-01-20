from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")


class ReflectionState(TypedDict):
    input: str
    draft: str
    critique: str
    final: str


def generator_node(state: ReflectionState):
    prompt = f"Answer the question clearly:\n{state['input']}"
    draft = llm.invoke(prompt).content
    return {"draft": draft}


def critic_node(state: ReflectionState):
    prompt = f"""
You are a critical reviewer.
Find weaknesses, missing points, or improvements.

Answer:
{state['draft']}
"""
    critique = llm.invoke(prompt).content
    return {"critique": critique}


def refiner_node(state: ReflectionState):
    prompt = f"""
Improve the answer using this critique.

Original answer:
{state['draft']}

Critique:
{state['critique']}
"""
    final = llm.invoke(prompt).content
    return {"final": final}


def build_reflection_graph():
    graph = StateGraph(ReflectionState)

    graph.add_node("generator", generator_node)
    graph.add_node("critic", critic_node)
    graph.add_node("refiner", refiner_node)

    graph.set_entry_point("generator")
    graph.add_edge("generator", "critic")
    graph.add_edge("critic", "refiner")
    graph.add_edge("refiner", END)

    return graph.compile()
