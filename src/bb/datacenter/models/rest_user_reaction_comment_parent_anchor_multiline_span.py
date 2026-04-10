from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RestUserReactionCommentParentAnchorMultilineSpan")


@_attrs_define
class RestUserReactionCommentParentAnchorMultilineSpan:
    dst_span_end: int
    """ The line number of the last line on the right-hand side of the diff that the comment spans """
    dst_span_start: int
    """ The line number of the first line on the right-hand side of the diff that the comment spans """
    src_span_end: int
    """ The line number of the last line on the left-hand side of the diff that the comment spans """
    src_span_start: int
    """ The line number of the first line on the left-hand side of the diff that the comment spans """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dst_span_end = self.dst_span_end

        dst_span_start = self.dst_span_start

        src_span_end = self.src_span_end

        src_span_start = self.src_span_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dstSpanEnd": dst_span_end,
                "dstSpanStart": dst_span_start,
                "srcSpanEnd": src_span_end,
                "srcSpanStart": src_span_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dst_span_end = d.pop("dstSpanEnd")

        dst_span_start = d.pop("dstSpanStart")

        src_span_end = d.pop("srcSpanEnd")

        src_span_start = d.pop("srcSpanStart")

        rest_user_reaction_comment_parent_anchor_multiline_span = cls(
            dst_span_end=dst_span_end,
            dst_span_start=dst_span_start,
            src_span_end=src_span_end,
            src_span_start=src_span_start,
        )

        rest_user_reaction_comment_parent_anchor_multiline_span.additional_properties = d
        return rest_user_reaction_comment_parent_anchor_multiline_span

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
