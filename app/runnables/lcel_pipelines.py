from langchain_core.runnables import (
    RunnableLambda,
    RunnableMap,
    RunnablePassthrough
)

from app.core.llm import get_llm
from app.prompts.prompt_factory import get_prompt
from app.core.parsers import get_parser


# ----------------------------
# 1. Simple LCEL pipeline
# ----------------------------
def basic_lcel_chain():
    llm = get_llm()
    prompt = get_prompt("chat_basic")

    return prompt | llm


# ----------------------------
# 2. LCEL with transformation
# ----------------------------
def transformed_chain():
    llm = get_llm()
    prompt = get_prompt("chat_basic")

    clean_input = RunnableLambda(lambda x: {"input": x["input"].strip().lower()})

    return clean_input | prompt | llm


# ----------------------------
# 3. Parallel execution (RunnableMap)
# ----------------------------
def parallel_chain():
    llm = get_llm()

    summary_prompt = get_prompt("text_basic")
    explanation_prompt = get_prompt("chat_basic")

    return RunnableMap({
        "summary": summary_prompt | llm,
        "explanation": explanation_prompt | llm
    })


# ----------------------------
# 4. Passthrough example
# ----------------------------
def passthrough_chain():
    llm = get_llm()
    prompt = get_prompt("chat_basic")

    return RunnableMap({
        "original": RunnablePassthrough(),
        "llm_response": prompt | llm
    })

# ----------------------------
# 5. Retry mechanism example
def retry_chain():
    llm = get_llm()
    prompt = get_prompt("chat_basic")

    chain = prompt | llm

    # Retry up to 3 times with exponential backoff
    return chain.with_retry(
            max_attempts=2,
            wait_exponential_jitter=True
    )

# --------------------------
# 6. Fallback mechanism example
# ----------------------------

def fallback_chain():
    primary_llm = get_llm(provider="gemini")
    backup_llm = get_llm(provider="groq")

    prompt = get_prompt("chat_basic")

    primary_chain = prompt | primary_llm
    fallback_chain = prompt | backup_llm

    return primary_chain.with_fallbacks([fallback_chain])

def conditional_chain():
    llm = get_llm()

    tech_prompt = get_prompt("chat_basic")
    nontech_prompt = get_prompt("text_basic")

    tech_chain = tech_prompt | llm
    simple_chain = nontech_prompt | llm

    def router(inputs):
        text = inputs["input"].lower()
        if "code" in text or "python" in text or "langchain" in text:
            return tech_chain
        return simple_chain

    return RunnableLambda(router)
