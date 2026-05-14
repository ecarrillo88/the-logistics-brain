from langgraph.graph import END, START, StateGraph

from src.agents.customer_service_classifier import customer_service_classifier
from src.agents.customer_service_response import customer_service_response
from src.agents.logistic_operator_response import logistic_operator_response
from src.graph.node import get_order
from src.graph.router import classify_ticket
from src.graph.state import State


def build_graph():
    graph = StateGraph(State)

    graph.add_node("classify_customer_service_ticket", customer_service_classifier)
    graph.add_node("logistic_operator_response", logistic_operator_response)
    graph.add_node("get_order", get_order)
    graph.add_node("customer_service_response", customer_service_response)

    graph.add_conditional_edges(START, classify_ticket)

    graph.add_edge("logistic_operator_response", END)
    graph.add_edge("classify_customer_service_ticket", "get_order")
    graph.add_edge("get_order", "customer_service_response")
    graph.add_edge("customer_service_response", END)

    return graph.compile()