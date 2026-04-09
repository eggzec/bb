from enum import StrEnum


class IssueState(StrEnum):
    CLOSED = "closed"
    DUPLICATE = "duplicate"
    INVALID = "invalid"
    NEW = "new"
    ON_HOLD = "on hold"
    OPEN = "open"
    RESOLVED = "resolved"
    SUBMITTED = "submitted"
    WONTFIX = "wontfix"
