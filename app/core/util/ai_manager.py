from app.core.config.ai import chat
from langchain.schema import HumanMessage

class AIManager:
    def chat(self, prompt):
        response = chat.invoke([
            HumanMessage(content=prompt),
        ])
        return response.content

    def chat_with_parser(self, prompt, parser):
        response =chat.invoke([
            HumanMessage(content=prompt),
            HumanMessage(content=parser.get_format_instructions())
        ])
        return response.content