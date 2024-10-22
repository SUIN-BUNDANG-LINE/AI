from app.dto.model.question import Question
from app.dto.model.section import Section
from app.dto.model.survey import Survey
from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from app.core.util.ai_manager import AIManager
from app.dto.response.edit_total_survey_with_chat_response import (
    EditTotalSurveyWithChatResponse,
)
from app.dto.response.edit_section_with_chat_response import EditSectionWithChatResponse
from app.dto.response.edit_question_with_chat_response import (
    EditQuestionWithChatResponse,
)
from langchain.output_parsers import PydanticOutputParser

from app.core.prompt.edit.edit_survey_prompt import edit_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt
from app.core.prompt.prompt_resolve_prompt import prompt_resolve_prompt
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer


def remove_last_choice_if_allowed_other_in_survey(survey: Survey):
    for section in survey.sections:
        for question in section.questions:
            if question.is_allow_other and question.choices:
                question.choices.pop()

    return survey


def remove_last_choice_if_allowed_other_in_section(section: Section):
    for question in section.questions:
        if question.is_allow_other and question.choices:
            question.choices.pop()

    return section


def remove_last_choice_if_allowed_other_in_question(question: Question):
    if question.is_allow_other and question.choices:
        question.choices.pop()

    return question


class EditWithChatService:
    def __init__(self):
        self.edit_survey_prompt = edit_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_total_survey(self, request: EditSurveyWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        print(request.user_prompt)

        user_prompt = FunctionExecutionTimeMeasurer.run_function(
            "사용자 프롬프트 명확화 태스크",
            ai_manager.chat,
            prompt_resolve_prompt.format(user_prompt=request.user_prompt),
        )

        parser = PydanticOutputParser(pydantic_object=EditTotalSurveyWithChatResponse)
        edited_total_survey_has_parsing_format = (
            FunctionExecutionTimeMeasurer.run_function(
                "설문 수정 태스크",
                ai_manager.chat_with_history,
                self.edit_survey_prompt.format(
                    user_prompt=user_prompt,
                    user_survey_data=request.survey.model_dump_json(),
                ),
                False,
                parser,
            )
        )

        return remove_last_choice_if_allowed_other_in_survey(
            parser.parse(edited_total_survey_has_parsing_format)
        )

    def edit_section(self, request: EditSectionWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        user_prompt = FunctionExecutionTimeMeasurer.run_function(
            "사용자 프롬프트 명확화 태스크",
            ai_manager.chat,
            prompt_resolve_prompt.format(user_prompt=request.user_prompt),
        )

        parser = PydanticOutputParser(pydantic_object=EditSectionWithChatResponse)
        edited_section_has_parsing_format = FunctionExecutionTimeMeasurer.run_function(
            "섹션 수정 태스크",
            ai_manager.chat_with_history,
            self.edit_survey_prompt.format(
                user_prompt=user_prompt,
                user_survey_data=request.section.model_dump_json(),
            ),
            False,
            parser,
        )

        return remove_last_choice_if_allowed_other_in_section(
            parser.parse(edited_section_has_parsing_format)
        )

    def edit_question(self, request: EditQuestionWithChatRequest):
        ai_manager = AIManager(request.chat_session_id)

        user_prompt = FunctionExecutionTimeMeasurer.run_function(
            "사용자 프롬프트 명확화 태스크",
            ai_manager.chat,
            prompt_resolve_prompt.format(user_prompt=request.user_prompt),
        )

        parser = PydanticOutputParser(pydantic_object=EditQuestionWithChatResponse)
        edited_question_has_parsing_format = FunctionExecutionTimeMeasurer.run_function(
            "질문 수정 태스크",
            ai_manager.chat_with_history,
            self.edit_survey_prompt.format(
                user_prompt=user_prompt,
                user_survey_data=request.question.model_dump_json(),
            ),
            False,
            parser,
        )

        return remove_last_choice_if_allowed_other_in_question(
            parser.parse(edited_question_has_parsing_format)
        )
