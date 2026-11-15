from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class TopicCount(BaseModel):
    topic: str
    count: int


class RecommendationResponse(BaseModel):
    recommendations: list[str]