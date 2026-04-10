from enum import Enum


class SetPermissionForGroupsPermission(str, Enum):
    ADMIN = "ADMIN"
    LICENSED_USER = "LICENSED_USER"
    PROJECT_CREATE = "PROJECT_CREATE"
    SYS_ADMIN = "SYS_ADMIN"

    def __str__(self) -> str:
        return str(self.value)
