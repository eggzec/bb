from enum import Enum


class RestChangeType(str, Enum):
    ADD = "ADD"
    COPY = "COPY"
    DELETE = "DELETE"
    MODIFY = "MODIFY"
    MOVE = "MOVE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
