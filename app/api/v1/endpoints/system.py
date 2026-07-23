from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SystemInfo(BaseModel):
    cpu: str
    ram: str
    disk: str
    uptime: str

@router.get("/info")
def get_system_info():
    return SystemInfo(
        cpu="0%",
        ram="0/0 MB",
        disk="0/0 GB",
        uptime="0 days"
    )

@router.get("/metrics")
def get_metrics():
    return {"cpu": 0.0, "ram": 0.0, "disk": 0.0}
