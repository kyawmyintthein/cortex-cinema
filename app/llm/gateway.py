from app.llm.client import OpenAIClient


class LLMGateway:
    """Shared generation boundary with deterministic placeholders for the scaffold."""

    def __init__(self, client: OpenAIClient | None = None) -> None:
        self.client = client or OpenAIClient()

    def generate_teaser_question(self, movie: dict, trend_summary: dict) -> str:
        title = movie.get("title", "this movie")
        if trend_summary.get("enabled"):
            return f"Why has {title} sparked so much fresh conversation lately?"
        return f"What keeps {title} feeling like a movie people want to talk about?"

    def generate_fun_fact_candidates(
        self,
        movie: dict,
        trend_summary: dict,
        revealed_fact_ids: list[str],
    ) -> list[dict]:
        title = movie.get("title", "This movie")
        overview = movie.get("overview", "It has a distinctive style.")
        base_candidates = [
            {
                "factId": "fact_001",
                "teaserQuestion": f"What gives {title} its staying power with audiences?",
                "funFactAnswer": f"{title} stands out because {overview.lower()}",
                "trendTags": ["evergreen"],
                "confidence": "high",
                "sourceType": "tmdb",
            },
            {
                "factId": "fact_002",
                "teaserQuestion": f"Why do people keep resurfacing {title} in recommendation threads?",
                "funFactAnswer": (
                    f"Conversation around {title} keeps returning to its mix of scale, atmosphere, "
                    "and replayable discussion value."
                ),
                "trendTags": ["discussion"],
                "confidence": "medium",
                "sourceType": "trend" if trend_summary.get("enabled") else "tmdb",
            },
            {
                "factId": "fact_003",
                "teaserQuestion": f"What makes {title} feel worth discovering right now?",
                "funFactAnswer": (
                    f"It blends recognizable movie appeal with enough distinctive texture to keep people "
                    "comparing notes after they watch."
                ),
                "trendTags": ["discovery"],
                "confidence": "medium",
                "sourceType": "tmdb",
            },
        ]
        unseen = [candidate for candidate in base_candidates if candidate["factId"] not in revealed_fact_ids]
        return unseen or base_candidates

    def generate_why_watch_now(self, movie: dict, user_summary: dict) -> str:
        genres = user_summary.get("topGenres", [])
        if genres:
            return f"You have been leaning into {genres[0].lower()} lately, and this is a strong match for that mood."
        return "A strong choice if you want something engaging tonight."

    def generate_hook(self, movie: dict, trend_summary: dict) -> str:
        title = movie.get("title", "this movie")
        if trend_summary.get("enabled"):
            return f"{title} has the kind of momentum that makes it easy to recommend right now."
        return f"{title} is an easy pick when you want something with conversation value."
