from langgraph.graph import StateGraph, END
from .agents import planner_agent, router_agent, executor_agent, tool_agent, memory_agent
from .state import AgentOSState

def planner_node(state: AgentOSState):
    return {"plan": planner_agent(state["input"])}

def router_node(state: AgentOSState):
    return {"route": router_agent(state["plan"])}

def executor_node(state: AgentOSState):
    return {"output": executor_agent(state["input"])}

def tool_node(state: AgentOSState):
    return {"output": tool_agent(state["input"])}

def memory_node(state: AgentOSState):
    return {"output": memory_agent(state["input"])}

def route_logic(state: AgentOSState):
    if "tool" in state["route"]:
        return "tool"
    if "memory" in state["route"]:
        return "memory"
    return "executor"

def build_agent_os():
    graph = StateGraph(AgentOSState)

    graph.add_node("planner", planner_node)
    graph.add_node("router", router_node)
    graph.add_node("executor", executor_node)
    graph.add_node("tool", tool_node)
    graph.add_node("memory", memory_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "router")

    graph.add_conditional_edges(
        "router",
        route_logic,
        {
            "executor": "executor",
            "tool": "tool",
            "memory": "memory",
        }
    )

    graph.add_edge("executor", END)
    graph.add_edge("tool", END)
    graph.add_edge("memory", END)

    return graph.compile()
