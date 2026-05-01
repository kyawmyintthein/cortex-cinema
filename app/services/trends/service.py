from app.services.trends.sources.news import NewsSource
from app.services.trends.sources.reddit import RedditSource
from app.services.trends.sources.x import XSource


class TrendService:
    def __init__(self) -> None:
        self.sources = [NewsSource(), RedditSource(), XSource()]

    def get_trend_summary(self, movie: dict) -> dict:
        if not movie:
            return {"enabled": False, "items": []}

        items = [source.fetch_summary(movie["title"]) for source in self.sources]
        items = [item for item in items if item is not None]
        return {"enabled": bool(items), "items": items}
