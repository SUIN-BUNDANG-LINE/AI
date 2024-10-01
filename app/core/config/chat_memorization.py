import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")


def get_message_storage(session_id: str):
    message_storage = RedisChatMessageHistory(
        session_id,
        url="redis://default:password@localhost:6379/0",
        ttl=60 * 60)

    return message_storage
