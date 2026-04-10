from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_mirroring_request_mirror_type import RestMirroringRequestMirrorType
from ..models.rest_mirroring_request_state import RestMirroringRequestState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMirroringRequest")


@_attrs_define
class RestMirroringRequest:
    id: int | Unset = UNSET
    mirror_base_url: str | Unset = UNSET
    mirror_id: str | Unset = UNSET
    mirror_name: str | Unset = UNSET
    mirror_type: RestMirroringRequestMirrorType | Unset = UNSET
    product_version: str | Unset = UNSET
    state: RestMirroringRequestState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mirror_base_url = self.mirror_base_url

        mirror_id = self.mirror_id

        mirror_name = self.mirror_name

        mirror_type: str | Unset = UNSET
        if not isinstance(self.mirror_type, Unset):
            mirror_type = self.mirror_type.value

        product_version = self.product_version

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mirror_base_url is not UNSET:
            field_dict["mirrorBaseUrl"] = mirror_base_url
        if mirror_id is not UNSET:
            field_dict["mirrorId"] = mirror_id
        if mirror_name is not UNSET:
            field_dict["mirrorName"] = mirror_name
        if mirror_type is not UNSET:
            field_dict["mirrorType"] = mirror_type
        if product_version is not UNSET:
            field_dict["productVersion"] = product_version
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mirror_base_url = d.pop("mirrorBaseUrl", UNSET)

        mirror_id = d.pop("mirrorId", UNSET)

        mirror_name = d.pop("mirrorName", UNSET)

        _mirror_type = d.pop("mirrorType", UNSET)
        mirror_type: RestMirroringRequestMirrorType | Unset
        if isinstance(_mirror_type, Unset):
            mirror_type = UNSET
        else:
            mirror_type = RestMirroringRequestMirrorType(_mirror_type)

        product_version = d.pop("productVersion", UNSET)

        _state = d.pop("state", UNSET)
        state: RestMirroringRequestState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestMirroringRequestState(_state)

        rest_mirroring_request = cls(
            id=id,
            mirror_base_url=mirror_base_url,
            mirror_id=mirror_id,
            mirror_name=mirror_name,
            mirror_type=mirror_type,
            product_version=product_version,
            state=state,
        )

        rest_mirroring_request.additional_properties = d
        return rest_mirroring_request

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
