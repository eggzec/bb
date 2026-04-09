from enum import StrEnum


class IssueKind(StrEnum):
    BUG = "bug"
    ENHANCEMENT = "enhancement"
    PROPOSAL = "proposal"
    TASK = "task"
