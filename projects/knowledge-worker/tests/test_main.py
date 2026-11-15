from app.main import (
    main,
)
from app.models.report_metadata import (
    ReportMetadata,
)


def test_main_without_arguments(
    capsys,
):

    main([])

    captured = (
        capsys.readouterr()
    )

    assert "Usage" in captured.out


def test_main_topics(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_topics",
        lambda: {
            "fusion": 2,
            "energy": 1,
        },
    )

    main(
        ["--topics"]
    )

    captured = (
        capsys.readouterr()
    )

    assert "fusion" in captured.out

    assert "energy" in captured.out


def test_main_top_reports(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_top_reports",
        lambda: [
            ReportMetadata(
                filename="1.md",
                topic="Fusion Energy",
                score=95,
                grade="EXCELLENT",
            )
        ],
    )

    main(
        ["--top-reports"]
    )

    captured = (
        capsys.readouterr()
    )

    assert (
        "Fusion Energy"
        in captured.out
    )


def test_main_recommendations(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_recommendations",
        lambda limit=3: [
            "energy",
            "fusion",
            "storage",
        ],
    )

    main(
        ["--recommendations"]
    )

    captured = (
        capsys.readouterr()
    )

    assert "energy" in captured.out

    assert "fusion" in captured.out


def test_main_recommendations_with_limit(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_recommendations",
        lambda limit=3: [
            "energy",
            "fusion",
        ],
    )

    main(
        [
            "--recommendations",
            "2",
        ]
    )

    captured = (
        capsys.readouterr()
    )

    assert "energy" in captured.out

    assert "fusion" in captured.out


def test_main_top_topics(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_top_topics",
        lambda: [
            ("energy", 2),
            ("fusion", 2),
            ("storage", 1),
        ],
    )

    main(
        ["--top-topics"]
    )

    captured = (
        capsys.readouterr()
    )

    assert "TOP TOPICS" in captured.out

    assert "energy" in captured.out

    assert "fusion" in captured.out


def test_main_unknown_command(
    capsys,
):

    main(
        ["--unknown"]
    )

    captured = (
        capsys.readouterr()
    )

    assert (
        "Unknown command"
        in captured.out
    )
    
def test_main_related(
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "app.main.KnowledgeService.get_related_reports",
        lambda topic: [
            ReportMetadata(
                filename="related.md",
                topic="Fusion Energy Research",
                score=85,
                grade="GOOD",
            )
        ],
    )

    main(
        [
            "--related",
            "Fusion Energy",
        ]
    )

    captured = (
        capsys.readouterr()
    )

    assert (
        "Fusion Energy Research"
        in captured.out
    )    