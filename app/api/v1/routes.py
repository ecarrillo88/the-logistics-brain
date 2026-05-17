from fastapi import APIRouter

from app.graph.graph import build_graph
from app.schemas.ticket import TicketRequest, TicketResponse

router_v1 = APIRouter(prefix="/api/v1", tags=["v1"])

@router_v1.post(
    "/logistics/process-ticket",
    summary="Process a logistics ticket",
    description="""Receives and processes logistics tickets by automatically determining the appropriate
    workflow based on their type and priority. Executes operational actions for high-priority incidents
    and generates structured responses for administrative requests.""",
    response_model=TicketResponse
)
def process_ticket(req: TicketRequest):
    state = {
        "ticket": {
            "ticket_id": req.ticket_id,
            "source": req.source,
            "content": req.content,
            "metadata": req.metadata
        },
        "response": ""
    }

    res = build_graph().invoke(state)

    return {"response": res["response"]}