from enum import StrEnum


class RepositoryPermissionPermission(StrEnum):
    ADMIN = "admin"
    NONE = "none"
    READ = "read"
    WRITE = "write"
