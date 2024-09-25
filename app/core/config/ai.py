import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-4o-mini",
    temperature=0,
)

embeddings = OpenAIEmbeddings(
    api_key=openai_api_key,
    model="text-embedding-3-large"
)