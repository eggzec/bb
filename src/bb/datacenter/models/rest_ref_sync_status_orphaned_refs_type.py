from enum import Enum


class RestRefSyncStatusOrphanedRefsType(str, Enum):
    BRANCH = "BRANCH"
    TAG = "TAG"

    def __str__(self) -> str:
        return str(self.value)
