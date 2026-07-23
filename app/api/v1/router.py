from fastapi import APIRouter
from app.api.v1.endpoints import system, server, docker

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(server.router, prefix="/server", tags=["server"])
api_router.include_router(docker.router, prefix="/docker", tags=["docker"])
