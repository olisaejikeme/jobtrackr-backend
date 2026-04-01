from pydantic import BaseModel, EmailStr

from app.schemas.base_schema import ORMBaseModel


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel, ORMBaseModel):
    id: int
    name: str
    email: EmailStr