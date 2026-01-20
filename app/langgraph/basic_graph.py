from langgraph.graph import StateGraph, END
from .state import GraphState
from ..core.llm import get_llm

llm = get_llm("groq")

def llm_node(state: GraphState) -> GraphState:
    user_input = state["input"]

    response = llm.invoke(user_input)

    return {
        "input": user_input,
        "output": response.content
    }

def build_basic_graph():
    graph = StateGraph(GraphState)

    graph.add_node("chat", llm_node)

    graph.set_entry_point("chat")
    graph.add_edge("chat", END)

    return graph.compile()
