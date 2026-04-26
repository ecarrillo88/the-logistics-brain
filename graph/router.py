from consts.consts import DRIVER_APP

def classify_ticket(state):
  source  = state["ticket"]["source"]
  if source == DRIVER_APP:
    return "logistic_operator_response"
  else:
    return "classify_customer_service_ticket"
