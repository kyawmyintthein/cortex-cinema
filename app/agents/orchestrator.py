from langgraph.graph import END, START, StateGraph

from app.agents.nodes.fun_fact_answer import generate_fun_fact_answer
from app.agents.nodes.hook import maybe_generate_hook
from app.agents.nodes.movie_context import load_movie_context
from app.agents.nodes.response_composer import compose_response
from app.agents.nodes.teaser_question import generate_teaser_question
from app.agents.nodes.trend_agent import maybe_load_trend_context
from app.agents.nodes.user_profile import load_user_profile
from app.agents.nodes.why_watch import generate_why_watch_now
from app.agents.state import EngagementState
from app.api.schemas.engagement import EngagementQueryParams, EngagementResponse
from app.cache.service import EngagementCacheService
from app.storage.repositories.reveal_history import RevealHistoryRepository


class EngagementOrchestrator:
    def __init__(
        self,
        cache_service: EngagementCacheService,
        reveal_history_repository: RevealHistoryRepository,
    ) -> None:
        self.cache_service = cache_service
        self.reveal_history_repository = reveal_history_repository
        self.graph = self._build_graph()

    async def get_engagement(
        self,
        tmdb_id: int,
        params: EngagementQueryParams,
    ) -> EngagementResponse:
        cache_key = self.cache_service.build_final_response_key(
            tmdb_id=tmdb_id,
            user_id=params.user_id,
            include_hook=params.include_hook,
            locale=params.locale,
        )
        cached_response = self.cache_service.get_final_response(cache_key)
        if cached_response is not None:
            cached_response["metadata"]["cacheHit"] = True
            return EngagementResponse.model_validate(cached_response)

        initial_state: EngagementState = {
            "tmdb_id": tmdb_id,
            "params": params,
            "revealed_fact_ids": self.reveal_history_repository.get_revealed_fact_ids(
                user_id=params.user_id,
                movie_id=tmdb_id,
            ),
        }
        final_state = await self.graph.ainvoke(initial_state)
        payload = final_state["composed_response"]
        self.cache_service.set_final_response(cache_key, payload)
        return EngagementResponse.model_validate(payload)

    def _build_graph(self):
        graph = StateGraph(EngagementState)
        graph.add_node("load_movie_context", load_movie_context)
        graph.add_node("load_user_profile", load_user_profile)
        graph.add_node("maybe_load_trend_context", maybe_load_trend_context)
        graph.add_node("generate_teaser_question", generate_teaser_question)
        graph.add_node("generate_fun_fact_answer", generate_fun_fact_answer)
        graph.add_node("generate_why_watch_now", generate_why_watch_now)
        graph.add_node("maybe_generate_hook", maybe_generate_hook)
        graph.add_node("compose_response", compose_response)

        graph.add_edge(START, "load_movie_context")
        graph.add_edge(START, "load_user_profile")
        graph.add_edge("load_movie_context", "maybe_load_trend_context")
        graph.add_edge("load_user_profile", "maybe_load_trend_context")
        graph.add_edge("maybe_load_trend_context", "generate_teaser_question")
        graph.add_edge("maybe_load_trend_context", "generate_fun_fact_answer")
        graph.add_edge("maybe_load_trend_context", "generate_why_watch_now")
        graph.add_edge("generate_teaser_question", "maybe_generate_hook")
        graph.add_edge("generate_fun_fact_answer", "maybe_generate_hook")
        graph.add_edge("generate_why_watch_now", "maybe_generate_hook")
        graph.add_edge("maybe_generate_hook", "compose_response")
        graph.add_edge("compose_response", END)
        return graph.compile()
