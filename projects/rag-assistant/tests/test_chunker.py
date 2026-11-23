from app.chunking.text_chunker import chunk_text


def test_chunk_text_returns_chunks():
    text = "A" * 1200

    chunks = chunk_text(
        text=text,
        source_document="test.txt",
        chunk_size=500,
    )

    assert len(chunks) == 3


def test_chunk_ids_are_sequential():
    text = "A" * 1200

    chunks = chunk_text(
        text=text,
        source_document="test.txt",
        chunk_size=500,
    )

    assert chunks[0].chunk_id == 0
    assert chunks[1].chunk_id == 1
    assert chunks[2].chunk_id == 2


def test_empty_text_returns_empty_list():
    chunks = chunk_text(
        text="",
        source_document="test.txt",
    )

    assert chunks == []
