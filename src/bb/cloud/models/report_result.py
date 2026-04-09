from enum import StrEnum


class ReportResult(StrEnum):
    FAILED = "FAILED"
    PASSED = "PASSED"
    PENDING = "PENDING"
