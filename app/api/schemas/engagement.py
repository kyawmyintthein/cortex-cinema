from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class EngagementQueryParams(BaseModel):
    user_id: str | None = None
    include_hook: bool = False
    client_platform: str | None = None
    locale: str | None = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "userId": "user_123",
                "includeHook": True,
                "clientPlatform": "ios",
                "locale": "en-US",
            }
        }
    )


class EngagementContent(BaseModel):
    teaser_question: str = Field(alias="teaserQuestion")
    fun_fact_answer: str = Field(alias="funFactAnswer")
    why_watch_now: str = Field(alias="whyWatchNow")
    hook: str | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "teaserQuestion": "Why has this movie stayed such a strong recommendation magnet?",
                "funFactAnswer": "It keeps resurfacing because its style, scale, and discussion value give people a lot to compare notes on after watching.",
                "whyWatchNow": "You have been leaning into sci-fi lately, and this fits that mood well.",
                "hook": "A strong pick when you want something easy to talk about afterward.",
            }
        },
    )


class EngagementMetadata(BaseModel):
    personalized: bool
    trend_used: bool = Field(alias="trendUsed")
    fallback_used: bool = Field(alias="fallbackUsed")
    hook_included: bool = Field(alias="hookIncluded")
    fact_id: str = Field(alias="factId")
    version: str
    cache_hit: bool = Field(default=False, alias="cacheHit")

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "personalized": True,
                "trendUsed": True,
                "fallbackUsed": False,
                "hookIncluded": True,
                "factId": "fact_002",
                "version": "v1.0.0",
                "cacheHit": False,
            }
        },
    )


class EngagementResponse(BaseModel):
    movie_id: int = Field(alias="movieId")
    engagement: EngagementContent
    metadata: EngagementMetadata

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "movieId": 550,
                "engagement": {
                    "teaserQuestion": "Why has this movie stayed such a strong recommendation magnet?",
                    "funFactAnswer": "It keeps resurfacing because its style, scale, and discussion value give people a lot to compare notes on after watching.",
                    "whyWatchNow": "You have been leaning into sci-fi lately, and this fits that mood well.",
                    "hook": "A strong pick when you want something easy to talk about afterward.",
                },
                "metadata": {
                    "personalized": True,
                    "trendUsed": True,
                    "fallbackUsed": False,
                    "hookIncluded": True,
                    "factId": "fact_002",
                    "version": "v1.0.0",
                    "cacheHit": False,
                },
            }
        },
    )


class EngagementRevealRequest(BaseModel):
    user_id: str = Field(alias="userId")
    fact_id: str = Field(alias="factId")
    revealed_at: datetime = Field(alias="revealedAt")

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "userId": "user_123",
                "factId": "fact_002",
                "revealedAt": "2026-05-01T10:30:00Z",
            }
        },
    )


class EngagementFeedbackRequest(BaseModel):
    user_id: str = Field(alias="userId")
    fact_id: str = Field(alias="factId")
    feedback: Literal["helpful", "not_helpful"]

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "userId": "user_123",
                "factId": "fact_002",
                "feedback": "helpful",
            }
        },
    )


class AcceptedResponse(BaseModel):
    status: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "accepted",
            }
        }
    )
