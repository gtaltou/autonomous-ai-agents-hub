from datetime import datetime


class ExecutionLogger:

    @staticmethod
    def info(
        message: str,
    ) -> None:

        timestamp = (
            datetime.now()
            .isoformat(
                timespec="seconds"
            )
        )

        print(
            f"[INFO] "
            f"[{timestamp}] "
            f"{message}"
        )

    @staticmethod
    def warning(
        message: str,
    ) -> None:

        timestamp = (
            datetime.now()
            .isoformat(
                timespec="seconds"
            )
        )

        print(
            f"[WARN] "
            f"[{timestamp}] "
            f"{message}"
        )

    @staticmethod
    def error(
        message: str,
    ) -> None:

        timestamp = (
            datetime.now()
            .isoformat(
                timespec="seconds"
            )
        )

        print(
            f"[ERROR] "
            f"[{timestamp}] "
            f"{message}"
        )