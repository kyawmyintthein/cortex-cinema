from app.agents.state import EngagementState
from app.composition.ranking import rank_fact_candidates
from app.composition.repeat_avoidance import select_fact_candidate
from app.composition.validation import validate_composed_response


async def compose_response(state: EngagementState) -> EngagementState:
    ranked_candidates = rank_fact_candidates(
        state.get("fact_candidates", []),
        trend_summary=state.get("trend_summary", {}),
    )
    selected_candidate = select_fact_candidate(
        ranked_candidates,
        revealed_fact_ids=state.get("revealed_fact_ids", []),
    )

    payload = {
        "movieId": state["tmdb_id"],
        "engagement": {
            "teaserQuestion": state.get("teaser_question", selected_candidate["teaserQuestion"]),
            "funFactAnswer": selected_candidate["funFactAnswer"],
            "whyWatchNow": state.get("why_watch_now", ""),
            "hook": state.get("hook"),
        },
        "metadata": {
            "personalized": state.get("user_summary", {}).get("personalizationConfidence", "none") != "none",
            "trendUsed": bool(state.get("trend_summary", {}).get("enabled")),
            "fallbackUsed": False,
            "hookIncluded": state.get("hook") is not None,
            "factId": selected_candidate["factId"],
            "version": "v1.0.0",
            "cacheHit": False,
        },
    }
    validated = validate_composed_response(payload)
    return {
        "fact_id": selected_candidate["factId"],
        "composed_response": validated,
        "validation": {"fallbackUsed": validated["metadata"]["fallbackUsed"]},
    }
