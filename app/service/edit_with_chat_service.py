from langchain.output_parsers import PydanticOutputParser

from app.core.prompt.edit.edit_question_prompt import edit_question_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_survey_prompt import edit_survey_prompt
from app.core.util.ai_manager import AIManager
from app.core.util.allowed_other_manager import AllowedOtherManager
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.core.util.improve_user_prompt_with_search_chat import (
    chat_improve_user_prompt_with_search,
)
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.response.edit_question_with_chat_response import (
    EditQuestionWithChatResponse,
)
from app.dto.response.edit_section_with_chat_response import EditSectionWithChatResponse
from app.dto.response.edit_total_survey_with_chat_response import (
    EditTotalSurveyWithChatResponse,
)


class EditWithChatService:
    def __init__(self):
        self.edit_survey_prompt = edit_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_total_survey(self, request: EditSurveyWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        parser = PydanticOutputParser(pydantic_object=EditTotalSurveyWithChatResponse)

        edited_total_survey_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "설문 수정 태스크",
                ai_manager.chat_with_history,
                self.edit_survey_prompt.format(
                    user_prompt=chat_improve_user_prompt_with_search(
                        ai_manager=ai_manager, user_prompt=request.user_prompt
                    ),
                    user_survey_data=AllowedOtherManager.add_last_choice_in_survey(
                        request.survey
                    ).model_dump_json(),
                ),
                False,
                parser,
            )
        )

        result = parser.parse(
            edited_total_survey_has_parsing_format.replace('"null"', "null")
        )
        print(result.reason)

        return AllowedOtherManager.remove_last_choice_in_survey(result)

    def edit_section(self, request: EditSectionWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        parser = PydanticOutputParser(pydantic_object=EditSectionWithChatResponse)
        edited_section_has_parsing_format = FunctionExecutionTimeMeasurer.run_function(
            "섹션 수정 태스크",
            ai_manager.chat_with_history,
            self.edit_section_prompt.format(
                user_prompt=chat_improve_user_prompt_with_search(
                    ai_manager=ai_manager, user_prompt=request.user_prompt
                ),
                user_survey_data=AllowedOtherManager.add_last_choice_in_section(
                    request.section
                ).model_dump_json(),
            ),
            False,
            parser,
        )

        result = parser.parse(
            edited_section_has_parsing_format.replace('"null"', "null")
        )
        print(result.reason)

        return AllowedOtherManager.remove_last_choice_in_section(result)

    def edit_question(self, request: EditQuestionWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        parser = PydanticOutputParser(pydantic_object=EditQuestionWithChatResponse)
        edited_question_has_parsing_format = FunctionExecutionTimeMeasurer.run_function(
            "질문 수정 태스크",
            ai_manager.chat_with_history,
            self.edit_question_prompt.format(
                user_prompt=chat_improve_user_prompt_with_search(
                    ai_manager=ai_manager, user_prompt=request.user_prompt
                ),
                user_survey_data=AllowedOtherManager.add_last_choice_in_question(
                    request.question
                ).model_dump_json(),
            ),
            False,
            parser,
        )

        result = parser.parse(
            edited_question_has_parsing_format.replace('"null"', "null")
        )
        print(result.reason)

        return AllowedOtherManager.remove_last_choice_in_question(result)
