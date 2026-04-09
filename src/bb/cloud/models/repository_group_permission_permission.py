from enum import StrEnum


class RepositoryGroupPermissionPermission(StrEnum):
    ADMIN = "admin"
    NONE = "none"
    READ = "read"
    WRITE = "write"
