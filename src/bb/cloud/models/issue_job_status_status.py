from enum import StrEnum


class IssueJobStatusStatus(StrEnum):
    ACCEPTED = "ACCEPTED"
    FAILURE = "FAILURE"
    RUNNING = "RUNNING"
    STARTED = "STARTED"
