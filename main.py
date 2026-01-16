# from app.core.llm import get_llm
from app.chains.basic_chains import get_basic_chain, batch_chain, streaming_chain
from app.chains.structured_chains import get_structured_chain
from app.runnables.lcel_pipelines import (
    basic_lcel_chain,
    transformed_chain,
    parallel_chain,
    passthrough_chain,
    retry_chain,
    fallback_chain,
    conditional_chain
)
# from app.chains.tool_chain import tool_calling_chain
from app.agents.basic_agent import get_basic_agent, run_agent
from langchain_core.messages import HumanMessage
# from app.prompts.basic_prompts import summary_prompt, chat_prompt, get_chat_prompt
# from app.structured_output.user_schema import UserProfile
# from app.output_parsers.basic_parsers import get_basic_parser
# from app.core.parsers import get_parser
# from app.prompts.prompt_factory import get_prompt
def main():

    
    # llm = get_llm(provider="groq")# Debug line
    # parser = get_parser("pydantic")
    # prompt = get_prompt("text_basic")
    # chat_basic_prompt = get_prompt("chat_basic") remove parsing for now
    # text_basic_prompt = get_prompt("text_basic")
    # structured_chat_prompt = get_prompt("structured_chat", parser=parser)
    # chain = structured_chat_prompt | llm | parser
    # result = chain.invoke({"input": "I am software engineer with experience in Python and Machine Learning, aged 30, named Alice Smith."})
    # print(result)
    # basic parser usage
    # parser = get_basic_parser()
    # prompt = get_chat_prompt()
    # chain = prompt | llm | parser
    # print("---- Basic Parser Output ----")
    # print(chain.invoke({"input": "Artificial Intelligence"}))
    #convert normal prompt to structured prompt
    # structured_llm = llm.with_structured_output(UserProfile)
    # response = structured_llm.invoke("Create a user profile for a software engineer skilled in Python and Machine Learning, aged 30, named Alice Smith.")
    # print("Structured Output Response:")
    # print(response)
    # print("Parsed UserProfile Model:")
    # print(type(response))
    # # ---- PromptTemplate ----
    # formatted_prompt = summary_prompt.format(input="LangChain")
    # print("\n--- Using PromptTemplate ---")
    # print(formatted_prompt)

    # response = llm.invoke(formatted_prompt)
    # print("\nLLM Response:")
    # print(response.content)

    # ---- ChatPromptTemplate ----
    # print("\n--- Using ChatPromptTemplate ---")

    # messages = chat_prompt.format_messages(input="Prompt Engineering")
    # for m in messages:
    #     print(m)

    # response = llm.invoke(messages)
    # print("\nLLM Response:")
    # print(response.content)


    # chain = get_basic_chain(provider="groq")
    # result = chain.invoke({"input": "Explain the theory of relativity in simple terms."})
    # print("---- Basic Chain Output ----")
    # print(result)
    # structured_chain = get_structured_chain(provider="groq")
    # result = structured_chain.invoke({"input": "Explain the theory of relativity."})
    # print("---- Structured Chain Output ----")
    # print(result)

    # runnables / LCEL pipelines
    # print("\n--- Basic LCEL ---")
    # chain = basic_lcel_chain()
    # print(chain.invoke({"input": "Explain AI"}))

    # print("\n--- Transformed LCEL ---")
    # chain = transformed_chain()
    # print(chain.invoke({"input": "   Explain GenAI   "}))

    # print("\n--- Parallel LCEL ---")
    # chain = parallel_chain()
    # print(chain.invoke({"input": "LangChain"}))

    # print("\n--- Passthrough LCEL ---")
    # chain = passthrough_chain()
    # print(chain.invoke({"input": "Explain RAG"}))

    #batch chaining test
    # batch = batch_chain(provider="groq")
    # chain = batch_chain(provider="groq")
    # inputs = [
    #     {"input": "What is machine learning in 2 words?"},
    #     {"input": "Define computer in 2 words."},
    # ]
    # print("\n--- Batch Chain Output ---")
    # for inp in inputs:
    #     print(chain.invoke(inp))
    # print("\n--- Streaming Chain Output ---")
    # stream_chain = streaming_chain(provider="groq")
    # response_stream = stream_chain.invoke({"input": "Explain quantum computing."})
    # for chunk in response_stream:
    #     print(chunk, end="", flush=True)

    # print("\n--- Retry LCEL ---")
    # chain = retry_chain() 
    # chain = retry_chain()
    # print(chain.invoke({"input": "Explain RAG"}))

    # Fallback chaining test
    # chain = fallback_chain()
    # print(chain.invoke({"input": "Explain federated learning."}))

    # print("\n--- Conditional LCEL ---")
    # # Conditional chaining test with conditional routing
    # chain = conditional_chain()
    # print(chain.invoke({"input": "Explain Python decorators"}))
    # print(chain.invoke({"input": "Explain AI to a 10 year old"}))

    # print("\n--- Tool Calling Chain ---")
    # chain = tool_calling_chain()
    # print(chain.invoke({"input": "what is 15 plus 27?"}))


    # print("\n--- Basic Agent Execution ---")
    # agent = get_basic_agent()
    # print(run_agent(agent, "What is 15 + 27?"))
# print(agent.invoke({"input": "Tell me current time"}))
    # memory test
    agent = get_basic_agent()
    print(run_agent(agent, "My name is Anil!"))
    print(run_agent(agent, "What is my name?"))
    
if __name__ == "__main__":
    main()
