from enum import Enum


class RestDiffLineConflictMarker(str, Enum):
    MARKER = "MARKER"
    OURS = "OURS"
    THEIRS = "THEIRS"

    def __str__(self) -> str:
        return str(self.value)
