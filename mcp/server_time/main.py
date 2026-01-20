from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/tools")
def list_tools():
    return {
        "get_time": {
            "description": "Get current system time",
            "arguments": {}
        }
    }


@app.post("/tools/get_time")
def get_time():
    return {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
