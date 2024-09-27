from app.core.config.ai_model import embedding_model
from langchain.vectorstores import Chroma

chroma = Chroma(
    embedding_function=embedding_model
)