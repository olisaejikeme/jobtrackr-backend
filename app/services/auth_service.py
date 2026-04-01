from sqlalchemy.orm import Session

from app.enums.user_status import UserStatus
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
            raise Exception("Email already registered")

        password_hash = hash_password(data.password)

        user = self.repo.create(
            db,
            name=data.name,
            email=str(data.email),
            password_hash=password_hash
        )

        return user

    def login(self, db: Session, data: LoginRequest):
        user = self.repo.get_by_email(db, str(data.email))

        if not user:
            raise Exception("Invalid credentials")

        if not verify_password(data.password, user.password_hash):
            raise Exception("Invalid credentials")

        token = create_access_token({"sub": str(user.id)})

        return token