from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    name: str
    version: str
    environment: str


class FeatureConfig(BaseModel):
    trend_enrichment_enabled: bool
    hook_generation_enabled: bool


class CacheConfig(BaseModel):
    movie_context_ttl_seconds: int
    trend_context_ttl_seconds: int
    candidate_content_ttl_seconds: int
    final_response_ttl_seconds: int


class LLMConfig(BaseModel):
    model: str
    timeout_seconds: int
    max_retries: int


class Settings(BaseModel):
    app: AppConfig
    features: FeatureConfig
    cache: CacheConfig
    llm: LLMConfig


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    config_path = Path(__file__).resolve().parents[2] / "config" / "app.yaml"
    with config_path.open("r", encoding="utf-8") as config_file:
        payload = yaml.safe_load(config_file)
    return Settings.model_validate(payload)
