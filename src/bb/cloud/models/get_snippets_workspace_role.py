from enum import StrEnum


class GetSnippetsWorkspaceRole(StrEnum):
    CONTRIBUTOR = "contributor"
    MEMBER = "member"
    OWNER = "owner"
