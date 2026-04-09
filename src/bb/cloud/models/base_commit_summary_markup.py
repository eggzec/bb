from enum import StrEnum


class BaseCommitSummaryMarkup(StrEnum):
    CREOLE = "creole"
    MARKDOWN = "markdown"
    PLAINTEXT = "plaintext"
