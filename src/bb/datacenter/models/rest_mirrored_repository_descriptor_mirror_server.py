from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_mirrored_repository_descriptor_mirror_server_mirror_type import (
    RestMirroredRepositoryDescriptorMirrorServerMirrorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMirroredRepositoryDescriptorMirrorServer")


@_attrs_define
class RestMirroredRepositoryDescriptorMirrorServer:
    base_url: str
    id: str
    last_seen_date: datetime.datetime
    mirror_type: RestMirroredRepositoryDescriptorMirrorServerMirrorType
    name: str
    product_version: str
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        id = self.id

        last_seen_date = self.last_seen_date.isoformat()

        mirror_type = self.mirror_type.value

        name = self.name

        product_version = self.product_version

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseUrl": base_url,
                "id": id,
                "lastSeenDate": last_seen_date,
                "mirrorType": mirror_type,
                "name": name,
                "productVersion": product_version,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl")

        id = d.pop("id")

        last_seen_date = isoparse(d.pop("lastSeenDate"))

        mirror_type = RestMirroredRepositoryDescriptorMirrorServerMirrorType(d.pop("mirrorType"))

        name = d.pop("name")

        product_version = d.pop("productVersion")

        enabled = d.pop("enabled", UNSET)

        rest_mirrored_repository_descriptor_mirror_server = cls(
            base_url=base_url,
            id=id,
            last_seen_date=last_seen_date,
            mirror_type=mirror_type,
            name=name,
            product_version=product_version,
            enabled=enabled,
        )

        rest_mirrored_repository_descriptor_mirror_server.additional_properties = d
        return rest_mirrored_repository_descriptor_mirror_server

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
