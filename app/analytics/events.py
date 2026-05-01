class EngagementAnalyticsService:
    def record_fetch(self, tmdb_id: int, user_id: str | None, cache_hit: bool) -> None:
        return None

    def record_reveal(self, tmdb_id: int, user_id: str, fact_id: str) -> None:
        return None

    def record_feedback(self, tmdb_id: int, user_id: str, fact_id: str, feedback: str) -> None:
        return None
