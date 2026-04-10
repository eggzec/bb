from enum import Enum


class RestCommentAnchorPullRequestAuthorUserType(str, Enum):
    NORMAL = "NORMAL"
    SERVICE = "SERVICE"

    def __str__(self) -> str:
        return str(self.value)
