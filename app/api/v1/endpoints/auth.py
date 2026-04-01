from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response_schema import ResponseSchema
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.api.deps import get_db
from app.utils.response_utils import ResponseUtils

router = APIRouter()
service = AuthService()

@router.post("/register", response_model=ResponseSchema[UserResponse])
def register(data: UserCreate, db: Session = Depends(get_db)):
    return ResponseUtils.ok("User registered successfully",service.register(db, data))


@router.post("/login", response_model=ResponseSchema[TokenResponse])
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = service.login(db, data)
    data = TokenResponse(access_token=token)
    return ResponseUtils.ok("User logged in successfully", data)