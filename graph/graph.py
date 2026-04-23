from langgraph.graph import StateGraph, START, END
from agents.logistic_operator import logistic_operator
from agents.customer_service import customer_service
from graph.router import planner
from graph.state import State

def build_graph():
  graph = StateGraph(State)

  graph.add_node("logistic_operator_agent", logistic_operator)
  graph.add_node("Customer_service_agent", customer_service)

  graph.add_conditional_edges(START, planner)

  graph.add_edge("logistic_operator_agent", END)
  graph.add_edge("Customer_service_agent", END)

  return graph.compile()