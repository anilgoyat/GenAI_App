from langchain_core.messages import SystemMessage
from .memory_reader import retrieve_memories
from .memory_writer import extract_and_store_memory

def memory_node(state):
    messages = state["messages"]
    user_input = messages[-1].content

    # 1. Retrieve old memories
    memories = retrieve_memories(user_input)

    # 2. Inject memory into context
    if memories:
        memory_text = "\n".join(memories)
        messages.insert(
            0,
            SystemMessage(content=f"Known user facts:\n{memory_text}")
        )

    # 3. Store new memory
    extract_and_store_memory(user_input)

    return {"messages": messages}
