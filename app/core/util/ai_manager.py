from app.core.config.ai import chat
from langchain.schema import HumanMessage

class AIManager:
    def chat(self, prompt):
        response =chat([
            HumanMessage(content=prompt)
        ])
        return response.content