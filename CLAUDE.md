# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv sync                                      # install / sync dependencies
uv run uvicorn app.main:app --reload         # run dev server
uv run pytest                                # run all tests
uv run pytest tests/test_health.py::test_foo # run a single test
uv run ruff check .                          # lint
uv run ruff format .                         # format
```

## Architecture

This is a FastAPI service managed with **uv**. Key layout:

```
app/
  main.py           # creates FastAPI app, includes routers, calls configure_logging()
  api/v1/
    health.py       # GET /v1/health
  core/
    settings.py     # pydantic-settings BaseSettings (APP_NAME, LOG_LEVEL)
    logging.py      # configure_logging(log_level) called once at startup
tests/
  test_health.py    # pytest tests for /health and /v1/health
```

- `app/main.py` mounts `GET /health` directly and includes the `app/api/v1/` router.
- Settings are loaded from env vars via `pydantic-settings`; defaults work without any `.env` file.
- Logging is configured at app startup using `LOG_LEVEL` from settings.
- In-memory state only — no database, no auth.

## Spec

See `SPEC.md` for full endpoint contracts and acceptance criteria.
