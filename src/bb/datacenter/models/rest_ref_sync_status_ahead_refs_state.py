from enum import Enum


class RestRefSyncStatusAheadRefsState(str, Enum):
    AHEAD = "AHEAD"
    DIVERGED = "DIVERGED"
    ORPHANED = "ORPHANED"

    def __str__(self) -> str:
        return str(self.value)
