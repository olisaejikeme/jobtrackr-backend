from pydantic import BaseModel
from datetime import datetime

from app.schemas.base_schema import ORMBaseModel


class ResumeBase(BaseModel):
    file_name: str
    file_path: str
    version_label: str | None = None


class ResumeCreate(ResumeBase):
    pass


class ResumeResponse(ORMBaseModel):
    id: int
    file_name: str
    file_path: str
    uploaded_at: datetime