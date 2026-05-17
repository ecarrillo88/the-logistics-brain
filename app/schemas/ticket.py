from typing import Literal

from pydantic import BaseModel


class Metadata(BaseModel):
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    driver_id: str | None = None
    customer_segment: str | None = None

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
    response: str

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "example": {
                "response": "Request processed"
            }
        }
    }