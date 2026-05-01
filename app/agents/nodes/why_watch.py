from app.agents.state import EngagementState
from app.llm.gateway import LLMGateway

llm_gateway = LLMGateway()


async def generate_why_watch_now(state: EngagementState) -> EngagementState:
    result = llm_gateway.generate_why_watch_now(
        movie=state.get("movie", {}),
        user_summary=state.get("user_summary", {}),
    )
    return {"why_watch_now": result}
