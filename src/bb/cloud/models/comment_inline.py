from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentInline")


@_attrs_define
class CommentInline:
    path: str
    """ The path of the file this comment is anchored to. """
    from_: int | Unset = UNSET
    """ The comment's anchor line in the old version of the file. If the comment is a multi-line comment, this is
    the ending line number in the old version of the file. """
    to: int | Unset = UNSET
    """ The comment's anchor line in the new version of the file. If the comment is a multi-line comment, this is
    the ending line number in the new version of the file. """
    start_from: int | Unset = UNSET
    """ The starting line number in the old version of the file, if the comment is a multi-line comment. This is
    null otherwise. """
    start_to: int | Unset = UNSET
    """ The starting line number in the new version of the file, if the comment is a multi-line comment. This is
    null otherwise. """

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        from_ = self.from_

        to = self.to

        start_from = self.start_from

        start_to = self.start_to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if start_from is not UNSET:
            field_dict["start_from"] = start_from
        if start_to is not UNSET:
            field_dict["start_to"] = start_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        start_from = d.pop("start_from", UNSET)

        start_to = d.pop("start_to", UNSET)

        comment_inline = cls(
            path=path,
            from_=from_,
            to=to,
            start_from=start_from,
            start_to=start_to,
        )

        return comment_inline
