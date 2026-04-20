# 🚀 Workshop: Arquitectura de Agentes & Orquestación con Python

**Objetivo:** Diseñar un microservicio escalable ("The Logistics Brain") que procese incidencias logísticas de diferente naturaleza. Se busca demostrar criterio arquitectónico, limpieza de código y la capacidad de decidir cuándo aplicar agentes complejos y cuándo utilizar lógica determinista.

---

## Step 1: Setup

Queremos que este servicio esté listo para desplegarse. Crea un servicio con un único endpoint de health.

* **Gestor de Entorno:** Uso obligatorio de **uv** (astral-sh) para la gestión del proyecto y dependencias.
* **Servidor:** FastAPI + Uvicorn.
* **Calidad:** Configura **ruff** (como linter y formatter) para asegurar un código limpio y estandarizado.
* **Arquitectura:** Debe tener una arquitectura limpia

---

## Step 2: El Desafío de la Lógica de Negocio

**Endpoint:** `POST /api/v1/logistics/process-ticket`

Tu misión es construir un flujo de trabajo orquestado con **LangChain/LangGraph** que gestione la entrada de tickets. El sistema recibirá incidencias de diferentes fuentes y **debe ser capaz de ejecutar el flujo de trabajo correcto automáticamente** basándose en los datos de entrada, optimizando costes y latencia.

### Los Escenarios de Negocio

1. **Escenario: Operaciones en Campo (Alta Criticidad)**
    * Son incidencias reportadas directamente por los conductores desde la App (ej: accidentes, tráfico, averías).
    * El sistema debe comportarse como un **Operador Logístico Autónomo**. No basta con responder; debe investigar la situación y tomar decisiones operativas.
    * Requiere un ciclo de razonamiento (ReAct) para consultar el estado del tráfico, la ubicación del pedido y, si es necesario, ejecutar acciones de modificación.

2. **Escenario: Gestión Administrativa (Baja Criticidad)**
    * Son correos o mensajes de clientes solicitando información documental o quejas formales (ej: facturas, estado de reembolso).
    * El sistema debe actuar como un **Asistente de Atención al Cliente**.
    * El objetivo es generar una respuesta formal, estructurada y empática. No requiere acceso a sistemas de tráfico en tiempo real ni bucles de razonamiento complejos, solo capacidad de redacción y formateo.

### Caja de Herramientas (The Toolbox)

El sistema tiene acceso a las siguientes funciones (debes mockearlas/simularlas). Es tu responsabilidad decidir qué partes del sistema tienen acceso a qué herramientas:

* `get_order_details(order_id)`: Devuelve metadatos, cliente y estado.
* `check_road_incidents(gps_coords)`: Devuelve alertas de tráfico (DGT/Waze).
* `verify_driver_status(driver_id)`: Devuelve horas de conducción restantes.
* `update_delivery_schedule(order_id, new_time)`: Acción de escritura que cambia la entrega.
* `generate_invoice_pdf(order_id)`: Simula la generación de un enlace de descarga.

#### Modelos disponibles

Usar gemini-2.5-flash o gemini-2.5-flash-lite (Como más económico mejor)

---

### Step 3: Estrategia de Testing

Buscamos tests que validen el comportamiento del sistema, no solo que el código compile. Define 3-4 tests que validen el funcionamiento del agente.

---

### Step 4: EXTRA

Si quieres probar alguna de las tecnologías con las que trabajarás puedes tratar de añadir:

* **Observabilidad:** Integra **Langfuse** (self-hosted o cloud free).
* **Dockerización:** Crea un `Dockerfile` optimizado.
* **Streaming:** Haz que el endpoint pueda devolver la respuesta token a token (Server-Sent Events).

---

### Ejemplos de Inputs

Tu sistema debe ser capaz de procesar estos dos JSONs y derivarlos a la lógica adecuada sin intervención humana manual.

**Input 1:**

```json
{
  "ticket_id": "T-99821",
  "source": "DRIVER_APP",
  "content": "Estoy parado en la M-30 por un accidente. Llevo el pedido #ORD-555 (refrigerado) y me quedan solo 2 horas de tacógrafo.",
  "metadata": {
    "severity": "CRITICAL",
    "driver_id": "D-123"
  }
}
```

**Input 2:**

```json
{
  "ticket_id": "T-99822",
  "source": "CUSTOMER_EMAIL",
  "content": "Hola, necesito la factura del envío #ORD-123 entregado ayer para presentar mis impuestos. Gracias.",
  "metadata": {
    "severity": "LOW",
    "customer_segment": "B2B"
  }
}
```
