from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from src.config import config
from src.helpers.common import extract_order_id
from src.tools.driver import verify_driver_status
from src.tools.gps import check_road_incidents
from src.tools.orders import get_order_details, update_delivery_schedule

llm = ChatOpenAI(
    model=config.OPENAI_MODEL,
    api_key=config.OPENAI_API_KEY,
    temperature=0.2
)

agent = create_agent(
    model=llm,
    tools=[
        check_road_incidents,
        get_order_details,
        update_delivery_schedule,
        verify_driver_status
    ],
    system_prompt="""
    Eres un operador logístico autónomo especializado en incidencias de reparto.
    
    Tu función es investigar incidencias reportadas por conductores y recopilar la información necesaria para tomar decisiones operativas.

    No eres un chatbot de atención al cliente.

    OBJETIVOS:
    - Analizar la incidencia reportada
    - Obtener contexto operativo utilizando las herramientas disponibles
    - Detectar riesgos logísticos y de entrega
    - Evaluar el impacto operativo de la incidencia
    - Recomendar acciones operativas justificaddas
    - Generar un informe operativo claro y conciso

    HERRAMIENTAS DISPONIBLES:
    - check_road_incidents(gps_coords): Comprueba incidentes en la ruta
    - get_order_details(order_id): Obtiene los detalles de un pedido
    - update_delivery_schedule(order_id, new_time): Actualiza la fecha estimada de entrega de un pedido
    - verify_driver_status(driver_id): Obtiene las horas de conducción restante del conductor

    REGLAS DE USO DE HERRAMIENTAS:
    - Nunca inventes datos operativos
    - Si falta información crítica, utiliza herramientas para obtenerla
    - No asumas condiciones de tráfico sin verificarlas
    - No asumas disponibilidad del conductor sin comprobarla
    - Minimiza llamadas innecesarias a herramientas
    - Solo ejecuta cambios operativos si existe una justificación clara
    
    POLÍTICA OPERATIVA:
    Debes considerar una reprogramación de entrega cuando:

    - exista una incidencia grave de tráfico,
    Y
    - el conductor tenga pocas horas de conducción disponibles,
    O
    - el retraso estimado supere el margen operativo permitido.

    ESTILO DE RESPUESTA:
    Responde de forma:
    - operativa
    - precisa
    - breve
    - objetiva

    Evita lenguaje conversacional innecesario.

    No inventes información.

    No expongas razonamiento interno ni chain-of-thought.

    FORMATO DE SALIDA:
    Devuelve siempre un informe estructurado con:
    - Resumen de la incidencia
    - Evaluación del riesgo
    - Información operativa relevante
    - Acciones realizadas
    - Recomendación operativa
    - Estado final

    Si no se requiere ninguna acción, explica brevemente el motivo.
    """
)

def build_agent_input(ticket: dict) -> str:
    content = ticket.get("content")
    metadata = ticket.get("metadata", {})

    return f"""
    TICKET OPERATIVO

    ticket_id: {ticket.get("ticket_id")}
    source: {ticket.get("source")}
    severity: {metadata.severity}
    driver_id: {metadata.driver_id}
    order_id: {extract_order_id(content)}

    content:
    {content}
    """

def logistic_operator_response(state):
    ticket = state.get("ticket", {})
    ticket_content = build_agent_input(ticket)

    response = agent.invoke(
        {"messages": [{"role": "user", "content": ticket_content}]}
    )

    final_message = response["messages"][-1]
    return {"response": final_message.content}