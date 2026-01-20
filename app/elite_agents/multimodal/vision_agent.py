from app.core.llm import get_llm
from langchain_core.messages import HumanMessage

llm = get_llm("groq")  # replace with vision-capable model later

def vision_reason(image_description: str, user_query: str):
    """
    For now we simulate vision input using image description.
    Later we can connect actual image input.
    """

    prompt = f"""
You are a multimodal AI assistant.

Image description:
{image_description}

User question:
{user_query}

Analyze the image and answer intelligently.
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
