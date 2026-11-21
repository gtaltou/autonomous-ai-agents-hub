from typing import Protocol


class LLMInterface(Protocol):
    def generate(
        self,
        question: str,
        context: str,
    ) -> str: ...
