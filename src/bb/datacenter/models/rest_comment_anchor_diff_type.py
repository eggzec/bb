from enum import Enum


class RestCommentAnchorDiffType(str, Enum):
    COMMIT = "COMMIT"
    EFFECTIVE = "EFFECTIVE"
    RANGE = "RANGE"

    def __str__(self) -> str:
        return str(self.value)
