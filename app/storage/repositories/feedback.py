class FeedbackRepository:
    def __init__(self) -> None:
        self._items: list[dict] = []

    def record_feedback(self, user_id: str, movie_id: int, fact_id: str, feedback: str) -> None:
        self._items.append(
            {
                "user_id": user_id,
                "movie_id": movie_id,
                "fact_id": fact_id,
                "feedback": feedback,
            }
        )
