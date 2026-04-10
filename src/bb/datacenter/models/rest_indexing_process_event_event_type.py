from enum import Enum


class RestIndexingProcessEventEventType(str, Enum):
    OTHER = "OTHER"
    PROJECT = "PROJECT"
    REPOSITORY = "REPOSITORY"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
