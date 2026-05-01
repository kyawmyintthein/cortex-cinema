class XSource:
    def fetch_summary(self, title: str) -> dict:
        return {
            "type": "social_trend",
            "summary": f"Short-form conversation about {title} centers on momentum and shareable moments.",
            "confidence": "low",
        }
