from agents import Agent

from app.models import (
    ResearchReport,
)


def build_fact_checker_agent() -> Agent:
    """
    Agent responsible for reviewing and
    validating research findings.
    """

    return Agent(
        name="Research Fact Checker Agent",
        instructions="""
        You are responsible for validating
        research findings.

        Review information carefully.

        Look for:

        - inconsistencies
        - unsupported claims
        - missing context
        - factual accuracy

        Produce a complete research report.

        Return:

        - topic
        - executive_summary
        - key_findings
        - sources_reviewed
        - fact_check_notes
        - final_conclusion

        Always return a valid ResearchReport.
        """,
        output_type=ResearchReport,
    )