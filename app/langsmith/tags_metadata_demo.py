from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from app.core.llm import get_llm

def main():
    llm = get_llm("groq").with_config(
        run_name="groq_llm",
        tags=["llm", "groq"],
        metadata={"env": "dev"}
    )

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple terms"
    ).with_config(
        run_name="prompt_v1",
        tags=["prompt"],
        metadata={"version": "1.0"}
    )

    chain = (
        {"topic": RunnablePassthrough()}
        | prompt
        | llm
    ).with_config(
        run_name="langsmith_demo_chain",
        tags=["demo", "experiment-1"],
        metadata={"author": "anil"}
    )

    print(chain.invoke("RAG"))

if __name__ == "__main__":
    main()
