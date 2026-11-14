from app.analyzers.recommendations import (
    RecommendationsAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)


def test_get_recommendations():

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

    recommendations = (
        RecommendationsAnalyzer
        .get_recommendations(
            reports,
        )
    )

    assert "fusion" in recommendations
    assert "energy" in recommendations
    
    def test_get_recommendations_sorted():
    
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

    recommendations = (
        RecommendationsAnalyzer
        .get_recommendations(
            reports,
        )
    )

    assert recommendations[0] in {
        "fusion",
        "energy",
    }