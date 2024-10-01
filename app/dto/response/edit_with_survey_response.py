from typing import Dict, Any
from pydantic import BaseModel


class EditWithSurveyResponse(BaseModel):
    edittedSurveyData: Dict[str, Any]
