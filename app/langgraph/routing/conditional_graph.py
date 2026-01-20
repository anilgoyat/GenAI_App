from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from app.core.llm import get_llm


# --------------------
# 1. State
# --------------------
class RouteState(TypedDict):
    input: str
    decision: str
    output: str

# --------------------
# 2. Router node
# --------------------
def router(state: RouteState):
    text = state["input"].lower()

    if "add" in text or "sum" in text:
        return {"decision": "math"}

    elif "langgraph" in text:
        return {"decision": "llm"}
    else:
        return {"decision": "general"}
    
# --------------------
# 3. Nodes
# --------------------
def math_node(state: RouteState):
    return {"output": "I detected a math question."}

def general_node(state: RouteState):
    return {"output": "General small talk detected."}

def llm_node(state: RouteState):
    llm = get_llm("groq")
    response = llm.invoke(state["input"])
    return {"output": response.content}

# --------------------
# 4. Build graph
# --------------------
def build_conditional_graph():
    builder = StateGraph(RouteState)
    builder.add_node("router", router)
    builder.add_node("math", math_node)
    builder.add_node("general", general_node)
    builder.add_node("llm", llm_node)

    builder.set_entry_point("router")
    builder.add_conditional_edges(
        "router",
        lambda state: state["decision"],
        {
            "math": "math",
            "general": "general",
            "llm": "llm"
        }
    )

    builder.add_edge("math", END)
    builder.add_edge("general", END)
    builder.add_edge("llm", END)
    
    return builder.compile()