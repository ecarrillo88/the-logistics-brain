from typing import TypedDict


class Metadata(TypedDict):
    severity: str
    driver_id: str | None = None
    customer_segment: str | None = None

class Ticket(TypedDict):
    ticket_id: str
    source: str
    content: str
    metadata: Metadata

class State(TypedDict):
    ticket: Ticket
    order: dict | None
    customer_service_classification: dict | None
    logistic_operator_type_type: dict | None
    response: str