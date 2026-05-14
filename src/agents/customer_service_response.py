import json

from langchain_openai import ChatOpenAI

from src.config import config
from src.tools.orders import generate_invoice_pdf

llm = ChatOpenAI(
    model=config.OPENAI_MODEL,
    api_key=config.OPENAI_API_KEY,
    temperature=0.3
)

def customer_service_response(state):
    order = state.get("order")
    classification = state.get("customer_service_classification")
    invoice_pdf_url = None

    if(classification == "factura" and order):
        invoice_pdf_url = generate_invoice_pdf.invoke({"order_id": order.get("order_id")})

    order_json = json.dumps(
        order,
        indent=2,
        ensure_ascii=False
    ) if order else "No disponible"

    prompt = f"""
    Eres un asistente de atención al cliente.

    Tu objetivo es redactar una respuesta:
    - formal
    - empática
    - clara
    - estructurada

    Devuelve únicamente HTML válido.

    Datos del pedido:
    {order_json}

    URL factura:
    {invoice_pdf_url}

    Clasificación de la respuesta:
    {classification}

    Instrucciones:
    - No inventes información
    - Mantén tono profesional
    - Saluda al cliente utilizando su nombre
    - Adapta la respuesta según la clasificación

    Formato requerido:
    - usar <p> para párrafos
    - usar <strong> para destacar información importante
    - usar <ul>/<li> si hay enumeraciones
    - incluir enlaces usando <a href="">
    - NO usar markdown
    - NO usar bloques de código
    - NO incluir <html> ni <body>

    Redacta la respuesta final al cliente.
    """

    response = llm.invoke(prompt)

    return {"response": response.content}