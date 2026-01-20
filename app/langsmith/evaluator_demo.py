from langsmith import Client
from langsmith import evaluate
from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm

client = Client()

DATASET_NAME = "langchain-eval-dataset"


def get_dataset():
    datasets = list(client.list_datasets())
    for d in datasets:
        if d.name == DATASET_NAME:
            return d
    raise ValueError("Dataset not found.")


# -----------------------
# Custom evaluator
# -----------------------
def relevance_evaluator(run, example):
    """
    run.outputs -> model output
    example.inputs -> original dataset input
    """

    llm = get_llm("groq")

    judge_prompt = ChatPromptTemplate.from_template("""
You are a strict evaluator.

Question:
{question}

Model Answer:
{answer}

Score relevance from 1 to 10.
Return only the number.
""")

    response = (judge_prompt | llm).invoke({
        "question": example.inputs["input"],
        "answer": run.outputs["output"]
    })

    try:
        score = int(response.content.strip())
    except:
        score = 0

    return {
        "key": "relevance",
        "score": score
    }


# -----------------------
# Main
# -----------------------
def main():
    dataset = get_dataset()
    llm = get_llm("groq")

    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_template(
        "Explain clearly:\n{input}"
    )

    chain = (
        {"input": RunnablePassthrough()}
        | prompt
        | llm
    )

    def target(example):
        result = chain.invoke(example["input"])
        return {"output": result.content}

    print("🚀 Running evaluation with custom evaluator...")

    evaluate(
        target,
        data=dataset.name,
        evaluators=[relevance_evaluator],
        experiment_prefix="Evaluator-Demo"
    )

    print("✅ Check LangSmith UI → Project: Evaluator-Demo")


if __name__ == "__main__":
    main()
