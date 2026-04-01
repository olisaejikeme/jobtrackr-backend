from datetime import date

from pydantic import BaseModel

from app.schemas.base_schema import ORMBaseModel


# Base (shared fields)
class ApplicationBase(BaseModel):
    company_name: str
    job_title: str
    location: str | None = None
    status: str
    application_date: date | None = None
    job_link: str | None = None
    job_description: str | None = None
    resume_id: int | None = None
    notes: str | None = None

# Create (incoming request)
class ApplicationCreate(ApplicationBase):
    pass

# Update (partial updates)
class ApplicationUpdate(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    location: str | None = None
    status: str | None = None
    application_date: date | None = None
    job_link: str | None = None
    job_description: str | None = None
    resume_id: int | None = None
    notes: str | None = None

# Response (outgoing)
class ApplicationResponse(ORMBaseModel):
    id: int