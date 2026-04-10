from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_cluster_node_address import RestClusterNodeAddress


T = TypeVar("T", bound="RestClusterNode")


@_attrs_define
class RestClusterNode:
    address: RestClusterNodeAddress | Unset = UNSET
    build_version: str | Unset = UNSET
    id: str | Unset = UNSET
    local: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        build_version = self.build_version

        id = self.id

        local = self.local

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if build_version is not UNSET:
            field_dict["buildVersion"] = build_version
        if id is not UNSET:
            field_dict["id"] = id
        if local is not UNSET:
            field_dict["local"] = local
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_cluster_node_address import RestClusterNodeAddress

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: RestClusterNodeAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = RestClusterNodeAddress.from_dict(_address)

        build_version = d.pop("buildVersion", UNSET)

        id = d.pop("id", UNSET)

        local = d.pop("local", UNSET)

        name = d.pop("name", UNSET)

        rest_cluster_node = cls(
            address=address,
            build_version=build_version,
            id=id,
            local=local,
            name=name,
        )

        rest_cluster_node.additional_properties = d
        return rest_cluster_node

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
