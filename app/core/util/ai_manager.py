from app.core.config.ai_model import chat_model
from langchain.schema import HumanMessage
from app.core.config.chat_memorization import get_message_histroy
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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

    def chat_with_memory(self, formatted_prompt, session_id):

        prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "#Question:\n{question}"),
            ]
        )

        chain = prompt | chat_model

        user_input = {"question": formatted_prompt}
        config = {"configurable": {"session_id": session_id}}
        
        chain_with_history = RunnableWithMessageHistory(
            chain,
            get_message_histroy,
            input_messages_key="question", 
            history_messages_key="chat_history",
        )

        return chain_with_history.invoke(user_input, config = config)