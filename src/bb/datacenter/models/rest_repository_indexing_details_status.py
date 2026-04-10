from enum import Enum


class RestRepositoryIndexingDetailsStatus(str, Enum):
    BROKEN = "BROKEN"
    INDEXED = "INDEXED"
    INDEXING = "INDEXING"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
