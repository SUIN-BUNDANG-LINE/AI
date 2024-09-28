from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.chat_memorization import get_message_histroy
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser

class AIManager:
    def chat(self, prompt):
        response = chat_model.invoke([
            HumanMessage(content=prompt),
        ])
        return response.content

    def chat_with_parser(self, prompt, parser):
        response =chat_model.invoke([
            HumanMessage(content=prompt),
            HumanMessage(content=parser.get_format_instructions())
        ])
        return response.content

    def chat_with_memory(self, prompt, session_id):
        chain = RunnableParallel({"content":chat_model})
        
        chain_with_history = RunnableWithMessageHistory(
            chain,
            get_message_histroy,
        )

        response = chain_with_history.invoke(
            [HumanMessage(content=prompt)],
            config = {"configurable": {"session_id": session_id}}
        )

        return response