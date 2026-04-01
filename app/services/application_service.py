from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationService:

    def __init__(self):
        self.repo = ApplicationRepository()

    def create_application(self, db: Session, user_id: int, data: ApplicationCreate):
        return self.repo.create(db, user_id, data)

    def get_applications(self, db: Session, user_id: int):
        return self.repo.get_all(db, user_id)

    def get_application(self, db: Session, application_id: int, user_id: int):
        application = self.repo.get_by_id(db, application_id, user_id)

        if not application:
            raise Exception("Application not found")

        return application

    def update_application(
        self,
        db: Session,
        application_id: int,
        user_id: int,
        data: ApplicationUpdate
    ):
        application = self.repo.get_by_id(db, application_id, user_id)

        if not application:
            raise Exception("Application not found")

        return self.repo.update(db, application, data)

    def delete_application(self, db: Session, application_id: int, user_id: int):
        application = self.repo.get_by_id(db, application_id, user_id)

        if not application:
            raise Exception("Application not found")

        self.repo.delete(db, application)