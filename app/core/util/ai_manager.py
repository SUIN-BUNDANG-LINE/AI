import uuid
from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.message_storage import get_message_storage


class AIManager:
    def __init__(self):
        self._session_id = str(uuid.uuid4())

    @property
    def session_id(self):
        return self._session_id

    def chat(self, prompt):
        response = chat_model.invoke(
            [
                HumanMessage(content=prompt),
            ]
        )
        return response.content

    def chat_with_parser(self, prompt, parser):
        response = chat_model.invoke(
            [
                HumanMessage(content=prompt),
                HumanMessage(content=parser.get_format_instructions()),
            ]
        )
        return response.content

    def chat_with_history(self, prompt, session_id, is_new_chat_save):
        message_storage = get_message_storage(str(session_id))

        message_history = message_storage.messages

        response = chat_model.invoke(message_history + [HumanMessage(content=prompt)])

        if is_new_chat_save:
            message_storage.add_message(response)

        return response.content

    async def async_chat(self, prompt):
        response = await chat_model.ainvoke(
            [
                HumanMessage(content=prompt),
            ]
        )
        return response.content

    async def async_chat_with_history(self, prompt, session_id, is_new_chat_save):
        message_storage = get_message_storage(session_id)

        message_history = message_storage.messages

        response = await chat_model.ainvoke(
            message_history + [HumanMessage(content=prompt)]
        )

        if is_new_chat_save:
            message_storage.add_message(response)

        return response.content

    async def async_chat_with_parser(self, prompt, parser):
        response = await chat_model.ainvoke(
            [
                HumanMessage(content=prompt),
                HumanMessage(content=parser.get_format_instructions()),
            ]
        )
        return response.content
