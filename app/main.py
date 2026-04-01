from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "JobTrackr API is running"}