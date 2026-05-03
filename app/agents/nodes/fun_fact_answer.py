from app.agents.state import EngagementState
from app.llm.gateway import LLMGateway

llm_gateway = LLMGateway()


async def generate_fun_fact_answer(state: EngagementState) -> EngagementState:
    generated = llm_gateway.generate_fun_fact_candidates(
        movie=state.get("movie", {}),
        trend_summary=state.get("trend_summary", {}),
        revealed_fact_ids=state.get("revealed_fact_ids", []),
    )
    best_candidate = generated[0]
    return {
        "fact_candidates": generated,
        "fun_fact_answer": best_candidate["funFactAnswer"],
        "fact_id": best_candidate["factId"],
    }
