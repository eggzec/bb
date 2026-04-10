from enum import Enum


class RestUpstreamSettingsMode(str, Enum):
    ALL_PROJECTS = "ALL_PROJECTS"
    SELECTED_PROJECTS = "SELECTED_PROJECTS"

    def __str__(self) -> str:
        return str(self.value)
