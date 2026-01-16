from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


def build_rag_chain(retriever, llm):

    prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
""")
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return chain
