from enum import StrEnum


class GetPipelinesForRepositoryStatus(StrEnum):
    BUILDING = "BUILDING"
    ERROR = "ERROR"
    FAILED = "FAILED"
    HALTED = "HALTED"
    PARSING = "PARSING"
    PASSED = "PASSED"
    PAUSED = "PAUSED"
    PENDING = "PENDING"
    STOPPED = "STOPPED"
    UNKNOWN = "UNKNOWN"
