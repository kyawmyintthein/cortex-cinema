# Engagement Agent Skeleton

This scaffold turns the solution design into a minimal backend layout with clear module boundaries.

## Included

- FastAPI entrypoint and `/v1/movies/{tmdbId}/engagement` routes
- LangGraph orchestrator with explicit state and node modules
- service boundaries for TMDB, user profile, and trend enrichment
- LLM gateway and prompt placeholders for teaser, fact, why-watch, and hook generation
- composition helpers for ranking, repeat avoidance, and validation
- in-memory cache and repository placeholders to keep the skeleton runnable
- YAML configuration aligned to the repository defaults

## Intentionally Deferred

- real TMDB, OpenAI, Redis, PostgreSQL, and analytics integrations
- authentication and authorization
- Alembic migrations and SQLAlchemy models
- background queue processing for feedback or event fan-out
- production-grade observability and moderation

## Design Notes

- The skeleton keeps orchestration narrow and deterministic rather than introducing a broader agent swarm.
- Generation is stubbed behind `app/llm/gateway.py` so the OpenAI integration can replace placeholders without changing route or graph structure.
- Repositories and cache are process-local on purpose. They mark the contracts that would later move to PostgreSQL and Redis.
- The route layer stays thin and keeps reveal-history writes out of the `GET` path, matching the solution design.
