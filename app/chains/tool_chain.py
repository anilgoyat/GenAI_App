from app.core.llm import get_llm
from app.prompts.prompt_factory import get_prompt
from app.tools.basic_tools import add_numbers, get_current_time

def tool_calling_chain():
    llm = get_llm(provider="groq")
    llm_with_tools = llm.bind_tools([add_numbers, get_current_time])

    prompt = get_prompt("chat_basic")

    return prompt | llm_with_tools
