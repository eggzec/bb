from enum import Enum


class RestCommentAnchorPullRequestToRefRepositoryState(str, Enum):
    AVAILABLE = "AVAILABLE"
    INITIALISATION_FAILED = "INITIALISATION_FAILED"
    INITIALISING = "INITIALISING"
    OFFLINE = "OFFLINE"

    def __str__(self) -> str:
        return str(self.value)
