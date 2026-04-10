from enum import Enum


class RestPullRequestMergeabilityOutcome(str, Enum):
    CLEAN = "CLEAN"
    CONFLICTED = "CONFLICTED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
