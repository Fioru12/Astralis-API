from fastapi import APIRouter

router = APIRouter()

@router.get("/containers")
def list_containers():
    return {"containers": []}

@router.post("/{container_id}/start")
def start_container(container_id: str):
    return {"message": f"Container {container_id} started"}
