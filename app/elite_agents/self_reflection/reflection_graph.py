from langgraph.graph import StateGraph, END
from typing import TypedDict
from .reflection_agents import draft_agent, critic_agent, improver_agent

class ReflectionState(TypedDict):
    question: str
    draft: str
    critique: str
    final: str

def draft_node(state: ReflectionState):
    return {"draft": draft_agent(state["question"])}

def critic_node(state: ReflectionState):
    return {"critique": critic_agent(state["draft"])}

def improve_node(state: ReflectionState):
    return {"final": improver_agent(state["draft"], state["critique"])}

def build_reflection_graph():
    graph = StateGraph(ReflectionState)

    graph.add_node("draft", draft_node)
    graph.add_node("critic", critic_node)
    graph.add_node("improve", improve_node)

    graph.set_entry_point("draft")
    graph.add_edge("draft", "critic")
    graph.add_edge("critic", "improve")
    graph.add_edge("improve", END)

    return graph.compile()
