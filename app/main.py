from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="Astralis API",
    description="RESTful API for server and game management",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Astralis API", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}
