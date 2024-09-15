from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

chat = ChatOpenAI(
    model="gpt-4o-mini",
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)