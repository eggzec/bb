from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rest_cluster_information_local_node_address import RestClusterInformationLocalNodeAddress


T = TypeVar("T", bound="RestClusterInformationLocalNode")


@_attrs_define
class RestClusterInformationLocalNode:
    address: RestClusterInformationLocalNodeAddress
    build_version: str
    id: str
    local: bool
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address.to_dict()

        build_version = self.build_version

        id = self.id

        local = self.local

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "buildVersion": build_version,
                "id": id,
                "local": local,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_cluster_information_local_node_address import RestClusterInformationLocalNodeAddress

        d = dict(src_dict)
        address = RestClusterInformationLocalNodeAddress.from_dict(d.pop("address"))

        build_version = d.pop("buildVersion")

        id = d.pop("id")

        local = d.pop("local")

        name = d.pop("name")

        rest_cluster_information_local_node = cls(
            address=address,
            build_version=build_version,
            id=id,
            local=local,
            name=name,
        )

        rest_cluster_information_local_node.additional_properties = d
        return rest_cluster_information_local_node

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
