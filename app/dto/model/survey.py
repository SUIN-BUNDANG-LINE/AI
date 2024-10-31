from typing import Optional
from app.dto.model.section import Section
from pydantic import BaseModel, Field
from uuid import UUID


class Survey(BaseModel):
    id: Optional[UUID] = Field(default=None)
    title: str = Field(default="")
    description: str = Field(default="")
    finish_message: str = Field(default="")
    sections: Optional[list[Section]] = Field(default_factory=list)
    reason: str = Field(default="")
