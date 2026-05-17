# Workshop: Agent Architecture & Orchestration with Python

A minimal workshop project for experimenting with:

- Agent architectures
- Multi-step orchestration
- API design with FastAPI
- LLM integrations
- Observability for AI systems

Built with modern Python tooling and focused on developer experience.

## Tech Stack

| Tool             | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Python           | Core language                             |
| uv               | Dependency and environment management     |
| FastAPI          | API framework                             |
| Ruff             | Linting and formatting                    |
| LangChain        | LLM application framework                 |
| LangGraph        | Agent orchestration                       |
| LangChain OpenAI | OpenAI integration                        |
| Langfuse         | Tracing, observability, and cost tracking |
| Docker           | Local development environment             |

## Project Structure

```bash
.
├── app/
│ ├── agents/
│ ├── api/
│ ├── consts/
│ ├── database/
│ ├── graph/
│ ├── helpers/
│ ├── llm/
│ ├── schemas/
│ ├── tools/
│ ├── config.py
│ └── main.py
├── .env
├── docker-compose.dev.yml
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Prerequisites

Before starting, install:

- Docker + Docker Compose (optional)
- Python 3.13+
- uv

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Official docs:

https://docs.astral.sh/uv/

## Quick Start

### Option 1 — Docker (Recommended)

Start the development environment:

```bash
docker compose -f docker-compose.dev.yml up --build
```

View logs:

```bash
docker compose logs -f api
```

Start, stop and restart the container:

```bash
docker compose start|restart|stop
```

Remove the container:

```bash
docker compose down
```

The API will be available at:

```bash
http://127.0.0.1:8000
```

### Option 2 — Local Development

Install dependencies:

```bash
uv sync
```

Run the development server:

```bash
uv run fastapi dev src/main.py
```

Or using uvicorn:

```bash
uv run uvicorn src.main:app --reload
```

## Environment Variables

Create a .env file:

```bash
OPENAI_API_KEY=your_key_here

LANGFUSE_PUBLIC_KEY=your_key_here
LANGFUSE_SECRET_KEY=your_key_here
LANGFUSE_BASE_URL=langfuse_base_url
```

## API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```bash
http://127.0.0.1:8000/openapi.json
```

## Endpoints

### Health Check

Request:

```http
GET /health
```

Example:

```bash
curl http://127.0.0.1:8000/health
```

Response:

```json
{
  "status": "ok"
}
```

### Process Ticket

Processes a logistics support ticket through the orchestration workflow.

Request:

```http
POST /api/v1/logistics/process-ticket
```

Example:

```bash
curl 'http://127.0.0.1:8000/api/v1/logistics/process-ticket' \
--header 'Content-Type: application/json' \
--data '{
  "ticket_id": "T-99822",
  "source": "CUSTOMER_EMAIL",
  "content": "Hola, necesito la factura del envío #ORD-123 entregado ayer para presentar mis impuestos. Gracias.",
  "metadata": {
    "severity": "LOW",
    "customer_segment": "B2B"
  }
}'
```

Response:

```json
{
  "response": "The response"
}
```

## Development

Lint:

```bash
uv run ruff check .
```

Format:

```bash
uv run ruff format .
```

## Architecture Goals

This workshop explores patterns such as:

- Agent-based workflows
- State-driven orchestration
- Tool calling
- Structured outputs
- Human-in-the-loop systems
- Observability and tracing
- Modular API design

## Future Improvements

- Authentication
- Async workflows
- Streaming responses
- Queue-based processing
- Persistent memory
- Evaluation pipelines
- CI/CD pipelines
- Unit and integration testing
