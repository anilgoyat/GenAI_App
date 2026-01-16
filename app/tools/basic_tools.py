from langchain_core.tools import tool
from datetime import datetime

@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

@tool
def get_current_time() -> str:
    """Return the current system time as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")