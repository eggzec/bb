from enum import Enum


class Search2Order(str, Enum):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"

    def __str__(self) -> str:
        return str(self.value)
