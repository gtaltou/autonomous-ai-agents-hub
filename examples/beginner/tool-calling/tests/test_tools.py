from app.tools import calculate


def test_addition():

    assert calculate("2+3") == "5"


def test_multiplication():

    assert calculate("10*5") == "50"


def test_division():

    assert calculate("100/4") == "25.0"