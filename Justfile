set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

default:
    @just --list

setup:
    uv venv
    uv sync

run:
    uv run uvicorn app.main:app --reload

run-compose:
    docker compose up --build app

check:
    PYTHONPYCACHEPREFIX=/tmp/cortex-cinema-pycache uv run python -m compileall app

test-local:
    ./scripts/run_local_e2e.sh
