from langchain_community.chat_message_histories import RedisChatMessageHistory

def get_message_storage(session_id: str):
    message_storage = RedisChatMessageHistory(
        session_id,
        url="redis://localhost:6379/0"
    )

    return message_storage