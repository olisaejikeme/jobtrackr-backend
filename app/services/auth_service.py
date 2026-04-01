from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models import Role
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.schemas.auth import LoginRequest
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    def register(self, db: Session, data: UserCreate):
        existing_user = self.repo.get_by_email(db, str(data.email))

        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

        user_role = db.query(Role).filter(Role.name == "USER").first()

        if not user_role:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Default role not found")

        password_hash = hash_password(data.password)

        role_id = user_role.id

        user = self.repo.create(
            db,
            name=data.name,
            email=str(data.email),
            password_hash=password_hash,
            role_id=role_id # type: ignore
        )

        return user

    def login(self, db: Session, data: LoginRequest):
        user = self.repo.get_by_email(db, str(data.email))

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

        if not verify_password(data.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

        token = create_access_token({"sub": str(user.id)})

        return token