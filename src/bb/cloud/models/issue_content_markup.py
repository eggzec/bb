from enum import StrEnum


class IssueContentMarkup(StrEnum):
    CREOLE = "creole"
    MARKDOWN = "markdown"
    PLAINTEXT = "plaintext"
