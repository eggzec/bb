from enum import Enum


class GetRepositories1Permission(str, Enum):
    REPO_ADMIN = "REPO_ADMIN"
    REPO_READ = "REPO_READ"
    REPO_WRITE = "REPO_WRITE"

    def __str__(self) -> str:
        return str(self.value)
