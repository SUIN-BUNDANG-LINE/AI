from uuid import UUID

from langchain_core.output_parsers import PydanticOutputParser

from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.message_storage import get_message_storage
from app.dto.model.survey import Survey


class AIManager:
    def __init__(self, chat_session_id: UUID):
        self._chat_session_id = str(chat_session_id)

    @staticmethod
    def chat(prompt):
        response = chat_model.invoke(
            [
                HumanMessage(content=prompt),
            ]
        )
        return response.content

    @staticmethod
    async def async_chat(prompt):
        parser = PydanticOutputParser(pydantic_object=Survey)

        response = await chat_model.ainvoke(
            [
                HumanMessage(content=prompt),
                HumanMessage(content=parser.get_format_instructions()),
            ]
        )
        return response.content

    @staticmethod
    def chat_with_parser(prompt, parser):
        response = chat_model.invoke(
            [
                HumanMessage(content=prompt),
                HumanMessage(content=parser.get_format_instructions()),
            ]
        )
        return response.content

    @staticmethod
    async def async_chat_with_parser(prompt, parser):
        response = await chat_model.ainvoke(
            [
                HumanMessage(content=prompt),
                HumanMessage(content=parser.get_format_instructions()),
            ]
        )
        return response.content

    def chat_with_history(self, prompt, is_new_chat_save):
        message_storage = get_message_storage(self._chat_session_id)

        message_history = message_storage.messages

        response = chat_model.invoke(message_history + [HumanMessage(content=prompt)])

        if is_new_chat_save:
            message_storage.add_message(response)

        return response.content

    async def async_chat_with_history(self, prompt, is_new_chat_save):
        message_storage = get_message_storage(self._chat_session_id)

        message_history = message_storage.messages

        response = await chat_model.ainvoke(
            message_history + [HumanMessage(content=prompt)]
        )

        if is_new_chat_save:
            message_storage.clear()
            message_storage.add_message(response)

        return response.content
