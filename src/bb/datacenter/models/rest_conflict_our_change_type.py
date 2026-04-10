from enum import Enum


class RestConflictOurChangeType(str, Enum):
    ADD = "ADD"
    COPY = "COPY"
    DELETE = "DELETE"
    MODIFY = "MODIFY"
    MOVE = "MOVE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
