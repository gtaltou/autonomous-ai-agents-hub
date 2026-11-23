from app.llm.fake_llm import FakeLLM


def test_generate_response() -> None:
    llm = FakeLLM()

    response = llm.generate(
        context="Python is awesome",
        question="What is Python?",
    )

    assert "Python is awesome" in response
    assert "What is Python?" in response
