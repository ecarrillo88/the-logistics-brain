from consts.consts import DRIVER_APP

def planner(state):
  if state["source"] == DRIVER_APP:
    return "logistic_operator_agent"
  else:
    return "Customer_service_agent"