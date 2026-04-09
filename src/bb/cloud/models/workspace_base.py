from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_base_links import WorkspaceBaseLinks


T = TypeVar("T", bound="WorkspaceBase")


@_attrs_define
class WorkspaceBase:
    type_: str
    links: WorkspaceBaseLinks | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The workspace's immutable id. """
    slug: str | Unset = UNSET
    """ The short label that identifies this workspace. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        uuid = self.uuid

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_base_links import WorkspaceBaseLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: WorkspaceBaseLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkspaceBaseLinks.from_dict(_links)

        uuid = d.pop("uuid", UNSET)

        slug = d.pop("slug", UNSET)

        workspace_base = cls(
            type_=type_,
            links=links,
            uuid=uuid,
            slug=slug,
        )

        workspace_base.additional_properties = d
        return workspace_base

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
