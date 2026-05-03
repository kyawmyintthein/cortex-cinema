from pydantic import BaseModel, Field


class FactCandidate(BaseModel):
    fact_id: str = Field(alias="factId")
    teaser_question: str = Field(alias="teaserQuestion")
    fun_fact_answer: str = Field(alias="funFactAnswer")
    trend_tags: list[str] = Field(default_factory=list, alias="trendTags")
    confidence: str
    source_type: str = Field(alias="sourceType")


class PromptInput(BaseModel):
    movie: dict
    user_summary: dict
    trend_summary: dict
