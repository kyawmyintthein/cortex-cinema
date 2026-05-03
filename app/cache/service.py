class EngagementCacheService:
    def __init__(self) -> None:
        self.final_response_cache: dict[str, dict] = {}

    def build_final_response_key(
        self,
        tmdb_id: int,
        user_id: str | None,
        include_hook: bool,
        locale: str | None,
    ) -> str:
        return f"{user_id or 'anonymous'}:{tmdb_id}:{include_hook}:{locale or 'default'}:v1.0.0"

    def get_final_response(self, key: str) -> dict | None:
        return self.final_response_cache.get(key)

    def set_final_response(self, key: str, payload: dict) -> None:
        self.final_response_cache[key] = payload
