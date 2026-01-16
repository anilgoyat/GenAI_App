# app/rag/router.py

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def build_router_chain(llm):
    """
    Router decides whether query should go to RAG or direct LLM.
    Returns: Runnable chain
    """

    prompt = PromptTemplate.from_template("""
You are a routing controller for an AI system.

Decide where the user query should be handled.

Rules:
- If the query is about LangChain, LCEL, RAG, embeddings, retrievers, vector databases → return RAG
- Otherwise → return LLM

Return ONLY one word:
RAG or LLM

User query:
{input}
""")

    chain = prompt | llm | StrOutputParser()

    return chain
