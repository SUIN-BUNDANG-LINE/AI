from uuid import UUID
from app.core.config.vector_storage import vector_storage
from app.core.error.business_exception import business_exception
from app.core.error.error_code import ErrorCode
from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.message_storage import get_message_storage
from app.core.config.text_splitter import text_splitter


class AIManager:
    def __init__(self, chat_session_id: UUID):
        self._chat_session_id = (
            str(chat_session_id) if chat_session_id is not None else None
        )

    async def async_embed_document(self, document):
        self.__check_chat_session_id_exist()
        metadatas = {"id": self._chat_session_id}
        splitted_documents = text_splitter.create_documents([document], [metadatas])
        await vector_storage.aadd_documents(splitted_documents)

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
        self.__check_chat_session_id_exist()
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
        self.__check_chat_session_id_exist()
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

    def chat_with_similarity_search(self, prompt, parser=None):
        self.__check_chat_session_id_exist()
        documents = vector_storage.similarity_search(
            query=prompt, filter={"id": self._chat_session_id}, k=3
        )
        documents_string = " ".join([doc.page_content for doc in documents])

        human_messages = [documents_string] + [HumanMessage(content=prompt)]

        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = chat_model.invoke(human_messages)

        return response.content

    async def async_chat_with_similarity_search(self, prompt, parser=None):
        self.__check_chat_session_id_exist()
        documents = await vector_storage.asimilarity_search(
            query=prompt, filter={"id": self._chat_session_id}, k=3
        )
        documents_string = " ".join([doc.page_content for doc in documents])

        human_messages = [documents_string] + [HumanMessage(content=prompt)]

        if parser:
            human_messages += [HumanMessage(content=parser.get_format_instructions())]

        response = await chat_model.ainvoke(human_messages)

        return response.content

    def __check_chat_session_id_exist(self):
        if self._chat_session_id is None:
            raise business_exception(ErrorCode.CHAT_SESSION_ID_NOT_EXIST)
