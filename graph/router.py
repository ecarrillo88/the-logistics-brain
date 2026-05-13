from consts.consts import DRIVER_APP

def classify_ticket(state):
    source  = state.get("ticket", {}).get("source")
    if source == DRIVER_APP:
        ticket_classification = "logistic_operator_response"
        print(f"===> Ticket classification: {ticket_classification}")
        return ticket_classification
    else:
        ticket_classification = "classify_customer_service_ticket"
        print(f"===> Ticket classification: {ticket_classification}")
        return ticket_classification
