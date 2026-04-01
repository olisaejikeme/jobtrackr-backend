from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.repositories.resume_repository import ResumeRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationService:

    def __init__(self):
        self.repo = ApplicationRepository()
        self.resume_repo = ResumeRepository()

    def create_application(self, db: Session, user_id: int, data: ApplicationCreate):

        if data.resume_id is not None:
            resume = self.resume_repo.get_by_id_and_user(db, data.resume_id, user_id)

            if not resume:
                raise HTTPException(status_code=404, detail="Resume not found")

        return self.repo.create(db, user_id, data)

    def get_applications(self, db: Session, user_id: int):
        return self.repo.get_all_by_user(db, user_id)

    def get_application(self, db: Session, application_id: int, user_id: int):
        application = self.repo.get_by_id_and_user(db, application_id, user_id)

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        return application

    def update_application(self, db: Session, application_id: int, user_id: int, data: ApplicationUpdate):
        application = self.repo.get_by_id_and_user(db, application_id, user_id)

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        return self.repo.update(db, user_id, application, data)

    def delete_application(self, db: Session, application_id: int, user_id: int):
        application = self.repo.get_by_id_and_user(db, application_id, user_id)

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        self.repo.soft_delete(db, application)