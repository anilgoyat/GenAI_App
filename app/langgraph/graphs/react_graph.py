from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage
from app.core.llm import get_llm
from app.tools.basic_tools import add_numbers

llm = get_llm("groq")

class ReActState(TypedDict):
    messages: List


def reason_node(state):
    response = llm.invoke(state["messages"])
    state["messages"].append(response)
    return {"messages": state["messages"]}


def tool_node(state):
    last = state["messages"][-1]

    # If model asks to use tool
    if last.tool_calls:
        tool_call = last.tool_calls[0]
        if tool_call["name"] == "add_numbers":
            args = tool_call["args"]
            result = add_numbers(**args)
            state["messages"].append(AIMessage(content=f"Tool result: {result}"))
    return {"messages": state["messages"]}


def should_continue(state):
    last = state["messages"][-1].content.lower()
    if "final" in last:
        return END
    return "tool"


def build_react_graph():
    graph = StateGraph(ReActState)

    graph.add_node("reason", reason_node)
    graph.add_node("tool", tool_node)

    graph.set_entry_point("reason")
    graph.add_conditional_edges("reason", should_continue)
    graph.add_edge("tool", "reason")

    return graph.compile()
