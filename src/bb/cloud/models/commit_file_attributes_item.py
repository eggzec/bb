from enum import StrEnum


class CommitFileAttributesItem(StrEnum):
    BINARY = "binary"
    EXECUTABLE = "executable"
    LFS = "lfs"
    LINK = "link"
    SUBREPOSITORY = "subrepository"
