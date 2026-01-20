from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from app.core.llm import get_llm

def main():
    llm = get_llm("groq").with_config(run_name="groq_llm")

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple terms"
    ).with_config(run_name="simple_prompt")

    chain = (
        {"topic": RunnablePassthrough()}
        | prompt
        | llm
    ).with_config(run_name="simple_chain")

    print(chain.invoke("LangGraph"))

if __name__ == "__main__":
    main()
