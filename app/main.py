from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from app.api.v1.endpoints.router import api_router
from app.core.cors import configure_cors
from app.core.openapi import custom_openapi
from app.exceptions.http_exceptions import http_exception_handler
from configs.settings import settings
from scripts.seed import seed

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Seed the database
    if settings.environment == "development":
        seed()
    yield
    pass

app = FastAPI(lifespan=lifespan)

configure_cors(app)
app.openapi = custom_openapi(app)
app.add_exception_handler(HTTPException, http_exception_handler)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "JobTrackr API is running"}