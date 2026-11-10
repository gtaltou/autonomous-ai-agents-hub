from agents import Agent


def build_summarizer_agent() -> Agent:
    """
    Agent responsible for synthesizing
    research findings into concise,
    structured summaries.
    """

    return Agent(
        name="Research Summarizer Agent",
        instructions="""
        You are a research summarization specialist.

        Your responsibility is to transform
        research findings into clear and
        concise summaries.

        Focus on:

        - key insights
        - major findings
        - relevance
        - clarity
        - accuracy

        Avoid unnecessary details.

        Produce structured and actionable
        summaries suitable for research reports.
        """,
    )