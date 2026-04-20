from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return JSONResponse(
        status_code=200,
        content={"status": "ok"}
    )

router_v1 = APIRouter(prefix="/api/v1", tags=["v1"])

@router_v1.post("/logistics/process-ticket", tags=["logistics"])
def process_ticket():
    return {"status": "processed", "version": "v1"}

app.include_router(router_v1)