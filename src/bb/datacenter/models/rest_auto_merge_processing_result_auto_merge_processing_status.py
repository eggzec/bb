from enum import Enum


class RestAutoMergeProcessingResultAutoMergeProcessingStatus(str, Enum):
    CANCELLED = "CANCELLED"
    LOCK_FAILURE = "LOCK_FAILURE"
    MERGED = "MERGED"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"
    VETOED = "VETOED"

    def __str__(self) -> str:
        return str(self.value)
