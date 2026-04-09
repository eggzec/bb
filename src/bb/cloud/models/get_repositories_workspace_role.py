from enum import StrEnum


class GetRepositoriesWorkspaceRole(StrEnum):
    ADMIN = "admin"
    CONTRIBUTOR = "contributor"
    MEMBER = "member"
    OWNER = "owner"
