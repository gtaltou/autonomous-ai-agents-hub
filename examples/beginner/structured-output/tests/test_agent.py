from app.agent import build_agent
from app.models import Person


def test_agent_name():

    agent = build_agent()

    assert agent.name == "Person Extractor"


def test_agent_output_type():

    agent = build_agent()

    assert agent.output_type == Person