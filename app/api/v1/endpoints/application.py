from datetime import date

from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, get_current_user
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationUpdate
)
from app.schemas.response_schema import ResponseSchema
from app.services.application_service import ApplicationService
from app.models.user import User
from app.utils.response_utils import ResponseUtils

router = APIRouter()
service = ApplicationService()

@router.post("", response_model=ResponseSchema[ApplicationResponse])
def create_application(
    company_name: str = Form(...),
    job_title: str = Form(...),
    status: str = Form(...),
    location: str = Form(None),
    application_date: date = Form(None),
    job_link: str = Form(None),
    job_description: str = Form(None),
    resume_id: int = Form(None),
    notes: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    payload = ApplicationCreate(
        company_name=company_name,
        job_title=job_title,
        status=status,
        location=location,
        application_date=application_date,
        job_link=job_link,
        job_description=job_description,
        resume_id=resume_id,
        notes=notes
    )

    data = service.create_application(db, current_user.id, payload, file)
    return ResponseUtils.ok("Application created successfully", data)

@router.get("", response_model=ResponseSchema[List[ApplicationResponse]])
def get_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.get_applications(db, current_user.id)
    return ResponseUtils.ok("Applications fetched successfully", data)

@router.get("/{application_id}", response_model=ResponseSchema[ApplicationResponse])
def get_application_by_id(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.get_application(db, application_id, current_user.id)
    return ResponseUtils.ok("Application fetched successfully", data)

@router.put("/{application_id}", response_model=ResponseSchema[ApplicationResponse])
def update_application(
    application_id: int,
    data: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.update_application(
        db,
        application_id,
        current_user.id,
        data
    )
    return ResponseUtils.ok("Application updated successfully", data)

@router.delete("/{application_id}", status_code=204)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service.delete_application(db, application_id, current_user.id)

@router.patch("/{application_id}/status", response_model=ResponseSchema[ApplicationResponse])
def update_application_status(
    application_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.update_status(db, application_id, current_user.id, status)
    return ResponseUtils.ok("Status updated successfully", data)