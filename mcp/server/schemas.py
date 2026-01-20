# mcp/server/schemas.py

from pydantic import BaseModel
from typing import List

class ToolSchema(BaseModel):
    name: str
    description: str
    parameters: dict
