import pytest

from app.analyzers.recommendations import (
    RecommendationsAnalyzer,
)
from app.analyzers.topic_discovery import (
    TopicDiscoveryAnalyzer,
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


def test_discover_topics_ignores_stop_words():
    reports = [
        ReportMetadata(
            filename="1.md",
            topic="The Future of Energy",
            score=95,
            grade="EXCELLENT",
        ),
    ]

    topics = (
        TopicDiscoveryAnalyzer
        .discover_topics(
            reports
        )
    )

    assert "the" not in topics
    assert "of" not in topics
    
def test_get_recommendations_limit():
    
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
            limit=2,
        )
    )

    assert len(recommendations) == 2
    
def test_get_recommendations_large_limit():
    
    reports = [
        ReportMetadata(
            filename="1.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        ),
    ]

    recommendations = (
        RecommendationsAnalyzer
        .get_recommendations(
            reports,
            limit=10,
        )
    )

    assert len(recommendations) == 2
    
def test_get_recommendations_limit_zero():
    
    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        RecommendationsAnalyzer.get_recommendations(
            [],
            limit=0,
        )
        
def test_get_recommendations_negative_limit():
    
    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        RecommendationsAnalyzer.get_recommendations(
            [],
            limit=-1,
        )
        
def test_get_recommendations_string_limit():
    
    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):

        RecommendationsAnalyzer.get_recommendations(
            [],
            limit="5",
        )
       
                      