from fastapi import FastAPI

from app.api.routes.engagement import router as engagement_router
from app.api.routes.health import router as health_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app.name,
        version=settings.app.version,
        description="Mobile-facing engagement API for teaser, fun fact, and why-watch copy.",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_tags=[
            {
                "name": "health",
                "description": "Operational health and readiness endpoints.",
            },
            {
                "name": "engagement",
                "description": "Movie engagement, reveal, and feedback endpoints.",
            },
        ],
    )
    app.include_router(health_router)
    app.include_router(engagement_router, prefix="/v1")
    return app


app = create_app()
