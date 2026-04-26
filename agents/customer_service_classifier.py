from pydantic import BaseModel
from typing import Literal, Optional
from langchain_openai import ChatOpenAI
from tools.orders import get_order_details
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

class CustomerServiceOutput(BaseModel):
    classification: Literal[
        "factura",
        "estado_pedido",
        "estado_reembolso",
        "quejas",
        "desconocido"
    ]
    order_id: Optional[str]

def customer_service_classifier(state):
    ticket_content = state["ticket"]["content"]
    
    prompt = f"""
        Analiza el siguiente textoy clásificalo según su tipo.
        Extrae también el número de pedido. Tendrá el formato #ORD-xxx, siendo xxx una secuencia numérica.
        Responde ÚNICAMENTE en formato JSON válido:
        {{"classification": "factura|estado_pedido|estado_reembolso|quejas|desconocido", "order_id": "#ORD-xxx|None"}}
  
        Texto: {ticket_content}
    """

    structured_llm = llm.with_structured_output(CustomerServiceOutput)

    response = structured_llm.invoke(prompt)

    state["customer_service_classification"] = response.classification
    state["order"] = get_order_details.invoke({"order_id": response.order_id})

    return state