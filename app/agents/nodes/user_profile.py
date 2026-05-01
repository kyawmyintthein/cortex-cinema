from app.agents.state import EngagementState
from app.services.user_profile.service import UserProfileService

user_profile_service = UserProfileService()


async def load_user_profile(state: EngagementState) -> EngagementState:
    params = state["params"]
    summary = user_profile_service.get_user_summary(params.user_id)
    return {"user_summary": summary}
