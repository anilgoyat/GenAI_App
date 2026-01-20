from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from app.core.llm import get_llm

client = Client()

DATASET_NAME = "langchain-eval-dataset"

def create_dataset_if_not_exists():
    datasets = client.list_datasets()
    for d in datasets:
        if d.name == DATASET_NAME:
            return d.id

    dataset = client.create_dataset(
        dataset_name=DATASET_NAME,
        description="Evaluation dataset for LangChain concepts"
    )
    return dataset.id


def add_examples(dataset_id):
    examples = [
        {"input": "What is RAG?"},
        {"input": "Explain LCEL"},
        {"input": "What is a vector database?"}
    ]

    outputs = [
        {"answer": "RAG combines retrieval and generation"},
        {"answer": "LCEL is LangChain Expression Language"},
        {"answer": "A vector DB stores embeddings for similarity search"}
    ]

    client.create_examples(
        inputs=examples,
        outputs=outputs,
        dataset_id=dataset_id
    )


def main():
    dataset_id = create_dataset_if_not_exists()
    add_examples(dataset_id)

    llm = get_llm("groq")

    prompt = ChatPromptTemplate.from_template(
        "Answer this question accurately:\n{input}"
    )

    chain = (
        {"input": RunnablePassthrough()}
        | prompt
        | llm
    )

    examples = client.list_examples(dataset_id=dataset_id)

    print("\n--- Running evaluation locally ---")
    for ex in examples:
        result = chain.invoke(ex.inputs["input"])
        print("Q:", ex.inputs["input"])
        print("Model:", result.content)
        print("Expected:", ex.outputs["answer"])
        print("-" * 50)


if __name__ == "__main__":
    main()
