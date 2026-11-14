import pytest

from app.models.report_metadata import (
    ReportMetadata,
)
from app.services.knowledge_service import (
    KnowledgeService,
)


def test_get_top_reports_limit(
    monkeypatch,
):

    reports = [
        ReportMetadata(
            filename=f"{i}.md",
            topic=f"Topic {i}",
            score=i,
            grade="GOOD",
        )
        for i in range(10)
    ]

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: reports,
    )

    results = (
        KnowledgeService
        .get_top_reports(
            limit=3,
        )
    )

    assert len(results) == 3
    
 


def test_get_top_reports_invalid_limit(
    monkeypatch,
):

    reports = [
        ReportMetadata(
            filename="report.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        ),
    ]

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: reports,
    )

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        KnowledgeService.get_top_reports(
            limit=0,
        )
        

def test_get_top_reports_negative_limit(
    monkeypatch,
):

    reports = [
        ReportMetadata(
            filename="report.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        ),
    ]

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: reports,
    )

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        KnowledgeService.get_top_reports(
            limit=-3,
        )  
        
        
@classmethod
def get_top_reports(
    cls,
    reports: list[ReportMetadata],
    limit: int = 5,
) -> list[ReportMetadata]:

    if not isinstance(limit, int):

        raise TypeError(
            "limit must be an integer"
        )

    if limit < 1:

        raise ValueError(
            "limit must be greater than 0"
        )

    sorted_reports = sorted(
        reports,
        key=lambda report: report.score,
        reverse=True,
    )

    return sorted_reports[:limit]



def test_get_top_reports_string_limit(
    monkeypatch,
):

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: [],
    )

    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):

        KnowledgeService.get_top_reports(
            limit="5",
        )
        
def test_get_topics(
    monkeypatch,
):

    reports = [
        ReportMetadata(
            filename="1.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        ),
        ReportMetadata(
            filename="2.md",
            topic="Fusion Research",
            score=85,
            grade="GOOD",
        ),
    ]

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: reports,
    )

    topics = (
        KnowledgeService
        .get_topics()
    )

    assert topics["fusion"] == 2

    assert topics["energy"] == 1

    assert topics["research"] == 1
    
def test_get_topics_empty_repository(
    monkeypatch,
):

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: [],
    )

    topics = (
        KnowledgeService
        .get_topics()
    )

    assert topics == {} 
    
           