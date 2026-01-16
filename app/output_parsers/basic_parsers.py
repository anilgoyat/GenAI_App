from langchain_core.output_parsers import PydanticOutputParser
from app.structured_output.user_schema import UserProfile
def get_basic_parser():
    return PydanticOutputParser(pydantic_object=UserProfile)