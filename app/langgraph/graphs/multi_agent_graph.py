from langgraph.graph import StateGraph, END
from typing import TypedDict

from app.langgraph.agents.supervisor import supervisor_decision
from app.langgraph.agents.research_agent import research_agent
from app.langgraph.agents.coding_agent import coding_agent


class AgentState(TypedDict):
    query: str
    response: str


def supervisor_node(state: AgentState):
    decision = supervisor_decision(state["query"])
    print(f"\n[Supervisor] Routing decision → {decision.upper()} agent")
    return {"route": decision}


def research_node(state: AgentState):
    answer = research_agent(state["query"])
    print("[Research Agent] Handling the query...")
    return {"response": answer}


def coding_node(state: AgentState):
    answer = coding_agent(state["query"])
    print("[Coding Agent] Handling the query...")
    return {"response": answer}


def build_multi_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("research", research_node)
    graph.add_node("coding", coding_node)

    graph.set_entry_point("supervisor")

    graph.add_conditional_edges(
        "supervisor",
        lambda x: x["route"],
        {
            "research": "research",
            "coding": "coding"
        }
    )

    graph.add_edge("research", END)
    graph.add_edge("coding", END)

    return graph.compile()
