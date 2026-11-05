from agents import Agent

from app.models import Person


def build_agent() -> Agent:
    """
    Build an agent that extracts structured
    person information from text.
    """

    return Agent(
        name="Person Evaluation Agent",
        instructions="""
        Extract structured information from the provided text.

        Return:
        - name
        - age
        - city

        Only extract information explicitly present in the text.

        Always return a valid Person object.
        """,
        output_type=Person,
    )