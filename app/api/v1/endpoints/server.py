from fastapi import APIRouter
from pydantic import BaseModel
import subprocess
import os

router = APIRouter()

class ServerStatus(BaseModel):
    name: str
    status: str
    players: int
    port: int

class ServerAction(BaseModel):
    action: str
    server_name: str

@router.get("/status", response_model=ServerStatus)
def get_server_status():
    # Check if Docker container is running
    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", "name=zomboid-server", "--format", "{{.Status}}"],
            capture_output=True,
            text=True
        )
        status = "running" if result.stdout.strip() else "stopped"
    except Exception:
        status = "unknown"
    
    return ServerStatus(
        name="AstralisZomboid",
        status=status,
        players=0,
        port=16261
    )

@router.post("/action")
def server_action(action: ServerAction):
    actions_map = {
        "start": ["docker", "start", "zomboid-server"],
        "stop": ["docker", "stop", "zomboid-server"],
        "restart": ["docker", "restart", "zomboid-server"]
    }
    
    if action.action not in actions_map:
        return {"error": "Invalid action"}
    
    try:
        result = subprocess.run(
            actions_map[action.action],
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            "message": f"Server {action.action} completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {"error": "Action timed out"}
    except Exception as e:
        return {"error": str(e)}
