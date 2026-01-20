from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    approved: bool | None

class GraphState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    research: str
    critique: str
    final: str
