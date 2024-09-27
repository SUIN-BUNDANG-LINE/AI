from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain.memory import ConversationBufferWindowMemory

def get_message_histroy(thread_id):
    history = RedisChatMessageHistory(
        session_id=thread_id,
        url="redis://localhost:6379/0"
    )

    # memory = ConversationBufferWindowMemory(
    #     return_messages=True,
    #     k=3,
    #     history=history
    # )

    return history