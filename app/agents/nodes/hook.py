from app.agents.state import EngagementState
from app.llm.gateway import LLMGateway

llm_gateway = LLMGateway()


async def maybe_generate_hook(state: EngagementState) -> EngagementState:
    params = state["params"]
    if not params.include_hook:
        return {"hook": None}
    result = llm_gateway.generate_hook(
        movie=state.get("movie", {}),
        trend_summary=state.get("trend_summary", {}),
    )
    return {"hook": result}
