from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ServerStatus(BaseModel):
    name: str
    status: str
    players: int

@router.get("/status")
def get_status():
    return ServerStatus(name="AstralisZomboid", status="stopped", players=0)

@router.post("/start")
def start_server():
    return {"message": "Server started"}

@router.post("/stop")
def stop_server():
    return {"message": "Server stopped"}
