from fastapi import FastAPI, HTTPException

from app.repositories.report_repository import ReportRepository
from app.services.knowledge_service import (
    KnowledgeService,
)

app = FastAPI(
    title="Knowledge Worker API",
    version="1.2.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
    }


@app.get("/topics")
def get_topics() -> dict[str, int]:
    return (
        KnowledgeService
        .get_topics()
    )


@app.get("/top-topics")
def get_top_topics():
    return (
        KnowledgeService
        .get_top_topics()
    )
    

@app.get("/recommendations")
def get_recommendations():
    return (
        KnowledgeService
        .get_recommendations()
    )
    
@app.get("/top-reports")
def get_top_reports():
    return (
        KnowledgeService
        .get_top_reports()
    )
    
@app.get("/related/{topic}")
def get_related_reports(
    topic: str,
):

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