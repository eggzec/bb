from enum import StrEnum


class GetWorkspacesRole(StrEnum):
    COLLABORATOR = "collaborator"
    MEMBER = "member"
    OWNER = "owner"
