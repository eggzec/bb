from enum import Enum


class GetRepositories1State(str, Enum):
    AVAILABLE = "AVAILABLE"
    INITIALISATION_FAILED = "INITIALISATION_FAILED"
    INITIALISING = "INITIALISING"

    def __str__(self) -> str:
        return str(self.value)
