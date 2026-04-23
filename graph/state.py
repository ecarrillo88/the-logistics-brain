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
  request: Ticket
  response: str