from app.prompts.prompt_factory import get_prompt
from app.core.parsers import get_parser
from app.core.llm import get_llm

def get_structured_chain(provider="groq"):
    llm = get_llm(provider)
    parser = get_parser("pydantic")
    prompt = get_prompt("structured_chat", parser=parser)

    return prompt | llm | parser
