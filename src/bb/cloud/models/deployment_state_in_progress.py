from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deployment_state_in_progress_name import DeploymentStateInProgressName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="DeploymentStateInProgress")


@_attrs_define
class DeploymentStateInProgress:
    type_: str | Unset = UNSET
    name: DeploymentStateInProgressName | Unset = UNSET
    """ The name of deployment state (IN_PROGRESS). """
    url: str | Unset = UNSET
    """ Link to the deployment result. """
    deployer: Account | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    """ The timestamp when the deployment was started. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        url = self.url

        deployer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deployer, Unset):
            deployer = self.deployer.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if deployer is not UNSET:
            field_dict["deployer"] = deployer
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _name = d.pop("name", UNSET)
        name: DeploymentStateInProgressName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateInProgressName(_name)

        url = d.pop("url", UNSET)

        _deployer = d.pop("deployer", UNSET)
        deployer: Account | Unset
        if isinstance(_deployer, Unset):
            deployer = UNSET
        else:
            deployer = Account.from_dict(_deployer)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        deployment_state_in_progress = cls(
            type_=type_,
            name=name,
            url=url,
            deployer=deployer,
            start_date=start_date,
        )

        deployment_state_in_progress.additional_properties = d
        return deployment_state_in_progress

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
