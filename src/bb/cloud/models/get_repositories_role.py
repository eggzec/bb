from enum import StrEnum


class GetRepositoriesRole(StrEnum):
    ADMIN = "admin"
    CONTRIBUTOR = "contributor"
    MEMBER = "member"
    OWNER = "owner"
