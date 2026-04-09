from enum import StrEnum


class PullrequestState(StrEnum):
    DECLINED = "DECLINED"
    DRAFT = "DRAFT"
    MERGED = "MERGED"
    OPEN = "OPEN"
    QUEUED = "QUEUED"
    SUPERSEDED = "SUPERSEDED"
