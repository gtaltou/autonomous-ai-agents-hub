import pytest

from app.analyzers.top_topics import (
    TopTopicsAnalyzer,
)


def test_get_top_topics():

    topics = {
        "energy": 2,
        "fusion": 2,
        "storage": 1,
        "research": 1,
    }

    results = (
        TopTopicsAnalyzer
        .get_top_topics(
            topics,
        )
    )

    assert len(results) == 4

    assert results[0][1] >= results[1][1]


def test_get_top_topics_limit():

    topics = {
        "energy": 2,
        "fusion": 2,
        "storage": 1,
        "research": 1,
    }

    results = (
        TopTopicsAnalyzer
        .get_top_topics(
            topics,
            limit=2,
        )
    )

    assert len(results) == 2


def test_get_top_topics_large_limit():

    topics = {
        "energy": 2,
        "fusion": 2,
    }

    results = (
        TopTopicsAnalyzer
        .get_top_topics(
            topics,
            limit=10,
        )
    )

    assert len(results) == 2


def test_get_top_topics_limit_zero():

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):
        TopTopicsAnalyzer.get_top_topics(
            {},
            limit=0,
        )


def test_get_top_topics_negative_limit():

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):
        TopTopicsAnalyzer.get_top_topics(
            {},
            limit=-1,
        )


def test_get_top_topics_string_limit():

    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):
        TopTopicsAnalyzer.get_top_topics(
            {},
            limit="5",
        )