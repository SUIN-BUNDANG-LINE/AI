from pydantic import BaseModel
from sympy import Array

class Who(BaseModel):
    age: int
    gender: str
    job: str
    
    def to_string(self):
        return f"{self.age}살 {self.gender} {self.job}"

class SurveyGenerateRequest(BaseModel):
    who: Who
    group_name: str
    file_url : str