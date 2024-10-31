import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini", temperature=0.2)
