from uuid import UUID

from langchain_core.output_parsers import PydanticOutputParser

from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.message_storage import get_message_storage


class AIManager:
    def __init__(self, chat_session_id: UUID):
        self._chat_session_id = str(chat_session_id)

    @staticmethod
    def chat(prompt, parser=None):
        human_messages = [HumanMessage(content=prompt)]
        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = chat_model.invoke(human_messages)
        return response.content

    @staticmethod
    async def async_chat(prompt, parser=None):
        human_messages = [HumanMessage(content=prompt)]
        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = await chat_model.ainvoke(human_messages)
        return response.content

    def chat_with_history(self, prompt, is_new_chat_save, parser=None):
        message_storage = get_message_storage(self._chat_session_id)
        message_history = message_storage.messages

        human_messages = message_history + [HumanMessage(content=prompt)]

        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = chat_model.invoke(human_messages)

        if is_new_chat_save:
            message_storage.add_message(response)

        return response.content

    async def async_chat_with_history(self, prompt, is_new_chat_save, parser=None):
        message_storage = get_message_storage(self._chat_session_id)
        message_history = message_storage.messages

        human_messages = message_history + [HumanMessage(content=prompt)]

        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = await chat_model.ainvoke(human_messages)

        if is_new_chat_save:
            message_storage.clear()
            message_storage.add_message(response)

        return response.content
