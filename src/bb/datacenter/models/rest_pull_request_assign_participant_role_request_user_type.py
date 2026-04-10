from enum import Enum


class RestPullRequestAssignParticipantRoleRequestUserType(str, Enum):
    NORMAL = "NORMAL"
    SERVICE = "SERVICE"

    def __str__(self) -> str:
        return str(self.value)
