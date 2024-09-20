from enum import Enum

class QuestionType(Enum):
    TEXT_RESPONSE = "TEXT_RESPONSE"
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"