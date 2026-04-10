from enum import Enum


class RestUserReactionCommentAnchorPullRequestAuthorRole(str, Enum):
    AUTHOR = "AUTHOR"
    PARTICIPANT = "PARTICIPANT"
    REVIEWER = "REVIEWER"

    def __str__(self) -> str:
        return str(self.value)
