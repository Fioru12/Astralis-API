from fastapi import APIRouter
import subprocess
from typing import List, Dict

router = APIRouter()

@router.get("/containers")
def list_containers() -> List[Dict]:
    try:
        result = subprocess.run(
            ["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}\t{{.Ports}}"],
            capture_output=True,
            text=True
        )
        
        containers = []
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                if line:
                    parts = line.split("\t")
                    containers.append({
                        "name": parts[0],
                        "status": parts[1] if len(parts) > 1 else "unknown",
                        "ports": parts[2] if len(parts) > 2 else ""
                    })
        return containers
    except Exception as e:
        return [{"error": str(e)}]

@router.get("/{container_id}/logs")
def get_container_logs(container_id: str, tail: int = 50):
    try:
        result = subprocess.run(
            ["docker", "logs", "--tail", str(tail), container_id],
            capture_output=True,
            text=True
        )
        return {
            "container": container_id,
            "logs": result.stdout,
            "errors": result.stderr
        }
    except Exception as e:
        return {"error": str(e)}
