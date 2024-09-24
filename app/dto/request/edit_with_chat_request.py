from pydantic import BaseModel

class EditWitchChatRequest(BaseModel):
    survey_data: any
    diff: any
    user_prompt : str