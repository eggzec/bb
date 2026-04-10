from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_mirrored_repository_descriptor_links import RestMirroredRepositoryDescriptorLinks
    from ..models.rest_mirrored_repository_descriptor_mirror_server import RestMirroredRepositoryDescriptorMirrorServer


T = TypeVar("T", bound="RestMirroredRepositoryDescriptor")


@_attrs_define
class RestMirroredRepositoryDescriptor:
    links: RestMirroredRepositoryDescriptorLinks | Unset = UNSET
    mirror_server: RestMirroredRepositoryDescriptorMirrorServer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        mirror_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mirror_server, Unset):
            mirror_server = self.mirror_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if mirror_server is not UNSET:
            field_dict["mirrorServer"] = mirror_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_mirrored_repository_descriptor_links import RestMirroredRepositoryDescriptorLinks
        from ..models.rest_mirrored_repository_descriptor_mirror_server import (
            RestMirroredRepositoryDescriptorMirrorServer,
        )

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: RestMirroredRepositoryDescriptorLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestMirroredRepositoryDescriptorLinks.from_dict(_links)

        _mirror_server = d.pop("mirrorServer", UNSET)
        mirror_server: RestMirroredRepositoryDescriptorMirrorServer | Unset
        if isinstance(_mirror_server, Unset):
            mirror_server = UNSET
        else:
            mirror_server = RestMirroredRepositoryDescriptorMirrorServer.from_dict(_mirror_server)

        rest_mirrored_repository_descriptor = cls(
            links=links,
            mirror_server=mirror_server,
        )

        rest_mirrored_repository_descriptor.additional_properties = d
        return rest_mirrored_repository_descriptor

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
