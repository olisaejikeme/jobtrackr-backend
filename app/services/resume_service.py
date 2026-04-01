from sqlalchemy.orm import Session
from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume import ResumeCreate


class ResumeService:

    def __init__(self):
        self.repo = ResumeRepository()

    def create_resume(self, db: Session, user_id: int, data: ResumeCreate):
        return self.repo.create(db, user_id, data)

    def get_resumes(self, db: Session, user_id: int):
        return self.repo.get_all(db, user_id)

    def delete_resume(self, db: Session, resume_id: int, user_id: int):
        resumes = self.repo.get_all(db, user_id)

        resume = next((r for r in resumes if r.id == resume_id), None)

        if not resume:
            raise Exception("Resume not found")

        self.repo.delete(db, resume)