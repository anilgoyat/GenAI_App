from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    PydanticOutputParser
)

from app.structured_output.user_schema import UserProfile

def get_parser(parser_type="str"):
    parser_type = parser_type.lower()

    if parser_type == "str":
        return StrOutputParser()

    if parser_type == "json":
        return JsonOutputParser()

    if parser_type == "pydantic":
        return PydanticOutputParser(pydantic_object=UserProfile)

    raise ValueError(f"Unknown parser type: {parser_type}")
