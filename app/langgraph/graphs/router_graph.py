from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.langgraph.agents.router_agent import route_query
from app.langgraph.agents.executor_agent import executor_agent

class RouterState(TypedDict):
    input: str
    route: str
    output: str


def router_node(state):
    route = route_query(state["input"])
    print("[Router decided]:", route)
    return {"route": route}


def agent_node(state):
    result = executor_agent(state["input"])
    return {"output": result}


def build_router_graph():
    graph = StateGraph(RouterState)

    graph.add_node("router", router_node)
    graph.add_node("agent", agent_node)

    graph.set_entry_point("router")
    graph.add_edge("router", "agent")
    graph.add_edge("agent", END)

    return graph.compile()
