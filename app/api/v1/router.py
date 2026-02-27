from fastapi import APIRouter

from app.api.v1 import echo, health, items

router = APIRouter(prefix="/v1")
router.include_router(health.router)
router.include_router(echo.router)
router.include_router(items.router)
