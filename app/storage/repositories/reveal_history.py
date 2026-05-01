from datetime import datetime


class RevealHistoryRepository:
    def __init__(self) -> None:
        self._storage: dict[tuple[str, int], list[str]] = {}

    def get_revealed_fact_ids(self, user_id: str | None, movie_id: int) -> list[str]:
        if not user_id:
            return []
        return list(self._storage.get((user_id, movie_id), []))

    def record_reveal(self, user_id: str, movie_id: int, fact_id: str, revealed_at: datetime) -> None:
        key = (user_id, movie_id)
        existing = self._storage.setdefault(key, [])
        if fact_id not in existing:
            existing.append(fact_id)
