from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["health"])


@router.get(
    "/healthz",
    summary="Health check",
    description="Simple readiness endpoint for local smoke tests and container health checks.",
)
async def healthcheck() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app.name,
        "version": settings.app.version,
    }
