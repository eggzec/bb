from enum import Enum


class RestRepositoryPolicyPermission(str, Enum):
    ADMIN = "ADMIN"
    PROJECT_ADMIN = "PROJECT_ADMIN"
    REPO_ADMIN = "REPO_ADMIN"
    SYS_ADMIN = "SYS_ADMIN"

    def __str__(self) -> str:
        return str(self.value)
