from pydantic import BaseModel


class ReportMetadata(BaseModel):

    filename: str

    topic: str

    score: int

    grade: str