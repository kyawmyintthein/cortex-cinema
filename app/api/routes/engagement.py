from fastapi import APIRouter, Query, status

from app.agents.orchestrator import EngagementOrchestrator
from app.analytics.events import EngagementAnalyticsService
from app.api.schemas.engagement import (
    AcceptedResponse,
    EngagementFeedbackRequest,
    EngagementQueryParams,
    EngagementResponse,
    EngagementRevealRequest,
)
from app.cache.service import EngagementCacheService
from app.storage.repositories.feedback import FeedbackRepository
from app.storage.repositories.reveal_history import RevealHistoryRepository

router = APIRouter(tags=["engagement"])

cache_service = EngagementCacheService()
reveal_history_repository = RevealHistoryRepository()
feedback_repository = FeedbackRepository()
analytics_service = EngagementAnalyticsService()
orchestrator = EngagementOrchestrator(
    cache_service=cache_service,
    reveal_history_repository=reveal_history_repository,
)


@router.get(
    "/movies/{tmdb_id}/engagement",
    response_model=EngagementResponse,
    summary="Get movie engagement content",
    description=(
        "Returns teaser-question engagement content for a movie detail page. "
        "The response can include personalized why-watch copy and an optional hook."
    ),
)
async def get_engagement(
    tmdb_id: int,
    user_id: str | None = Query(
        default=None,
        alias="userId",
        description="Optional user identifier for personalization and repeat avoidance.",
    ),
    include_hook: bool = Query(
        default=False,
        alias="includeHook",
        description="Whether to include the optional hook field in the response.",
    ),
    client_platform: str | None = Query(
        default=None,
        alias="clientPlatform",
        description="Client platform identifier such as ios.",
    ),
    locale: str | None = Query(
        default=None,
        description="Optional locale code for future localization support.",
    ),
) -> EngagementResponse:
    params = EngagementQueryParams(
        user_id=user_id,
        include_hook=include_hook,
        client_platform=client_platform,
        locale=locale,
    )
    response = await orchestrator.get_engagement(tmdb_id=tmdb_id, params=params)
    analytics_service.record_fetch(
        tmdb_id=tmdb_id,
        user_id=user_id,
        cache_hit=response.metadata.cache_hit,
    )
    return response


@router.post(
    "/movies/{tmdb_id}/engagement/reveal",
    response_model=AcceptedResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Record reveal event",
    description="Records that a user revealed the fun-fact answer for a movie engagement card.",
)
async def post_reveal(tmdb_id: int, request: EngagementRevealRequest) -> AcceptedResponse:
    reveal_history_repository.record_reveal(
        user_id=request.user_id,
        movie_id=tmdb_id,
        fact_id=request.fact_id,
        revealed_at=request.revealed_at,
    )
    analytics_service.record_reveal(
        tmdb_id=tmdb_id,
        user_id=request.user_id,
        fact_id=request.fact_id,
    )
    return AcceptedResponse(status="accepted")


@router.post(
    "/movies/{tmdb_id}/engagement/feedback",
    response_model=AcceptedResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Record feedback event",
    description="Records helpful or not-helpful feedback for a generated engagement fact.",
)
async def post_feedback(tmdb_id: int, request: EngagementFeedbackRequest) -> AcceptedResponse:
    feedback_repository.record_feedback(
        user_id=request.user_id,
        movie_id=tmdb_id,
        fact_id=request.fact_id,
        feedback=request.feedback,
    )
    analytics_service.record_feedback(
        tmdb_id=tmdb_id,
        user_id=request.user_id,
        fact_id=request.fact_id,
        feedback=request.feedback,
    )
    return AcceptedResponse(status="accepted")
