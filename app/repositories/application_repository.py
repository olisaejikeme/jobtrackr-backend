from sqlalchemy.orm import Session
from app.models.application import Application
from app.repositories.base_repository import BaseRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationRepository(BaseRepository):

    def __init__(self):
        super().__init__(Application)

    def create(self, db: Session, user_id: int, data: ApplicationCreate):
        application = Application(
            user_id=user_id,
            **data.model_dump()
        )
        application.created_by = user_id

        db.add(application)
        db.commit()
        db.refresh(application)
        return application

    def get_all_by_user(self, db: Session, user_id: int):
        return self.get_query(db).filter(
            Application.user_id == user_id
        ).all()

    def get_by_id_and_user(self, db: Session, application_id: int, user_id: int):
        return self.get_query(db).filter(
            Application.id == application_id,
            Application.user_id == user_id
        ).first()

    def update(self, db: Session, user_id: int, application: Application, data: ApplicationUpdate):
        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(application, key, value)

        application.modified_by = user_id

        db.commit()
        db.refresh(application)
        return application