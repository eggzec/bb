from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deployment_state_completed_name import DeploymentStateCompletedName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.deployment_state_completed_status import DeploymentStateCompletedStatus


T = TypeVar("T", bound="DeploymentStateCompleted")


@_attrs_define
class DeploymentStateCompleted:
    type_: str
    name: DeploymentStateCompletedName | Unset = UNSET
    """ The name of deployment state (COMPLETED). """
    url: str | Unset = UNSET
    """ Link to the deployment result. """
    deployer: Account | Unset = UNSET
    status: DeploymentStateCompletedStatus | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    """ The timestamp when the deployment was started. """
    completion_date: datetime.datetime | Unset = UNSET
    """ The timestamp when the deployment completed. """
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

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        completion_date: str | Unset = UNSET
        if not isinstance(self.completion_date, Unset):
            completion_date = self.completion_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if deployer is not UNSET:
            field_dict["deployer"] = deployer
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if completion_date is not UNSET:
            field_dict["completion_date"] = completion_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.deployment_state_completed_status import DeploymentStateCompletedStatus

        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: DeploymentStateCompletedName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateCompletedName(_name)

        url = d.pop("url", UNSET)

        _deployer = d.pop("deployer", UNSET)
        deployer: Account | Unset
        if isinstance(_deployer, Unset):
            deployer = UNSET
        else:
            deployer = Account.from_dict(_deployer)

        _status = d.pop("status", UNSET)
        status: DeploymentStateCompletedStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeploymentStateCompletedStatus.from_dict(_status)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _completion_date = d.pop("completion_date", UNSET)
        completion_date: datetime.datetime | Unset
        if isinstance(_completion_date, Unset):
            completion_date = UNSET
        else:
            completion_date = isoparse(_completion_date)

        deployment_state_completed = cls(
            type_=type_,
            name=name,
            url=url,
            deployer=deployer,
            status=status,
            start_date=start_date,
            completion_date=completion_date,
        )

        deployment_state_completed.additional_properties = d
        return deployment_state_completed

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
