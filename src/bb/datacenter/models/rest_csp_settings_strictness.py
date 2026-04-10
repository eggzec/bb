from enum import Enum


class RestCspSettingsStrictness(str, Enum):
    DEFAULT = "DEFAULT"
    REPORT_ONLY = "REPORT_ONLY"
    STRICT = "STRICT"

    def __str__(self) -> str:
        return str(self.value)
