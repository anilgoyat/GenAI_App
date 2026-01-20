from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from app.core.llm import get_llm

llm = get_llm("groq")


class PlanState(TypedDict):
    goal: str
    plan: List[str]
    current_step: int
    results: List[str]
    final: str


def planner_node(state: PlanState):
    prompt = f"""
You are a planner agent.
Break this goal into clear numbered steps.

Goal: {state['goal']}
"""
    plan_text = llm.invoke(prompt).content

    steps = [line.strip() for line in plan_text.split("\n") if line.strip()]
    return {"plan": steps, "current_step": 0, "results": []}


def executor_node(state: PlanState):
    step = state["plan"][state["current_step"]]

    prompt = f"""
Execute this step carefully:
Step: {step}
"""
    result = llm.invoke(prompt).content

    new_results = state["results"] + [result]
    return {"results": new_results}


def critic_node(state: PlanState):
    last_result = state["results"][-1]

    prompt = f"""
Evaluate this result:
{last_result}

Reply only YES or NO if the step is satisfactory.
"""
    verdict = llm.invoke(prompt).content.strip().upper()

    if verdict == "YES":
        return {"current_step": state["current_step"] + 1}
    else:
        return {"current_step": state["current_step"]}  # repeat step


def final_node(state: PlanState):
    combined = "\n".join(state["results"])
    return {"final": combined}


def router(state: PlanState):
    if state["current_step"] >= len(state["plan"]):
        return "final"
    return "executor"


def build_planner_graph():
    graph = StateGraph(PlanState)

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("critic", critic_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "critic")

    graph.add_conditional_edges(
        "critic",
        router,
        {
            "executor": "executor",
            "final": "final",
        }
    )

    graph.add_edge("final", END)

    return graph.compile()
