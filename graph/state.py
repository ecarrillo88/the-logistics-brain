from typing import TypedDict, Optional

class Metadata(TypedDict):
  severity: str
  driver_id: Optional[str] = None
  customer_segment: Optional[str] = None

class Ticket(TypedDict):
  ticket_id: str
  source: str
  content: str
  metadata: Metadata

class State(TypedDict):
  ticket: Ticket
  execution_intent: Optional[str]
  order: Optional[dict]
  customer_service_classification: Optional[dict]
  logistic_operator_type_type: Optional[dict]
  response: str