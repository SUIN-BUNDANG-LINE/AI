from app.core.config.ai import chat
from langchain.schema import HumanMessage

class AIManager:
    def chat(self, prompt):
        response =chat([
            HumanMessage(content=prompt),
        ])
        return response.content

    def chat_with_parser(self, prompt, parser):
        response =chat([
            HumanMessage(content=prompt),
            HumanMessage(content=parser.get_format_instructions())
        ])
        return response.content