from app.analyzers.topic_discovery import (
    TopicDiscoveryAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)


def test_discover_topics():

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
        ReportMetadata(
            filename="3.md",
            topic="Energy Storage",
            score=75,
            grade="GOOD",
        ),
    ]

    topics = (
        TopicDiscoveryAnalyzer
        .discover_topics(
            reports
        )
    )

    assert topics["fusion"] == 2

    assert topics["energy"] == 2

    assert topics["research"] == 1

    assert topics["storage"] == 1
    
def test_discover_topics_empty_list():
    
    topics = (
        TopicDiscoveryAnalyzer
        .discover_topics(
            []
        )
    )

    assert topics == {}
    
def test_discover_topics_case_insensitive():
    
    reports = [
        ReportMetadata(
            filename="1.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        ),
        ReportMetadata(
            filename="2.md",
            topic="fusion energy",
            score=80,
            grade="GOOD",
        ),
    ]

    topics = (
        TopicDiscoveryAnalyzer
        .discover_topics(
            reports
        )
    )

    assert topics["fusion"] == 2

    assert topics["energy"] == 2      