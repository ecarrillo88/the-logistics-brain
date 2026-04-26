from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

from tools.orders import generate_invoice_pdf

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def customer_service_response(state):
    order = state["order"]
    classification = state["customer_service_classification"]
    invoice_pdf_url = None

    if(classification == "factura" and state["order"]):
        invoice_pdf_url = generate_invoice_pdf.invoke({"order_id": state["order"]["order_id"]})

    prompt = f"""
    Eres un asistente de atención al cliente.

    Tu objetivo es redactar una respuesta:
    - formal
    - empática
    - clara
    - estructurada

    Datos del pedido:
    {order}

    URL factura:
    {invoice_pdf_url}

    Clasificación de la respuesta:
    {classification}

    Instrucciones:
    - No inventes información
    - Mantén tono profesional
    - Saluda al cliente utilizando su nombre
    - Adapta la respuesta según la clasificación

    Redacta la respuesta final al cliente.
    """

    response = llm.invoke(prompt)

    return {"response": response.content}