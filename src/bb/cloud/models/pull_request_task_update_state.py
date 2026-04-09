from enum import StrEnum


class PullRequestTaskUpdateState(StrEnum):
    RESOLVED = "RESOLVED"
    UNRESOLVED = "UNRESOLVED"
