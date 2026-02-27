# Spec: FastAPI Baseline Service (uv-managed)

## Goal
Create a production-ready FastAPI starter project with clean structure, config, logging, linting, and tests.

## Scope (must have)
### Endpoints
1) `GET /health`
- Purpose: infra readiness/liveness probe
- Response: HTTP 200
- Body: `{ "status": "ok" }`

2) `GET /v1/health`
- Purpose: versioned API example
- Response: HTTP 200
- Body: `{ "status": "ok" }`

### Configuration
Use `pydantic-settings` to load env vars.

Env vars:
- `APP_NAME` (default: `fastapi-agentic`)
- `LOG_LEVEL` (default: `INFO`)

### Logging
- Configure Python logging once at startup using `LOG_LEVEL`.
- Ensure logs do not include secrets (none in this scope).

### Repo structure
Required:
- `app/main.py` creates FastAPI app and includes routers
- `app/api/v1/health.py` defines the versioned health route
- `app/core/settings.py` defines Settings via BaseSettings
- `app/core/logging.py` defines a `configure_logging(log_level: str) -> None`
- `tests/test_health.py` tests both endpoints

### Tooling
- Use **ruff** for lint/format.
- Use **pytest** for tests.
- All checks must pass:
  - `uv run ruff check .`
  - `uv run pytest`

## Non-goals (explicitly out of scope for this spec)
- Authentication/authorization
- Database integration
- Docker/Kubernetes
- OpenAPI customizations beyond defaults
- Advanced error response envelope

## Acceptance Criteria
- Both endpoints return correct JSON and HTTP 200.
- Settings load correctly with defaults (even if env vars not set).
- Logging configuration is invoked at app startup.
- Tests cover `/health` and `/v1/health`.
- Ruff + pytest pass cleanly.

## Local Run Commands
- Install/sync: `uv sync`
- Run app: `uv run uvicorn app.main:app --reload`
- Run tests: `uv run pytest`
- Lint: `uv run ruff check .`