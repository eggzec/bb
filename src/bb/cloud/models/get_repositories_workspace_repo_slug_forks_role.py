from enum import StrEnum


class GetRepositoriesWorkspaceRepoSlugForksRole(StrEnum):
    ADMIN = "admin"
    CONTRIBUTOR = "contributor"
    MEMBER = "member"
    OWNER = "owner"
