from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app

pytestmark = pytest.mark.integration

client = TestClient(
    app,
)

    

def list_reports(
    cls,
) -> list[Path]:

    if (
        not cls.REPORTS_DIR.exists()
        or not cls.REPORTS_DIR.is_dir()
    ):

        return []

    return sorted(
        cls.REPORTS_DIR.glob(
            "*.md"
        )
    )
  
        
def test_api_workflow():
    
    health_response = client.get(
        "/health",
    )

    assert (
        health_response.status_code
        == 200
    )

    topics_response = client.get(
        "/topics",
    )

    assert (
        topics_response.status_code
        == 200
    )

    topics = (
        topics_response.json()
    )

    assert len(
        topics
    ) > 0

    top_topics_response = client.get(
        "/top-topics",
    )

    assert (
        top_topics_response.status_code
        == 200
    )

    top_topics = (
        top_topics_response.json()
    )

    assert len(
        top_topics
    ) > 0

    reports_response = client.get(
        "/top-reports",
    )

    assert (
        reports_response.status_code
        == 200
    )

    reports = (
        reports_response.json()
    )

    assert len(
        reports
    ) > 0

    recommendations_response = client.get(
        "/recommendations",
    )

    assert (
        recommendations_response.status_code
        == 200
    )

    recommendations = (
        recommendations_response.json()
    )

    assert (
        "recommendations"
        in recommendations
    )

    assert len(
        recommendations[
            "recommendations"
        ]
    ) > 0

    related_response = client.get(
        "/related/Fusion Energy",
    )

    assert (
        related_response.status_code
        == 200
    )

    related_reports = (
        related_response.json()
    )

    assert len(
        related_reports
    ) > 0          