from enum import Enum


class RestPullRequestParticipantStatus(str, Enum):
    APPROVED = "APPROVED"
    NEEDS_WORK = "NEEDS_WORK"
    UNAPPROVED = "UNAPPROVED"

    def __str__(self) -> str:
        return str(self.value)
