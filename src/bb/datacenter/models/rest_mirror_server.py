from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_mirror_server_mirror_type import RestMirrorServerMirrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMirrorServer")


@_attrs_define
class RestMirrorServer:
    base_url: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    last_seen_date: datetime.datetime | Unset = UNSET
    mirror_type: RestMirrorServerMirrorType | Unset = UNSET
    name: str | Unset = UNSET
    product_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        enabled = self.enabled

        id = self.id

        last_seen_date: str | Unset = UNSET
        if not isinstance(self.last_seen_date, Unset):
            last_seen_date = self.last_seen_date.isoformat()

        mirror_type: str | Unset = UNSET
        if not isinstance(self.mirror_type, Unset):
            mirror_type = self.mirror_type.value

        name = self.name

        product_version = self.product_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if last_seen_date is not UNSET:
            field_dict["lastSeenDate"] = last_seen_date
        if mirror_type is not UNSET:
            field_dict["mirrorType"] = mirror_type
        if name is not UNSET:
            field_dict["name"] = name
        if product_version is not UNSET:
            field_dict["productVersion"] = product_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _last_seen_date = d.pop("lastSeenDate", UNSET)
        last_seen_date: datetime.datetime | Unset
        if isinstance(_last_seen_date, Unset):
            last_seen_date = UNSET
        else:
            last_seen_date = isoparse(_last_seen_date)

        _mirror_type = d.pop("mirrorType", UNSET)
        mirror_type: RestMirrorServerMirrorType | Unset
        if isinstance(_mirror_type, Unset):
            mirror_type = UNSET
        else:
            mirror_type = RestMirrorServerMirrorType(_mirror_type)

        name = d.pop("name", UNSET)

        product_version = d.pop("productVersion", UNSET)

        rest_mirror_server = cls(
            base_url=base_url,
            enabled=enabled,
            id=id,
            last_seen_date=last_seen_date,
            mirror_type=mirror_type,
            name=name,
            product_version=product_version,
        )

        rest_mirror_server.additional_properties = d
        return rest_mirror_server

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
