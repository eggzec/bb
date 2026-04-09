from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_attachment_links import IssueAttachmentLinks


T = TypeVar("T", bound="IssueAttachment")


@_attrs_define
class IssueAttachment:
    type_: str
    links: IssueAttachmentLinks | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_attachment_links import IssueAttachmentLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: IssueAttachmentLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IssueAttachmentLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        issue_attachment = cls(
            type_=type_,
            links=links,
            name=name,
        )

        issue_attachment.additional_properties = d
        return issue_attachment

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
