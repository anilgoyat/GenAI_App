from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.core.llm import get_llm

llm = get_llm("groq")


class TeamState(TypedDict):
    input: str
    research: str
    draft: str
    review: str
    final: str


def researcher_node(state: TeamState):
    prompt = f"Research key points about: {state['input']}"
    research = llm.invoke(prompt).content
    return {"research": research}


def writer_node(state: TeamState):
    prompt = f"""
Write a clear explanation using this research:

Research:
{state['research']}
"""
    draft = llm.invoke(prompt).content
    return {"draft": draft}


def reviewer_node(state: TeamState):
    prompt = f"""
Improve this answer. Fix mistakes, add clarity.

Draft:
{state['draft']}
"""
    review = llm.invoke(prompt).content
    return {"review": review}


def supervisor_node(state: TeamState):
    prompt = f"""
Provide final high-quality answer based on this:

Reviewed Answer:
{state['review']}
"""
    final = llm.invoke(prompt).content
    return {"final": final}


def build_team_graph():
    graph = StateGraph(TeamState)

    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)
    graph.add_node("reviewer", reviewer_node)
    graph.add_node("supervisor", supervisor_node)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", "supervisor")
    graph.add_edge("supervisor", END)

    return graph.compile()
