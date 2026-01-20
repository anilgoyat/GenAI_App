ROLE_PERMISSIONS = {
    "admin": ["*"],  # all tools
    "developer": ["add", "multiply", "time"],
    "user": ["time"],
    "guest": []
}

def is_tool_allowed(role: str, tool: str) -> bool:
    allowed = ROLE_PERMISSIONS.get(role, [])
    return "*" in allowed or tool in allowed
