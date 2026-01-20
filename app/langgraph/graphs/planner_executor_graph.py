from langgraph.graph import StateGraph, END
from typing import TypedDict

from app.langgraph.agents.planner_agent import planner_agent
from app.langgraph.agents.executor_agent import executor_agent
from app.langgraph.agents.critic_agents import critic_agent


class AgentState(TypedDict):
    goal: str
    plan: str
    execution: str
    feedback: str


def plan_node(state):
    plan = planner_agent(state["goal"])
    print("\n[Planner]\n", plan)
    return {"plan": plan}


def execute_node(state):
    result = executor_agent(state["plan"])
    print("\n[Executor]\n", result)
    return {"execution": result}


def critic_node(state):
    feedback = critic_agent(state["execution"])
    print("\n[Critic]\n", feedback)
    return {"feedback": feedback}


def build_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", plan_node)
    graph.add_node("executor", execute_node)
    graph.add_node("critic", critic_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "critic")
    graph.add_edge("critic", END)

    return graph.compile()
