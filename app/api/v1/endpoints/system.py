from fastapi import APIRouter
from pydantic import BaseModel
import psutil
import time
from typing import Dict

router = APIRouter()

class SystemInfo(BaseModel):
    cpu_percent: float
    cpu_count: int
    memory_percent: float
    memory_total: float
    memory_used: float
    disk_percent: float
    disk_total: float
    disk_used: float
    uptime_days: int
    uptime_hours: int

@router.get("/info", response_model=SystemInfo)
def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_days = int(uptime_seconds // 86400)
    uptime_hours = int((uptime_seconds % 86400) // 3600)
    
    return SystemInfo(
        cpu_percent=cpu_percent,
        cpu_count=cpu_count,
        memory_percent=mem.percent,
        memory_total=mem.total / (1024**3),
        memory_used=mem.used / (1024**3),
        disk_percent=disk.percent,
        disk_total=disk.total / (1024**3),
        disk_used=disk.used / (1024**3),
        uptime_days=uptime_days,
        uptime_hours=uptime_hours
    )

@router.get("/metrics")
def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu": cpu,
        "memory": mem.percent,
        "disk": disk.percent,
        "timestamp": time.time()
    }
