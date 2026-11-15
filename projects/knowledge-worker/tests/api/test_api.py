import pytest
from fastapi.testclient import TestClient

from app.api import app

client = TestClient(
    app,
)

@pytest.mark.api
def test_health():

    response = client.get(
        "/health",
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()
        == {
            "status": "ok",
        }
    )

@pytest.mark.api
def test_topics():

    response = client.get(
        "/topics",
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        dict,
    )
    
@pytest.mark.api    
def test_top_topics():
    
    response = client.get(
        "/top-topics",
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )

    assert len(
        response.json()
    ) > 0 
    
@pytest.mark.api  
def test_recommendations():
    
    response = client.get(
        "/recommendations",
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        "recommendations"
        in data
    )

    assert isinstance(
        data["recommendations"],
        list,
    )

    assert len(
        data["recommendations"]
    ) > 0
     
@pytest.mark.api 
def test_top_reports():
    
    response = client.get(
        "/top-reports",
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )

    assert len(
        response.json()
    ) > 0
    
@pytest.mark.api 
def test_related_reports():
    
    response = client.get(
        "/related/Fusion Energy",
    )

    assert (
        response.status_code
        == 200
    )

    assert isinstance(
        response.json(),
        list,
    )

    assert len(
        response.json()
    ) > 0 
    
@pytest.mark.api
def test_related_reports_not_found():
    
    response = client.get(
        "/related/unknown-topic",
    )

    assert (
        response.status_code
        == 404
    )
    
