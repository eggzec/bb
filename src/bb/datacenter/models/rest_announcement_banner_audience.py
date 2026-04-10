from enum import Enum


class RestAnnouncementBannerAudience(str, Enum):
    ALL = "ALL"
    AUTHENTICATED = "AUTHENTICATED"

    def __str__(self) -> str:
        return str(self.value)
