class UserProfileService:
    def get_user_summary(self, user_id: str | None) -> dict:
        if not user_id:
            return {
                "topGenres": [],
                "favoriteActors": [],
                "recentThemes": [],
                "preferredPacing": None,
                "personalizationConfidence": "none",
                "revealedFactIds": [],
            }

        return {
            "topGenres": ["Sci-Fi", "Thriller"],
            "favoriteActors": ["Actor A"],
            "recentThemes": ["space", "mystery"],
            "preferredPacing": "slow-burn",
            "personalizationConfidence": "medium",
            "revealedFactIds": [],
        }
