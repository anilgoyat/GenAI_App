from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")


class ReflexionState(TypedDict):
    question: str
    answer: str
    critique: str
    improved_answer: str


def generator(state: ReflexionState):
    prompt = f"Answer this clearly:\n{state['question']}"
    answer = llm.invoke(prompt).content
    return {"answer": answer}


def critic(state: ReflexionState):
    prompt = f"""
Critique this answer. Identify flaws, missing details, and improvements.

Answer:
{state['answer']}
"""
    critique = llm.invoke(prompt).content
    return {"critique": critique}


def refiner(state: ReflexionState):
    prompt = f"""
Improve this answer using the critique.

Answer:
{state['answer']}

Critique:
{state['critique']}
"""
    improved = llm.invoke(prompt).content
    return {"improved_answer": improved}


def build_reflexion_graph():
    graph = StateGraph(ReflexionState)

    graph.add_node("generator", generator)
    graph.add_node("critic", critic)
    graph.add_node("refiner", refiner)

    graph.set_entry_point("generator")
    graph.add_edge("generator", "critic")
    graph.add_edge("critic", "refiner")
    graph.add_edge("refiner", END)

    return graph.compile()
