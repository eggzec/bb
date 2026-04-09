from enum import StrEnum


class RepositoryUserPermissionPermission(StrEnum):
    ADMIN = "admin"
    NONE = "none"
    READ = "read"
    WRITE = "write"
