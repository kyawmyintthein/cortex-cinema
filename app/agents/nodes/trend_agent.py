from app.agents.state import EngagementState
from app.services.trends.service import TrendService

trend_service = TrendService()


async def maybe_load_trend_context(state: EngagementState) -> EngagementState:
    movie = state.get("movie", {})
    trend_summary = trend_service.get_trend_summary(movie=movie)
    return {"trend_summary": trend_summary}
