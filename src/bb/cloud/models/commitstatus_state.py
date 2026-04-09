from enum import StrEnum


class CommitstatusState(StrEnum):
    FAILED = "FAILED"
    INPROGRESS = "INPROGRESS"
    STOPPED = "STOPPED"
    SUCCESSFUL = "SUCCESSFUL"
