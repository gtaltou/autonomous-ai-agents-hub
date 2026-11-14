from dataclasses import dataclass


@dataclass
class ReportMetadata:

    filename: str
    topic: str
    score: int
    grade: str