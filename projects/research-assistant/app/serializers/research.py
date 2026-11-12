from app.models import (
    SearchResult,
    SummaryResult,
)


def search_result_to_prompt(
    search_result: SearchResult,
) -> str:

    findings = "\n".join(
        search_result.findings
    )

    return f"""
Topic:
{search_result.topic}

Findings:
{findings}

Source Count:
{search_result.source_count}
"""


def summary_result_to_prompt(
    summary_result: SummaryResult,
) -> str:

    key_points = "\n".join(
        summary_result.key_points
    )

    return f"""
Summary:
{summary_result.summary}

Key Points:
{key_points}

Confidence Score:
{summary_result.confidence_score}
"""