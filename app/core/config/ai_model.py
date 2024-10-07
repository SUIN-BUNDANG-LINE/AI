import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-4o-mini",
    temperature=0,
)

embedding_model = OpenAIEmbeddings(
    api_key=openai_api_key, model="text-embedding-3-large"
)
