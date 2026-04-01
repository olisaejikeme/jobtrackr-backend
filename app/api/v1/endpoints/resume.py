from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, get_current_user
from app.schemas.response_schema import ResponseSchema
from app.schemas.resume import ResumeCreate, ResumeResponse
from app.services.resume_service import ResumeService
from app.models.user import User
from app.utils.response_utils import ResponseUtils

router = APIRouter()
service = ResumeService()

@router.post("", response_model=ResponseSchema[ResumeResponse])
def create_resume(
    payload: ResumeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.create_resume(db, current_user.id, payload)
    return ResponseUtils.ok("Resume uploaded successfully", data)

@router.get("", response_model=ResponseSchema[List[ResumeResponse]])
def get_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.get_resumes(db, current_user.id)
    return ResponseUtils.ok("Resumes fetched successfully", data)

@router.delete("/{resume_id}", status_code=204)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service.delete_resume(db, resume_id, current_user.id)