from datetime import date

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.repositories.resume_repository import ResumeRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate
from app.schemas.resume import ResumeCreate


class ApplicationService:

    def __init__(self):
        self.repo = ApplicationRepository()
        self.resume_repo = ResumeRepository()

    def create_application(self, db: Session, user_id: int, data: ApplicationCreate, file: UploadFile = None):
        # Scenario A: User uploaded a new file
        if file:
            # Ensure we are at the start of the file
            file.file.seek(0)

            # Validate File Extension
            allowed_extensions = ["pdf", "docx", "doc"]
            extension = file.filename.split(".")[-1].lower()

            if extension not in allowed_extensions:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Unsupported file type .{extension}. Only PDF and DOCX are allowed."
                )

            # Optional: Validate File Size (e.g., 5MB limit)
            file.file.seek(0, 2) # move to end
            size = file.file.tell() # get size
            file.file.seek(0) # reset
            if size > 5 * 1024 * 1024:
                raise HTTPException(status_code=400, detail="File too large")

            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(
                file.file,
                folder="resumes",
                resource_type="raw"
            )

            resume_payload = ResumeCreate(
                file_name=file.filename,
                file_path=upload_result['secure_url'],
                version_label="v1"
            )

            # Create the Resume record
            new_resume = self.resume_repo.create(db, user_id, resume_payload)

            # Set the resume_id for the application
            data.resume_id = new_resume.id

        # Scenario B: User selected an existing resume
        elif data.resume_id is not None:
            resume = self.resume_repo.get_by_id_and_user(db, data.resume_id, user_id)
            if not resume:
                raise HTTPException(status_code=404, detail="Resume not found")

        if not data.application_date:
            data.application_date = date.today()

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

    def update_status(self, db: Session, application_id: int, user_id: int, new_status: str):
        application = self.repo.get_by_id_and_user(db, application_id, user_id)

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        from app.schemas.application import ApplicationUpdate
        update_data = ApplicationUpdate(status=new_status)

        return self.repo.update(db, user_id, application, update_data)