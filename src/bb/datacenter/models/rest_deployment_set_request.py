from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_deployment_set_request_state import RestDeploymentSetRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_deployment_environment import RestDeploymentEnvironment


T = TypeVar("T", bound="RestDeploymentSetRequest")


@_attrs_define
class RestDeploymentSetRequest:
    deployment_sequence_number: int
    description: str
    display_name: str
    environment: RestDeploymentEnvironment
    key: str
    state: RestDeploymentSetRequestState
    url: str
    last_updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_sequence_number = self.deployment_sequence_number

        description = self.description

        display_name = self.display_name

        environment = self.environment.to_dict()

        key = self.key

        state = self.state.value

        url = self.url

        last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deploymentSequenceNumber": deployment_sequence_number,
                "description": description,
                "displayName": display_name,
                "environment": environment,
                "key": key,
                "state": state,
                "url": url,
            }
        )
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_deployment_environment import RestDeploymentEnvironment

        d = dict(src_dict)
        deployment_sequence_number = d.pop("deploymentSequenceNumber")

        description = d.pop("description")

        display_name = d.pop("displayName")

        environment = RestDeploymentEnvironment.from_dict(d.pop("environment"))

        key = d.pop("key")

        state = RestDeploymentSetRequestState(d.pop("state"))

        url = d.pop("url")

        last_updated = d.pop("lastUpdated", UNSET)

        rest_deployment_set_request = cls(
            deployment_sequence_number=deployment_sequence_number,
            description=description,
            display_name=display_name,
            environment=environment,
            key=key,
            state=state,
            url=url,
            last_updated=last_updated,
        )

        rest_deployment_set_request.additional_properties = d
        return rest_deployment_set_request

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
