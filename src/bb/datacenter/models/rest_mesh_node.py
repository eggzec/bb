from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_mesh_node_state import RestMeshNodeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMeshNode")


@_attrs_define
class RestMeshNode:
    availability_zone: str | Unset = UNSET
    id: str | Unset = UNSET
    last_seen_date: float | Unset = UNSET
    name: str | Unset = UNSET
    offline: bool | Unset = UNSET
    rpc_id: str | Unset = UNSET
    rpc_url: str | Unset = UNSET
    state: RestMeshNodeState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability_zone = self.availability_zone

        id = self.id

        last_seen_date = self.last_seen_date

        name = self.name

        offline = self.offline

        rpc_id = self.rpc_id

        rpc_url = self.rpc_url

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_zone is not UNSET:
            field_dict["availabilityZone"] = availability_zone
        if id is not UNSET:
            field_dict["id"] = id
        if last_seen_date is not UNSET:
            field_dict["lastSeenDate"] = last_seen_date
        if name is not UNSET:
            field_dict["name"] = name
        if offline is not UNSET:
            field_dict["offline"] = offline
        if rpc_id is not UNSET:
            field_dict["rpcId"] = rpc_id
        if rpc_url is not UNSET:
            field_dict["rpcUrl"] = rpc_url
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability_zone = d.pop("availabilityZone", UNSET)

        id = d.pop("id", UNSET)

        last_seen_date = d.pop("lastSeenDate", UNSET)

        name = d.pop("name", UNSET)

        offline = d.pop("offline", UNSET)

        rpc_id = d.pop("rpcId", UNSET)

        rpc_url = d.pop("rpcUrl", UNSET)

        _state = d.pop("state", UNSET)
        state: RestMeshNodeState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestMeshNodeState(_state)

        rest_mesh_node = cls(
            availability_zone=availability_zone,
            id=id,
            last_seen_date=last_seen_date,
            name=name,
            offline=offline,
            rpc_id=rpc_id,
            rpc_url=rpc_url,
            state=state,
        )

        rest_mesh_node.additional_properties = d
        return rest_mesh_node

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
