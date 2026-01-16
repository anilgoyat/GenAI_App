from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ..core.llm import get_llm


class QueryTransformer:
    def __init__(self, provider="groq"):
        self.llm = get_llm(provider)

    # -------------------------
    # 1. Query Rewriting
    # -------------------------
    def rewrite_query(self, query: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert at rewriting search queries for better document retrieval."),
            ("human", "Rewrite this query to be clearer and more effective:\n\n{query}")
        ])

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"query": query})

    # -------------------------
    # 2. Multi Query Expansion
    # -------------------------
    def multi_query(self, query: str, n: int = 4) -> List[str]:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Generate multiple diverse search queries for better document retrieval."),
            ("human", "Generate {n} different search queries for: {{query}}\nReturn each on new line.")
        ])

        chain = prompt | self.llm | StrOutputParser()
        result = chain.invoke({"query": query, "n": n})
        return [q.strip() for q in result.split("\n") if q.strip()]

    # -------------------------
    # 3. HyDE (Hypothetical Answer Generation)
    # -------------------------
    def hyde(self, query: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You generate a hypothetical answer to help retrieve relevant documents."),
            ("human", "Write a detailed hypothetical answer for this question:\n\n{query}")
        ])

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"query": query})


def get_query_transformer(provider="groq"):
    return QueryTransformer(provider)
