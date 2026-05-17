from typing import Literal

from pydantic import BaseModel

from app.llm.models import gpt_4o_mini

llm = gpt_4o_mini.bind(temperature=0.0)

class CustomerServiceOutput(BaseModel):
    classification: Literal[
        "factura",
        "estado_pedido",
        "estado_reembolso",
        "quejas",
        "desconocido"
    ]

def customer_service_classifier(state):
    ticket_content = state.get("ticket", {}).get("content")
    
    prompt = f"""
        Analiza el siguiente textoy clasificalo en una de estas categorías:
        - factura
        - estado_pedido
        - estado_reembolso
        - quejas
        - desconocido
  
        Texto:
        {ticket_content}
        """

    try:
        structured_llm = llm.with_structured_output(CustomerServiceOutput)

        response = structured_llm.invoke(prompt)
        classification = response.classification
    except Exception:
        classification = "desconocido"

    state["customer_service_classification"] = classification
    print(f"===> Classification: {classification}")

    return state