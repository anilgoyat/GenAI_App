from app.core.llm import get_llm

llm = get_llm("groq")

def writer_node(state):
    question = state["messages"][-1].content
    critique = state.get("critique", "")

    prompt = f"""
You are a senior technical writer.

Question:
{question}

Critique:
{critique}

Write final answer.
"""

    response = llm.invoke(prompt)

    return {
        "final": response.content
    }
