from typing import TypedDict

class AgentOSState(TypedDict):
    input: str
    plan: str
    route: str
    output: str
