from enum import StrEnum


class ReportAnnotationResult(StrEnum):
    FAILED = "FAILED"
    IGNORED = "IGNORED"
    PASSED = "PASSED"
    SKIPPED = "SKIPPED"
