from enum import StrEnum


class GetSnippetsRole(StrEnum):
    CONTRIBUTOR = "contributor"
    MEMBER = "member"
    OWNER = "owner"
