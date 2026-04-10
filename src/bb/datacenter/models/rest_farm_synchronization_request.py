from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_farm_synchronization_request_type import RestFarmSynchronizationRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestFarmSynchronizationRequest")


@_attrs_define
class RestFarmSynchronizationRequest:
    attempt: int | Unset = UNSET
    created_at: str | Unset = UNSET
    external_repo_id: str | Unset = UNSET
    type_: RestFarmSynchronizationRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        created_at = self.created_at

        external_repo_id = self.external_repo_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if external_repo_id is not UNSET:
            field_dict["externalRepoId"] = external_repo_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt = d.pop("attempt", UNSET)

        created_at = d.pop("createdAt", UNSET)

        external_repo_id = d.pop("externalRepoId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestFarmSynchronizationRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestFarmSynchronizationRequestType(_type_)

        rest_farm_synchronization_request = cls(
            attempt=attempt,
            created_at=created_at,
            external_repo_id=external_repo_id,
            type_=type_,
        )

        rest_farm_synchronization_request.additional_properties = d
        return rest_farm_synchronization_request

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
