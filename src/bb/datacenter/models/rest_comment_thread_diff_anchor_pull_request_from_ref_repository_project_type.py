from enum import Enum


class RestCommentThreadDiffAnchorPullRequestFromRefRepositoryProjectType(str, Enum):
    NORMAL = "NORMAL"
    PERSONAL = "PERSONAL"

    def __str__(self) -> str:
        return str(self.value)
