from langgraph.graph import StateGraph, END
from typing import TypedDict
from .vision_agent import vision_reason

class VisionState(TypedDict):
    image: str
    question: str
    answer: str

def vision_node(state: VisionState):
    result = vision_reason(
        image_description=state["image"],
        user_query=state["question"]
    )
    return {"answer": result}

def build_vision_graph():
    graph = StateGraph(VisionState)
    graph.add_node("vision", vision_node)
    graph.set_entry_point("vision")
    graph.add_edge("vision", END)
    return graph.compile()
