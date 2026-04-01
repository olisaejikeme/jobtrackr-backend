from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume import ResumeCreate


class ResumeService:

    def __init__(self):
        self.repo = ResumeRepository()

    def create_resume(self, db: Session, user_id: int, data: ResumeCreate):
        return self.repo.create(db, user_id, data)

    def get_resumes(self, db: Session, user_id: int):
        return self.repo.get_all_by_user(db, user_id)

    def delete_resume(self, db: Session, resume_id: int, user_id: int):
        resume = self.repo.get_by_id_and_user(db, resume_id, user_id)

        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        self.repo.soft_delete(db, resume)