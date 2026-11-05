from app.models import Person


def test_person_model():

    person = Person(
        name="John Doe",
        age=42,
        city="Paris",
    )

    assert person.name == "John Doe"
    assert person.age == 42
    assert person.city == "Paris"