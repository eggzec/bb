from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snippet import Snippet
    from ..models.snippet_comment_links import SnippetCommentLinks


T = TypeVar("T", bound="SnippetComment")


@_attrs_define
class SnippetComment:
    type_: str | Unset = UNSET
    links: SnippetCommentLinks | Unset = UNSET
    snippet: Snippet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        snippet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snippet, Unset):
            snippet = self.snippet.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snippet import Snippet
        from ..models.snippet_comment_links import SnippetCommentLinks

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: SnippetCommentLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SnippetCommentLinks.from_dict(_links)

        _snippet = d.pop("snippet", UNSET)
        snippet: Snippet | Unset
        if isinstance(_snippet, Unset):
            snippet = UNSET
        else:
            snippet = Snippet.from_dict(_snippet)

        snippet_comment = cls(
            type_=type_,
            links=links,
            snippet=snippet,
        )

        snippet_comment.additional_properties = d
        return snippet_comment

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
