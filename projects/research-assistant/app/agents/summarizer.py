from agents import Agent

from app.models import SummaryResult


def build_summarizer_agent() -> Agent:

    return Agent(
        name="Research Summarizer Agent",
        instructions="""
        You are a research summarization specialist.

        Analyze the findings provided.

        Return:

        - summary
        - key_points
        - confidence_score

        Always return a valid SummaryResult.
        """,
        output_type=SummaryResult,
    )
