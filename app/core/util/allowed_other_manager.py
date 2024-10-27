from app.dto.model.question import Question
from app.dto.model.section import Section
from app.dto.model.survey import Survey


class AllowedOtherManager:
    @staticmethod
    def remove_last_choice_in_survey(survey: Survey):
        if hasattr(survey, "reason"):
            del survey.reason
        for section in survey.sections:
            if section.questions:
                for question in section.questions:
                    if question.is_allow_other and question.choices:
                        question.choices.pop()
        return survey

    @staticmethod
    def remove_last_choice_in_section(section: Section):
        if hasattr(section, "reason"):
            del section.reason
        if section.questions:
            for question in section.questions:
                if question.is_allow_other and question.choices:
                    question.choices.pop()
        return section

    @staticmethod
    def remove_last_choice_in_question(question: Question):
        if hasattr(question, "reason"):
            del question.reason
        if question.choices:
            if question.is_allow_other and question.choices:
                question.choices.pop()
        return question

    @staticmethod
    def add_last_choice_in_survey(survey: Survey):
        for section in survey.sections:
            if section.questions:
                for question in section.questions:
                    if question.is_allow_other and question.choices:
                        question.choices.append("기타")
        return survey

    @staticmethod
    def add_last_choice_in_section(section: Section):
        if section.questions:
            for question in section.questions:
                if question.is_allow_other and question.choices:
                    question.choices.append("기타")
        return section

    @staticmethod
    def add_last_choice_in_question(question: Question):
        if question.choices:
            if question.is_allow_other and question.choices:
                question.choices.append("기타")
        return question
