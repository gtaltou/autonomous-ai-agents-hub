from pydantic import BaseModel, Field


class Person(BaseModel):
    """
    Structured representation of a person.
    """

    name: str = Field(
        description="Full name of the person"
    )

    age: int = Field(
        ge=0,
        description="Age of the person"
    )

    city: str = Field(
        description="City where the person lives"
    )

