from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ..core.llm import get_llm


class SimpleLLMReranker:
    def __init__(self, provider="groq"):
        self.llm = get_llm(provider)

    def rerank(self, query: str, docs: List[str], top_k: int = 3) -> List[str]:
        joined_docs = "\n\n".join(
            [f"Document {i+1}:\n{doc}" for i, doc in enumerate(docs)]
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert information retrieval system. Rank documents by relevance."),
            ("human", f"""
Query: {query}

Documents:
{joined_docs}

Return the numbers of the {top_k} most relevant documents in order.
Only return comma separated numbers like: 1,3,2
""")
        ])

        chain = prompt | self.llm | StrOutputParser()
        result = chain.invoke({})

        try:
            indexes = [int(i.strip()) - 1 for i in result.split(",")]
            return [docs[i] for i in indexes if 0 <= i < len(docs)]
        except:
            # fallback if LLM output malformed
            return docs[:top_k]


def get_reranker(provider="groq"):
    return SimpleLLMReranker(provider)
