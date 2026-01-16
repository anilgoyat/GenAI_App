from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

summary_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
    Explain the topic "{input}" in a concise manner.
    Provide:
    - Clear explanation
    - Real-world examples
    - Why is matters
    """
)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful senior AI engineer."),
    ("human", "Explain {input} for a frontend developer."),
])

def get_chat_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful senior AI engineer."),
        ("human", "Explain {input} for a frontend developer."),
    ])