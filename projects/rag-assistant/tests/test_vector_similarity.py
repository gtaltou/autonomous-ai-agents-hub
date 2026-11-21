from app.vectorstore.vector_similarity import (
    cosine_similarity,
)


def test_identical_vectors() -> None:
    result = cosine_similarity(
        [1.0, 0.0],
        [1.0, 0.0],
    )

    assert result == 1.0


def test_different_vectors() -> None:
    result = cosine_similarity(
        [1.0, 0.0],
        [0.0, 1.0],
    )

    assert result == 0.0


def test_zero_vector() -> None:
    result = cosine_similarity(
        [0.0, 0.0],
        [1.0, 0.0],
    )

    assert result == 0.0
