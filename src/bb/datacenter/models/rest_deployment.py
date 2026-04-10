from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_deployment_state import RestDeploymentState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_deployment_environment import RestDeploymentEnvironment
    from ..models.rest_deployment_from_commit import RestDeploymentFromCommit
    from ..models.rest_deployment_repository import RestDeploymentRepository
    from ..models.rest_deployment_to_commit import RestDeploymentToCommit


T = TypeVar("T", bound="RestDeployment")


@_attrs_define
class RestDeployment:
    deployment_sequence_number: int | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    environment: RestDeploymentEnvironment | Unset = UNSET
    from_commit: RestDeploymentFromCommit | Unset = UNSET
    key: str | Unset = UNSET
    last_updated: int | Unset = UNSET
    repository: RestDeploymentRepository | Unset = UNSET
    state: RestDeploymentState | Unset = UNSET
    to_commit: RestDeploymentToCommit | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_sequence_number = self.deployment_sequence_number

        description = self.description

        display_name = self.display_name

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        from_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_commit, Unset):
            from_commit = self.from_commit.to_dict()

        key = self.key

        last_updated = self.last_updated

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        to_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_commit, Unset):
            to_commit = self.to_commit.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_sequence_number is not UNSET:
            field_dict["deploymentSequenceNumber"] = deployment_sequence_number
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if from_commit is not UNSET:
            field_dict["fromCommit"] = from_commit
        if key is not UNSET:
            field_dict["key"] = key
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if repository is not UNSET:
            field_dict["repository"] = repository
        if state is not UNSET:
            field_dict["state"] = state
        if to_commit is not UNSET:
            field_dict["toCommit"] = to_commit
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_deployment_environment import RestDeploymentEnvironment
        from ..models.rest_deployment_from_commit import RestDeploymentFromCommit
        from ..models.rest_deployment_repository import RestDeploymentRepository
        from ..models.rest_deployment_to_commit import RestDeploymentToCommit

        d = dict(src_dict)
        deployment_sequence_number = d.pop("deploymentSequenceNumber", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: RestDeploymentEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = RestDeploymentEnvironment.from_dict(_environment)

        _from_commit = d.pop("fromCommit", UNSET)
        from_commit: RestDeploymentFromCommit | Unset
        if isinstance(_from_commit, Unset):
            from_commit = UNSET
        else:
            from_commit = RestDeploymentFromCommit.from_dict(_from_commit)

        key = d.pop("key", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: RestDeploymentRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestDeploymentRepository.from_dict(_repository)

        _state = d.pop("state", UNSET)
        state: RestDeploymentState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestDeploymentState(_state)

        _to_commit = d.pop("toCommit", UNSET)
        to_commit: RestDeploymentToCommit | Unset
        if isinstance(_to_commit, Unset):
            to_commit = UNSET
        else:
            to_commit = RestDeploymentToCommit.from_dict(_to_commit)

        url = d.pop("url", UNSET)

        rest_deployment = cls(
            deployment_sequence_number=deployment_sequence_number,
            description=description,
            display_name=display_name,
            environment=environment,
            from_commit=from_commit,
            key=key,
            last_updated=last_updated,
            repository=repository,
            state=state,
            to_commit=to_commit,
            url=url,
        )

        rest_deployment.additional_properties = d
        return rest_deployment

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
