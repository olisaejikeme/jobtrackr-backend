from fastapi import APIRouter, Depends
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
    payload: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.create_application(db, current_user.id, payload)
    return ResponseUtils.ok("Application created successfully", data)

@router.get("", response_model=ResponseSchema[List[ApplicationResponse]])
def get_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    data = service.get_applications(db, current_user.id)
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