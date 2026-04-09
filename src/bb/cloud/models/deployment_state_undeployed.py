from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_state_undeployed_name import DeploymentStateUndeployedName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateUndeployed")


@_attrs_define
class DeploymentStateUndeployed:
    type_: str
    name: DeploymentStateUndeployedName | Unset = UNSET
    """ The name of deployment state (UNDEPLOYED). """
    trigger_url: str | Unset = UNSET
    """ Link to trigger the deployment. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        trigger_url = self.trigger_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if trigger_url is not UNSET:
            field_dict["trigger_url"] = trigger_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: DeploymentStateUndeployedName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateUndeployedName(_name)

        trigger_url = d.pop("trigger_url", UNSET)

        deployment_state_undeployed = cls(
            type_=type_,
            name=name,
            trigger_url=trigger_url,
        )

        deployment_state_undeployed.additional_properties = d
        return deployment_state_undeployed

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
