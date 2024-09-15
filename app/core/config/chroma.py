from config.ai import embeddings
from langchain.vectorstores import Chroma

database = Chroma(
    embedding_function=embeddings
)