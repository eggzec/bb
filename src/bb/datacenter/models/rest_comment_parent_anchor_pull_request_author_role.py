from enum import Enum


class RestCommentParentAnchorPullRequestAuthorRole(str, Enum):
    AUTHOR = "AUTHOR"
    PARTICIPANT = "PARTICIPANT"
    REVIEWER = "REVIEWER"

    def __str__(self) -> str:
        return str(self.value)
