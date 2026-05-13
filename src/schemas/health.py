from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "status": "ok"
            }
        }
    }