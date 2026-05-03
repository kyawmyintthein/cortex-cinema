def rank_fact_candidates(candidates: list[dict], trend_summary: dict) -> list[dict]:
    if not trend_summary.get("enabled"):
        return candidates

    def score(candidate: dict) -> tuple[int, int]:
        trend_bonus = 1 if candidate.get("sourceType") == "trend" else 0
        confidence_score = {"high": 3, "medium": 2, "low": 1}.get(candidate.get("confidence"), 0)
        return (trend_bonus, confidence_score)

    return sorted(candidates, key=score, reverse=True)
