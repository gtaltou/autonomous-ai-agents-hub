from app.models import Person


def evaluate_person(
    expected: Person,
    actual: Person,
) -> bool:
    """
    Compare an expected Person object with an actual Person object.
    """

    return (
        expected.name == actual.name
        and expected.age == actual.age
        and expected.city == actual.city
    )