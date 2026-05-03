# cortex-cinema

Minimal project skeleton for the `Engagement Agent v1.0.0` backend described in the solution design.

## What this scaffold includes

- `FastAPI` app with engagement, reveal, and feedback endpoints
- `LangGraph` orchestration boundary with explicit node modules
- service-layer stubs for `TMDB`, user-profile, and trend enrichment
- shared LLM gateway and prompt files for generation responsibilities
- composition helpers for ranking, repeat avoidance, and validation
- YAML config and in-memory cache/storage placeholders

## Quick start

```bash
just setup
just run
```

Then open:

- `GET /v1/movies/550/engagement?userId=user_123&includeHook=true`
- Swagger UI at `/docs`
- ReDoc at `/redoc`
- Raw OpenAPI spec at `/openapi.json`

Available local commands:

- `just setup` to create the `uv` virtualenv and sync dependencies
- `just run` to start the FastAPI app
- `just run-compose` to run the app in Docker Compose
- `just check` to run a lightweight Python compile check
- `just test-local` to build with Docker Compose and run the end-to-end smoke test

The API documentation is generated from the FastAPI `OpenAPI` schema, so the route definitions and Pydantic models are the source of truth for:

- request and response schemas
- field descriptions
- example payloads
- Swagger UI and ReDoc rendering

## Notes

- The scaffold is intentionally minimal and does not include real external integrations yet.
- The current placeholder logic is deterministic so the route shape and orchestration flow can be exercised before wiring OpenAI, Redis, or PostgreSQL.
- Additional context is in `docs/engagement-agent-skeleton.md`.

## Local Docker Compose E2E

Build and run the full local smoke path with Docker Compose:

```bash
just test-local
```

This script:

- builds the local Docker image with `uv`
- installs the app inside the container with `uv` into `/app/.venv`
- starts the API with Docker Compose
- runs a smoke-test container that calls `/healthz` and the engagement endpoint

Key files:

- `Justfile`
- `Dockerfile`
- `docker-compose.yml`
- `scripts/run_local_e2e.sh`
