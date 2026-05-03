from app.agents.state import EngagementState
from app.services.tmdb.service import TMDBService

tmdb_service = TMDBService()


async def load_movie_context(state: EngagementState) -> EngagementState:
    movie = tmdb_service.build_movie_context(state["tmdb_id"])
    return {"movie": movie}
