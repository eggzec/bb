from enum import StrEnum


class PipelineSelectorType(StrEnum):
    BOOKMARKS = "bookmarks"
    BRANCHES = "branches"
    CUSTOM = "custom"
    DEFAULT = "default"
    TAGS = "tags"
