from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pipeline_runner_state_status import PipelineRunnerStateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_runner_version import PipelineRunnerVersion


T = TypeVar("T", bound="PipelineRunnerState")


@_attrs_define
class PipelineRunnerState:
    type_: str | Unset = UNSET
    status: PipelineRunnerStateStatus | Unset = UNSET
    """ The current status of the runner. """
    version: PipelineRunnerVersion | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the runner state was last updated. """
    cordoned: bool | Unset = UNSET
    """ Whether the runner is cordoned (prevented from accepting new steps). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        cordoned = self.cordoned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if cordoned is not UNSET:
            field_dict["cordoned"] = cordoned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_runner_version import PipelineRunnerVersion

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _status = d.pop("status", UNSET)
        status: PipelineRunnerStateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PipelineRunnerStateStatus(_status)

        _version = d.pop("version", UNSET)
        version: PipelineRunnerVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = PipelineRunnerVersion.from_dict(_version)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        cordoned = d.pop("cordoned", UNSET)

        pipeline_runner_state = cls(
            type_=type_,
            status=status,
            version=version,
            updated_on=updated_on,
            cordoned=cordoned,
        )

        pipeline_runner_state.additional_properties = d
        return pipeline_runner_state

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
