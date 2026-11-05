from agents import Agent

from app.models import Person


def build_agent() -> Agent:

    return Agent(
        name="Person Extractor",
        instructions="""
        Extract structured information from the provided text.

        Return:
        - name
        - age
        - city

        If information is missing, make your best effort based on
        the provided content.

        Always return a valid Person object.
        """,
        output_type=Person,
    )
