from enum import Enum


class RestPullRequestAuthorRole(str, Enum):
    AUTHOR = "AUTHOR"
    PARTICIPANT = "PARTICIPANT"
    REVIEWER = "REVIEWER"

    def __str__(self) -> str:
        return str(self.value)
