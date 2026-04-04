from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.repositories.base_repository import BaseRepository
from app.schemas.resume import ResumeCreate


class ResumeRepository(BaseRepository):

    def __init__(self):
        super().__init__(Resume)

    def create(self, db: Session, user_id: int, data: ResumeCreate):
        resume = Resume(
            user_id=user_id,
            **data.model_dump()
        )

        if hasattr(resume, 'created_by'):
            resume.created_by = user_id

        db.add(resume)
        db.commit()
        db.refresh(resume)
        return resume

    def get_all_by_user(self, db: Session, user_id: int):
        return self.get_query(db).filter(
            Resume.user_id == user_id
        ).all()

    def get_by_id_and_user(self, db: Session, resume_id: int, user_id: int):
        return self.get_query(db).filter(
            Resume.id == resume_id,
            Resume.user_id == user_id
        ).first()