from app.evaluator import evaluate_person
from app.models import Person


def test_evaluation_success():

    expected = Person(
        name="John Doe",
        age=42,
        city="Paris",
    )

    actual = Person(
        name="John Doe",
        age=42,
        city="Paris",
    )

    assert evaluate_person(
        expected,
        actual,
    )


def test_evaluation_failure():

    expected = Person(
        name="John Doe",
        age=42,
        city="Paris",
    )

    actual = Person(
        name="John Doe",
        age=43,
        city="Paris",
    )

    assert not evaluate_person(
        expected,
        actual,
    )