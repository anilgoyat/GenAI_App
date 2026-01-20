from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from app.langgraph.state import AgentState
from app.langgraph.agents.research_agents import research_node
from app.langgraph.agents.critic_agent import critic_node
from app.langgraph.agents.writer_agent import writer_node

memory = MemorySaver()

def build_collaborative_graph():
    graph = StateGraph(AgentState)

    graph.add_node("research", research_node)
    graph.add_node("critic", critic_node)
    graph.add_node("writer", writer_node)

    graph.set_entry_point("research")
    graph.add_edge("research", "critic")
    graph.add_edge("critic", "writer")
    graph.add_edge("writer", END)

    return graph.compile(checkpointer=memory)
