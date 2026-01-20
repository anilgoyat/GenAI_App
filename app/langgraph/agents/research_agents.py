from app.core.llm import get_llm

llm = get_llm("groq")

def research_node(state):
    question = state["messages"][-1].content

    prompt = f"""
You are a research agent.
Provide concise factual research for the question.

Question:
{question}

Return only bullet points.
"""

    response = llm.invoke(prompt)

    # IMPORTANT: must return dict only
    return {
        "research": response.content
    }
