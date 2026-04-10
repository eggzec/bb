from enum import Enum


class RestSshAccessKeyPermission(str, Enum):
    ADMIN = "ADMIN"
    LICENSED_USER = "LICENSED_USER"
    PROJECT_ADMIN = "PROJECT_ADMIN"
    PROJECT_CREATE = "PROJECT_CREATE"
    PROJECT_READ = "PROJECT_READ"
    PROJECT_VIEW = "PROJECT_VIEW"
    PROJECT_WRITE = "PROJECT_WRITE"
    REPO_ADMIN = "REPO_ADMIN"
    REPO_CREATE = "REPO_CREATE"
    REPO_READ = "REPO_READ"
    REPO_WRITE = "REPO_WRITE"
    SYS_ADMIN = "SYS_ADMIN"
    USER_ADMIN = "USER_ADMIN"

    def __str__(self) -> str:
        return str(self.value)
