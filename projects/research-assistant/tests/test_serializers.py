from app.models import (
    SearchResult,
    SummaryResult,
)
from app.serializers.research import (
    search_result_to_prompt,
    summary_result_to_prompt,
)


def test_search_result_serializer():

    result = SearchResult(
        topic="Quantum Computing",
        findings=[
            "Finding 1",
            "Finding 2",
        ],
        source_count=2,
    )

    prompt = search_result_to_prompt(
        result
    )

    assert "Quantum Computing" in prompt
    assert "Finding 1" in prompt
    assert "Finding 2" in prompt


def test_summary_result_serializer():

    result = SummaryResult(
        summary="Summary",
        key_points=[
            "Point 1",
            "Point 2",
        ],
        confidence_score=0.90,
    )

    prompt = summary_result_to_prompt(
        result
    )

    assert "Summary" in prompt
    assert "Point 1" in prompt
    assert "Point 2" in prompt