from langsmith import Client
from langsmith import evaluate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from app.core.llm import get_llm

client = Client()

DATASET_NAME = "langchain-eval-dataset"


def get_dataset():
    datasets = list(client.list_datasets())
    for d in datasets:
        if d.name == DATASET_NAME:
            return d
    raise ValueError("Dataset not found. Run dataset_demo.py first.")


def main():
    dataset = get_dataset()

    llm = get_llm("groq")

    # -----------------------
    # Prompt Version 1
    # -----------------------
    prompt_v1 = ChatPromptTemplate.from_template(
        "Answer the question:\n{input}"
    )

    chain_v1 = (
        {"input": RunnablePassthrough()}
        | prompt_v1
        | llm
    )

    # -----------------------
    # Prompt Version 2
    # -----------------------
    prompt_v2 = ChatPromptTemplate.from_template(
        """
You are an expert AI tutor.
Give clear, concise, technically accurate answers.

Question:
{input}
"""
    )

    chain_v2 = (
        {"input": RunnablePassthrough()}
        | prompt_v2
        | llm
    )

    # -----------------------
    # Wrap chains as targets
    # -----------------------
    def target_v1(example):
        # example contains dataset row like: {"input": "..."}
        result = chain_v1.invoke(example["input"])
        return {"output": result.content if hasattr(result, "content") else str(result)}

    def target_v2(example):
        result = chain_v2.invoke(example["input"])
        return {"output": result.content if hasattr(result, "content") else str(result)}

    # -----------------------
    # Run evaluations
    # -----------------------
    print("\n🚀 Running Experiment V1...")
    evaluate(
        target_v1,
        data=dataset.name,
        experiment_prefix="Prompt-Experiment-V1",
    )

    print("\n🚀 Running Experiment V2...")
    evaluate(
        target_v2,
        data=dataset.name,
        experiment_prefix="Prompt-Experiment-V2",
    )

    print("\n✅ Experiments submitted to LangSmith UI")


if __name__ == "__main__":
    main()
