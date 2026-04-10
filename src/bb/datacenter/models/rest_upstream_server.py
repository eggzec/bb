from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_upstream_server_state import RestUpstreamServerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestUpstreamServer")


@_attrs_define
class RestUpstreamServer:
    base_url: str | Unset = UNSET
    id: str | Unset = UNSET
    state: RestUpstreamServerState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        id = self.id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: RestUpstreamServerState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestUpstreamServerState(_state)

        rest_upstream_server = cls(
            base_url=base_url,
            id=id,
            state=state,
        )

        rest_upstream_server.additional_properties = d
        return rest_upstream_server

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
