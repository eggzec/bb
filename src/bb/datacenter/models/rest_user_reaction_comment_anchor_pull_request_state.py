from enum import Enum


class RestUserReactionCommentAnchorPullRequestState(str, Enum):
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
