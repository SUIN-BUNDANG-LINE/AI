from app.core.config.ai import embeddings
from langchain.vectorstores import Chroma

chroma = Chroma(
    embedding_function=embeddings
)