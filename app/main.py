from fastapi import FastAPI, HTTPException

from app.api.v1.endpoints.router import api_router
from app.core.cors import configure_cors
from app.core.openapi import custom_openapi
from app.exceptions.http_exceptions import http_exception_handler

app = FastAPI()
configure_cors(app)
app.openapi = custom_openapi(app)
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "JobTrackr API is running"}