class NewsSource:
    def fetch_summary(self, title: str) -> dict:
        return {
            "type": "publisher",
            "summary": f"Recent coverage frames {title} as a movie with strong discussion energy.",
            "confidence": "high",
        }
