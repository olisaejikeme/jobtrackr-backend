from sqlalchemy.orm import Session
from app.models.resume import Resume
from app.schemas.resume import ResumeCreate


class ResumeRepository:

    def create(self, db: Session, user_id: int, data: ResumeCreate):
        resume = Resume(
            user_id=user_id,
            **data.model_dump()
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)
        return resume

    def get_all(self, db: Session, user_id: int):
        return db.query(Resume).filter(Resume.user_id == user_id).all()

    def delete(self, db: Session, resume: Resume):
        db.delete(resume)
        db.commit()