import cloudinary.uploader

from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session
from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume import ResumeCreate


class ResumeService:

    def __init__(self):
        self.repo = ResumeRepository()

    async def handle_upload(self, db: Session, user_id: int, file: UploadFile, display_name: str = None):
        # Validate File Extension
        allowed_extensions = ["pdf", "docx", "doc"]
        extension = file.filename.split(".")[-1].lower()
        if extension not in allowed_extensions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported file type .{extension}. Only PDF and DOCX are allowed."
            )

        # Validate File Size (5MB limit)
        file.file.seek(0, 2)
        size = file.file.tell()
        file.file.seek(0)
        if size > 5 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File too large (Max 5MB)")

        # Upload to Cloudinary
        try:
            upload_result = cloudinary.uploader.upload(
                file.file,
                folder=f"jobtrackr/resumes/{user_id}",
                resource_type="raw"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Cloudinary upload failed: {str(e)}")

        # 4. Prepare Pydantic Model (Fixes the 'dict' AttributeError)
        resume_payload = ResumeCreate(
            file_name=display_name if display_name else file.filename,
            file_path=upload_result['secure_url'],
            version_label="v1"
        )

        return self.repo.create(db, user_id, resume_payload)

    def get_resumes(self, db: Session, user_id: int):
        return self.repo.get_all_by_user(db, user_id)

    def delete_resume(self, db: Session, resume_id: int, user_id: int):
        resume = self.repo.get_by_id_and_user(db, resume_id, user_id)

        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        self.repo.soft_delete(db, resume)