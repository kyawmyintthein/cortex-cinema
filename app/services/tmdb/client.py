class TMDBClient:
    """Placeholder client for TMDB-backed integrations."""

    def get_movie_details(self, tmdb_id: int) -> dict:
        return {
            "id": tmdb_id,
            "title": "Example Title",
            "overview": "A normalized movie summary for engagement generation.",
            "genres": ["Sci-Fi", "Drama"],
            "release_year": 2024,
            "director": "Director Name",
            "top_cast": ["Actor A", "Actor B"],
            "popularity_band": "high",
        }

    def get_movie_credits(self, tmdb_id: int) -> dict:
        return {
            "director": "Director Name",
            "top_cast": ["Actor A", "Actor B"],
        }
