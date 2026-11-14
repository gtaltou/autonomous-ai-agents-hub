class TopTopicsAnalyzer:
    
    @classmethod
    def get_top_topics(
        cls,
        topics: dict[str, int],
        limit: int = 10,
    ) -> list[tuple[str, int]]:

        if not isinstance(
            limit,
            int,
        ):
            raise TypeError(
                "limit must be an integer",
            )

        if limit < 1:
            raise ValueError(
                "limit must be greater than 0",
            )

        return sorted(
            topics.items(),
            key=lambda item: item[1],
            reverse=True,
        )[:limit]