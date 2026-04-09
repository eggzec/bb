from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_state_completed_status_failed_name import DeploymentStateCompletedStatusFailedName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateCompletedStatusFailed")


@_attrs_define
class DeploymentStateCompletedStatusFailed:
    type_: str
    name: DeploymentStateCompletedStatusFailedName | Unset = UNSET
    """ The name of the completed deployment status (FAILED). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: DeploymentStateCompletedStatusFailedName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateCompletedStatusFailedName(_name)

        deployment_state_completed_status_failed = cls(
            type_=type_,
            name=name,
        )

        deployment_state_completed_status_failed.additional_properties = d
        return deployment_state_completed_status_failed

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
