from enum import Enum


class RestInsightReportResult(str, Enum):
    FAIL = "FAIL"
    PASS = "PASS"

    def __str__(self) -> str:
        return str(self.value)
