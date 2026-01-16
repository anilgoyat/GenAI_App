from pydantic import BaseModel, Field
from typing import List

class UserProfile(BaseModel):
    name: str = Field(description="The full name of the user")
    age: int = Field(description="The age of the user in years")
    skills: List[str] = Field(description="A list of user's skills")