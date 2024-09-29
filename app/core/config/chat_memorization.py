from langchain_community.chat_message_histories import RedisChatMessageHistory

def get_message_histroy(thread_id):
    history = RedisChatMessageHistory(
        session_id=thread_id,
        url="redis://localhost:6379/0"
    )

    return history