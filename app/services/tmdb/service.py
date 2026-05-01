from app.services.tmdb.client import TMDBClient
from app.services.tmdb.mapper import map_movie_context


class TMDBService:
    def __init__(self, client: TMDBClient | None = None) -> None:
        self.client = client or TMDBClient()

    def build_movie_context(self, tmdb_id: int) -> dict:
        details = self.client.get_movie_details(tmdb_id)
        credits = self.client.get_movie_credits(tmdb_id)
        return map_movie_context(details, credits)
