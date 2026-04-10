from enum import Enum


class RestRefSyncStatusOrphanedRefsState(str, Enum):
    AHEAD = "AHEAD"
    DIVERGED = "DIVERGED"
    ORPHANED = "ORPHANED"

    def __str__(self) -> str:
        return str(self.value)
