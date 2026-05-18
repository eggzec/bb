from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_environment import DeploymentEnvironment
    from ..models.deployment_release import DeploymentRelease
    from ..models.deployment_state import DeploymentState


T = TypeVar("T", bound="Deployment")


@_attrs_define
class Deployment:
    type_: str | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The UUID identifying the deployment. """
    state: DeploymentState | Unset = UNSET
    environment: DeploymentEnvironment | Unset = UNSET
    release: DeploymentRelease | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        release: dict[str, Any] | Unset = UNSET
        if not isinstance(self.release, Unset):
            release = self.release.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if state is not UNSET:
            field_dict["state"] = state
        if environment is not UNSET:
            field_dict["environment"] = environment
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_environment import DeploymentEnvironment
        from ..models.deployment_release import DeploymentRelease
        from ..models.deployment_state import DeploymentState

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        _state = d.pop("state", UNSET)
        state: DeploymentState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DeploymentState.from_dict(_state)

        _environment = d.pop("environment", UNSET)
        environment: DeploymentEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = DeploymentEnvironment.from_dict(_environment)

        _release = d.pop("release", UNSET)
        release: DeploymentRelease | Unset
        if isinstance(_release, Unset):
            release = UNSET
        else:
            release = DeploymentRelease.from_dict(_release)

        deployment = cls(
            type_=type_,
            uuid=uuid,
            state=state,
            environment=environment,
            release=release,
        )

        deployment.additional_properties = d
        return deployment

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
