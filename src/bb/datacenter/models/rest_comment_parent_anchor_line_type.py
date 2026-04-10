from enum import Enum


class RestCommentParentAnchorLineType(str, Enum):
    ADDED = "ADDED"
    CONTEXT = "CONTEXT"
    REMOVED = "REMOVED"

    def __str__(self) -> str:
        return str(self.value)
