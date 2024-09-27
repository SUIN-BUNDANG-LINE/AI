from concurrent.futures import thread
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType

class EditWitchChatRequest(BaseModel):
    thread_id: str
    survey_data: any
    survey_data_type: SurveyDataType
    user_prompt: str