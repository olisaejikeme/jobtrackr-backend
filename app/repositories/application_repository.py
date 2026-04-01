from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationRepository:

    def create(self, db: Session, user_id: int, data: ApplicationCreate):
        application = Application(
            user_id=user_id,
            **data.model_dump()
        )

        db.add(application)
        db.commit()
        db.refresh(application)
        return application

    def get_all(self, db: Session, user_id: int):
        return db.query(Application).filter(Application.user_id == user_id).all()

    def get_by_id(self, db: Session, application_id: int, user_id: int):
        return db.query(Application).filter(
            Application.id == application_id,
            Application.user_id == user_id
        ).first()

    def update(self, db: Session, application: Application, data: ApplicationUpdate):
        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(application, key, value)

        db.commit()
        db.refresh(application)
        return application

    def delete(self, db: Session, application: Application):
        db.delete(application)
        db.commit()