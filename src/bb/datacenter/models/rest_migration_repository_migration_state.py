from enum import Enum


class RestMigrationRepositoryMigrationState(str, Enum):
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    MIGRATED = "MIGRATED"
    QUEUED = "QUEUED"
    SKIPPED = "SKIPPED"
    STAGED = "STAGED"
    STAGING = "STAGING"

    def __str__(self) -> str:
        return str(self.value)
