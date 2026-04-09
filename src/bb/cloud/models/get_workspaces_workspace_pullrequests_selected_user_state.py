from enum import StrEnum


class GetWorkspacesWorkspacePullrequestsSelectedUserState(StrEnum):
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPEN = "OPEN"
    SUPERSEDED = "SUPERSEDED"
