from langchain.vectorstores import Chroma
from app.core.config.ai_model import embedding_model

vector_storage = Chroma(persist_directory="./.data", embedding_function=embedding_model)
