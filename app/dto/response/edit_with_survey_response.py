from typing import Dict, Any
from pydantic import BaseModel


class EditWithSurveyResponse(BaseModel):
    editted_survey_data: Dict[str, Any]
