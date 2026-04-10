from enum import Enum


class CommentSeverity(str, Enum):
    BLOCKER = "BLOCKER"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
