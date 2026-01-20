import requests

SERVERS = {
    "math": "http://localhost:8000",
    "time": "http://localhost:8001",
}

def get_all_tools():
    """
    Always fetch latest tools dynamically from all servers.
    """
    all_tools = {}

    for name, base in SERVERS.items():
        try:
            res = requests.get(f"{base}/tools", timeout=2).json()

            for tool_name, meta in res.items():
                all_tools[tool_name] = {
                    **meta,
                    "server": base
                }

        except Exception as e:
            print(f"⚠️ Server {name} unavailable")

    return all_tools
