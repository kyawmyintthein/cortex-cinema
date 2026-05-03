class RedditSource:
    def fetch_summary(self, title: str) -> dict:
        return {
            "type": "social_trend",
            "summary": f"Audience discussion around {title} highlights visual scale and cast chemistry.",
            "confidence": "medium",
        }
