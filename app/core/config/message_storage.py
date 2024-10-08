import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")
REDIS_TTL = os.getenv("REDIS_TTL")


def get_message_storage(session_id: str):
    message_storage = RedisChatMessageHistory(session_id, url=REDIS_URL, ttl=REDIS_TTL)

    return message_storage
