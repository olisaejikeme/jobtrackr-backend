from fastapi import APIRouter

from app.api.v1.endpoints import auth, application, resume

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(application.router,prefix="/applications",tags=["Applications"])
api_router.include_router(resume.router,prefix="/resumes",tags=["Resumes"])