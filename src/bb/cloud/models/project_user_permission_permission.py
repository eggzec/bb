from enum import StrEnum


class ProjectUserPermissionPermission(StrEnum):
    ADMIN = "admin"
    CREATE_REPO = "create-repo"
    NONE = "none"
    READ = "read"
    WRITE = "write"
