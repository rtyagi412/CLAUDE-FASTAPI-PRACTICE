from fastapi import FastAPI

from app.api.v1.router import router as v1_router
from app.core.logging import configure_logging
from app.core.settings import settings

configure_logging(settings.log_level)

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1_router)
