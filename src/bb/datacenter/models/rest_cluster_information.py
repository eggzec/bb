from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_cluster_information_local_node import RestClusterInformationLocalNode
    from ..models.rest_cluster_node import RestClusterNode


T = TypeVar("T", bound="RestClusterInformation")


@_attrs_define
class RestClusterInformation:
    local_node: RestClusterInformationLocalNode | Unset = UNSET
    nodes: list[RestClusterNode] | Unset = UNSET
    running: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_node, Unset):
            local_node = self.local_node.to_dict()

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        running = self.running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_node is not UNSET:
            field_dict["localNode"] = local_node
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if running is not UNSET:
            field_dict["running"] = running

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_cluster_information_local_node import RestClusterInformationLocalNode
        from ..models.rest_cluster_node import RestClusterNode

        d = dict(src_dict)
        _local_node = d.pop("localNode", UNSET)
        local_node: RestClusterInformationLocalNode | Unset
        if isinstance(_local_node, Unset):
            local_node = UNSET
        else:
            local_node = RestClusterInformationLocalNode.from_dict(_local_node)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[RestClusterNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = RestClusterNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        running = d.pop("running", UNSET)

        rest_cluster_information = cls(
            local_node=local_node,
            nodes=nodes,
            running=running,
        )

        rest_cluster_information.additional_properties = d
        return rest_cluster_information

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
