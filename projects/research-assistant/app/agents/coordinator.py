from agents import Agent

from app.models import ResearchReport


def build_coordinator_agent() -> Agent:
    """
    Main orchestration agent for the
    Research Assistant workflow.
    """

    return Agent(
        name="Research Coordinator",
        instructions="""
        You are responsible for coordinating
        the research workflow.

        Analyze the user's question.

        Produce a structured research report.

        Focus on:
        - Topic identification
        - Information synthesis
        - Key findings
        - Final conclusion

        Always return a valid ResearchReport.
        """,
        output_type=ResearchReport,
    )