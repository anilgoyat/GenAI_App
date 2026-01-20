from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from app.core.llm import get_llm

llm = get_llm("groq")


class PlannerState(TypedDict):
    input: str
    plan: List[str]
    result: str


def planner_node(state: PlannerState):
    prompt = f"""
You are a planner AI.
Break the task into clear step-by-step plan.

Task: {state['input']}

Return as bullet list.
"""
    plan_text = llm.invoke(prompt).content

    steps = [s.strip("- ").strip() for s in plan_text.split("\n") if s.strip()]
    return {"plan": steps}


def executor_node(state: PlannerState):
    results = []

    for step in state["plan"]:
        prompt = f"Execute this step carefully:\n{step}"
        response = llm.invoke(prompt).content
        results.append(f"Step: {step}\nResult: {response}")

    return {"result": "\n\n".join(results)}


def build_planner_graph():
    graph = StateGraph(PlannerState)

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", END)

    return graph.compile()
