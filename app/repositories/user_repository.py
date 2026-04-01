from sqlalchemy.orm import Session

from app.enums.user_status import UserStatus
from app.models.user import User


class UserRepository:

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, name: str, email: str, password_hash: str):
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            status=UserStatus.ACTIVE
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user