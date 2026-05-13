from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.schemas.health import HealthResponse

router = APIRouter()

@router.get(
    "/health",
    summary="Service health check",
    description="""Checks the health status of the service. Returns information indicating whether the
    application is running and able to handle requests.""",
    response_model=HealthResponse,
    tags=["health"]
)
def health():
    return JSONResponse(
        status_code=200,
        content={"status": "ok"}
    )