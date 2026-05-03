def select_fact_candidate(candidates: list[dict], revealed_fact_ids: list[str]) -> dict:
    for candidate in candidates:
        if candidate["factId"] not in revealed_fact_ids:
            return candidate
    return candidates[0]
