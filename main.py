from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

from schemas.health import HealthResponse
from schemas.ticket import TicketRequest, TicketResponse

app = FastAPI()

@app.get(
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

router_v1 = APIRouter(prefix="/api/v1", tags=["v1"])

@router_v1.post(
    "/logistics/process-ticket",
    summary="Process a logistics ticket",
    description="""Receives and processes logistics tickets by automatically determining the appropriate
    workflow based on their type and priority. Executes operational actions for high-priority incidents
    and generates structured responses for administrative requests.""",
    response_model=TicketResponse
)
def process_ticket(ticket: TicketRequest):
    return {"status": "processed", "version": "v1"}

app.include_router(router_v1)