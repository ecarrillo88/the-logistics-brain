from langchain.tools import tool

@tool
def verify_driver_status(driver_id: str):
  """Returns remaining driving hours."""
  return 18