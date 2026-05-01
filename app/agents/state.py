from typing import Any, TypedDict

from app.api.schemas.engagement import EngagementQueryParams


class EngagementState(TypedDict, total=False):
    tmdb_id: int
    params: EngagementQueryParams
    movie: dict[str, Any]
    user_summary: dict[str, Any]
    trend_summary: dict[str, Any]
    revealed_fact_ids: list[str]
    teaser_question: str
    fun_fact_answer: str
    why_watch_now: str
    hook: str | None
    fact_candidates: list[dict[str, Any]]
    fact_id: str
    composed_response: dict[str, Any]
    validation: dict[str, Any]
