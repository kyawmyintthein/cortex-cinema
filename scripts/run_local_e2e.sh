#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cleanup() {
  docker compose -f "${REPO_ROOT}/docker-compose.yml" down --remove-orphans >/dev/null 2>&1 || true
}

trap cleanup EXIT

echo "Building and starting app with Docker Compose"
docker compose -f "${REPO_ROOT}/docker-compose.yml" up --build -d app

echo "Running end-to-end smoke test container"
docker compose -f "${REPO_ROOT}/docker-compose.yml" run --rm e2e

echo "Local Docker Compose end-to-end test passed"
