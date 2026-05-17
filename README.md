# Workshop: Agent Architecture & Orchestration with Python

This project is a minimal starting point for experimenting with API design, agent architectures, and orchestration patterns using Python.

---

## Requirements

- uv: An extremely fast Python package and project manager, written in Rust.
- FastAPI: FastAPI framework, high performance, easy to learn, fast to code, ready for production.
- Ruff: An extremely fast Python linter and code formatter, written in Rust.
- LangChain: LangChain is the platform for agent engineering
- LangChain OpenAI: An integration package connecting OpenAI and LangChain
- LangGraph: Agent Orchestration Framework for Reliable AI Agents
- Langfuse: Langfuse is an observability tool for LLM apps that tracks prompts, traces, and costs.

---

## Setup

### Docker

Start development environment:

```bash
docker compose -f docker-compose.dev.yml up --build
```

Logs:

```bash
docker compose logs -f api
```

Start, stop and restart the app:

```bash
docker compose start|restart|stop
```

Remove the container:

```bash
docker compose down
```

The API will be available at:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

### Manually

You need to have uv installed:

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

Install via curl:

```bash id="2h7q1x"
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install via wget:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Install via pip:

```bash
pip install uv
```

### Install dependencies:

```bash
uv sync
```

Start the API server:

```bash
uv run fastapi dev src/main.py
```

or

```bash
uv run uvicorn src.main:app --reload
```

The API will be available at:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Health Check

### Endpoint

```http
GET /health
```

### Test it

```bash
curl http://127.0.0.1:8000/health
```

### Response

```json
{
  "status": "ok"
}
```
