from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.langgraph.subgraphs.research_graph import build_research_graph
from app.langgraph.subgraphs.explain_graph import build_explain_graph
from app.langgraph.subgraphs.code_graph import build_code_graph

research_app = build_research_graph()
explain_app = build_explain_graph()
code_app = build_code_graph()

class SupervisorState(TypedDict):
    input: str
    research: str
    explanation: str
    code: str
    final: str


def research_node(state):
    return research_app.invoke({"input": state["input"]})


def explain_node(state):
    return explain_app.invoke({"input": state["input"]})


def code_node(state):
    return code_app.invoke({"input": state["input"]})


def merge_node(state):
    return {
        "final": f"""
Research:
{state.get('research', '')}

Explanation:
{state.get('explanation', '')}

Code:
{state.get('code', '')}
"""
    }


def build_supervisor_graph():
    graph = StateGraph(SupervisorState)

    graph.add_node("research", research_node)
    graph.add_node("explain", explain_node)
    graph.add_node("code", code_node)
    graph.add_node("merge", merge_node)

    graph.set_entry_point("research")

    graph.add_edge("research", "explain")
    graph.add_edge("research", "code")

    graph.add_edge("explain", "merge")
    graph.add_edge("code", "merge")

    graph.add_edge("merge", END)

    return graph.compile()
