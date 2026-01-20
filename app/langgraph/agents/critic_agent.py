from app.core.llm import get_llm

llm = get_llm("groq")

def critic_node(state):
    research = state.get("research", "")

    prompt = f"""
You are a critic agent.
Improve clarity, correctness and structure.

Research:
{research}

Return refined critique.
"""

    response = llm.invoke(prompt)

    return {
        "critique": response.content
    }
