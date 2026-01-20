from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.core.llm import get_llm


# --------------------
# 1. State
# --------------------
class WorkflowState(TypedDict):
    input: str
    plan: str
    result: str
    final: str


# --------------------
# 2. Planner Node
# --------------------
def planner_node(state: WorkflowState):
    llm = get_llm("groq")

    prompt = f"""
You are a planner agent.
Break this task into a clear plan.

Task: {state['input']}
"""
    response = llm.invoke(prompt)

    return {"plan": response.content}


# --------------------
# 3. Executor Node
# --------------------
def executor_node(state: WorkflowState):
    llm = get_llm("groq")

    prompt = f"""
You are an executor agent.
Follow this plan and generate the result.

Plan:
{state['plan']}
"""
    response = llm.invoke(prompt)

    return {"result": response.content}


# --------------------
# 4. Validator Node
# --------------------
def validator_node(state: WorkflowState):
    llm = get_llm("groq")

    prompt = f"""
You are a reviewer agent.
Check this answer for correctness and improve it.

Answer:
{state['result']}
"""
    response = llm.invoke(prompt)

    return {"final": response.content}


# --------------------
# 5. Build Graph
# --------------------
def build_multi_node_graph():
    builder = StateGraph(WorkflowState)

    builder.add_node("planner", planner_node)
    builder.add_node("executor", executor_node)
    builder.add_node("validator", validator_node)

    builder.set_entry_point("planner")

    builder.add_edge("planner", "executor")
    builder.add_edge("executor", "validator")
    builder.add_edge("validator", END)

    return builder.compile()
