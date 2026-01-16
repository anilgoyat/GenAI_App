from langchain_community.memory import ConversationBufferMemory

def get_basic_memory():
    return ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )