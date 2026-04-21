from pydantic import BaseModel
from typing import Literal, Optional

class Metadata(BaseModel):
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    driver_id: Optional[str] = None
    customer_segment: Optional[str] = None

    model_config = {
        "extra": "forbid",
    }

class TicketRequest(BaseModel):
    ticket_id: str
    source: Literal["DRIVER_APP", "CUSTOMER_EMAIL"]
    content: str
    metadata: Metadata

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "ticket_id": "T-99822",
                "source": "CUSTOMER_EMAIL",
                "content": "Hola, necesito la factura del envío #ORD-123 entregado ayer para presentar mis impuestos. Gracias.",
                "metadata": {
                    "severity": "LOW",
                    "customer_segment": "B2B"
                }
            }
        }
    }

class TicketResponse(BaseModel):
    status: str
    version: str

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "status": "processed",
                "version": "v1"
            }
        }
    }