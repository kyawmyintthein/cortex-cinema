from app.agents.state import EngagementState
from app.llm.gateway import LLMGateway

llm_gateway = LLMGateway()


async def generate_teaser_question(state: EngagementState) -> EngagementState:
    result = llm_gateway.generate_teaser_question(
        movie=state.get("movie", {}),
        trend_summary=state.get("trend_summary", {}),
    )
    return {"teaser_question": result}
