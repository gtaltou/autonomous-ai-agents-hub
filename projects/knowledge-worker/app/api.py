from fastapi import (
    FastAPI,
    HTTPException,
)

from app.models.api_models import (
    HealthResponse,
    RecommendationResponse,
    TopicCount,
)
from app.models.report_metadata import (
    ReportMetadata,
)
from app.repositories.report_repository import (
    ReportRepository,
)
from app.services.knowledge_service import (
    KnowledgeService,
)

app = FastAPI(
    title="Knowledge Worker API",
    description=(
        "REST API for analyzing markdown-based reports and "
        "extracting organizational knowledge."
    ),
    version="1.2.0",
)


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["System"],
    summary="Health check",
    description="Returns the API health status.",
)
def health() -> HealthResponse:

    return HealthResponse(
        status="ok",
    )


@app.get(
    "/topics",
    response_model=dict[str, int],
    tags=["Knowledge"],
    summary="Discover topics",
    description=(
        "Returns all discovered topics and their occurrence count."
    ),
)
def get_topics() -> dict[str, int]:

    return (
        KnowledgeService
        .get_topics()
    )


@app.get(
    "/top-topics",
    response_model=list[TopicCount],
    tags=["Knowledge"],
    summary="Get top topics",
    description=(
        "Returns the most frequently occurring topics ranked by popularity."
    ),
)
def get_top_topics() -> list[TopicCount]:

    return [
        TopicCount(
            topic=topic,
            count=count,
        )
        for topic, count in (
            KnowledgeService
            .get_top_topics()
        )
    ]


@app.get(
    "/recommendations",
    response_model=RecommendationResponse,
    tags=["Knowledge"],
    summary="Get recommendations",
    description=(
        "Returns recommended future research topics based on existing reports."
    ),
)
def get_recommendations() -> RecommendationResponse:

    return RecommendationResponse(
        recommendations=(
            KnowledgeService
            .get_recommendations()
        )
    )


@app.get(
    "/top-reports",
    response_model=list[ReportMetadata],
    tags=["Reports"],
    summary="Get top reports",
    description=(
        "Returns the highest-scoring reports ranked by quality."
    ),
)
def get_top_reports() -> list[ReportMetadata]:

    return (
        KnowledgeService
        .get_top_reports()
    )


@app.get(
    "/related/{topic}",
    response_model=list[ReportMetadata],
    tags=["Reports"],
    summary="Get related reports",
    description=(
        "Returns reports related to the specified topic."
    ),
)
def get_related_reports(
    topic: str,
) -> list[ReportMetadata]:

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    target = next(
        (
            report
            for report in reports
            if report.topic.lower()
            == topic.lower()
        ),
        None,
    )

    if target is None:

        raise HTTPException(
            status_code=404,
            detail="Topic not found.",
        )

    return (
        KnowledgeService
        .get_related_reports(
            target,
        )
    )