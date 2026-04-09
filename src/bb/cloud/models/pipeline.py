from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.pipeline_configuration_source import PipelineConfigurationSource
    from ..models.pipeline_state import PipelineState
    from ..models.pipeline_target import PipelineTarget
    from ..models.pipeline_trigger import PipelineTrigger
    from ..models.pipeline_variable import PipelineVariable
    from ..models.pipelines_pipeline_links import PipelinesPipelineLinks
    from ..models.repository import Repository


T = TypeVar("T", bound="Pipeline")


@_attrs_define
class Pipeline:
    type_: str
    uuid: str | Unset = UNSET
    """ The UUID identifying the pipeline. """
    build_number: int | Unset = UNSET
    """ The build number of the pipeline. """
    creator: Account | Unset = UNSET
    repository: Repository | Unset = UNSET
    target: PipelineTarget | Unset = UNSET
    trigger: PipelineTrigger | Unset = UNSET
    state: PipelineState | Unset = UNSET
    variables: list[PipelineVariable] | Unset = UNSET
    """ The variables for the pipeline. """
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the pipeline was created. """
    completed_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the Pipeline was completed. This is not set if the pipeline is still in progress. """
    build_seconds_used: int | Unset = UNSET
    """ The number of build seconds used by this pipeline. """
    configuration_sources: list[PipelineConfigurationSource] | Unset = UNSET
    """ An ordered list of sources of the pipeline configuration """
    links: PipelinesPipelineLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        build_number = self.build_number

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        trigger: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        completed_on: str | Unset = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        build_seconds_used = self.build_seconds_used

        configuration_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_sources, Unset):
            configuration_sources = []
            for configuration_sources_item_data in self.configuration_sources:
                configuration_sources_item = configuration_sources_item_data.to_dict()
                configuration_sources.append(configuration_sources_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if build_number is not UNSET:
            field_dict["build_number"] = build_number
        if creator is not UNSET:
            field_dict["creator"] = creator
        if repository is not UNSET:
            field_dict["repository"] = repository
        if target is not UNSET:
            field_dict["target"] = target
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if state is not UNSET:
            field_dict["state"] = state
        if variables is not UNSET:
            field_dict["variables"] = variables
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if completed_on is not UNSET:
            field_dict["completed_on"] = completed_on
        if build_seconds_used is not UNSET:
            field_dict["build_seconds_used"] = build_seconds_used
        if configuration_sources is not UNSET:
            field_dict["configuration_sources"] = configuration_sources
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.pipeline_configuration_source import PipelineConfigurationSource
        from ..models.pipeline_state import PipelineState
        from ..models.pipeline_target import PipelineTarget
        from ..models.pipeline_trigger import PipelineTrigger
        from ..models.pipeline_variable import PipelineVariable
        from ..models.pipelines_pipeline_links import PipelinesPipelineLinks
        from ..models.repository import Repository

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        build_number = d.pop("build_number", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Account | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = Account.from_dict(_creator)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _target = d.pop("target", UNSET)
        target: PipelineTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PipelineTarget.from_dict(_target)

        _trigger = d.pop("trigger", UNSET)
        trigger: PipelineTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = PipelineTrigger.from_dict(_trigger)

        _state = d.pop("state", UNSET)
        state: PipelineState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PipelineState.from_dict(_state)

        _variables = d.pop("variables", UNSET)
        variables: list[PipelineVariable] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = PipelineVariable.from_dict(variables_item_data)

                variables.append(variables_item)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _completed_on = d.pop("completed_on", UNSET)
        completed_on: datetime.datetime | Unset
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        build_seconds_used = d.pop("build_seconds_used", UNSET)

        _configuration_sources = d.pop("configuration_sources", UNSET)
        configuration_sources: list[PipelineConfigurationSource] | Unset = UNSET
        if _configuration_sources is not UNSET:
            configuration_sources = []
            for configuration_sources_item_data in _configuration_sources:
                configuration_sources_item = PipelineConfigurationSource.from_dict(configuration_sources_item_data)

                configuration_sources.append(configuration_sources_item)

        _links = d.pop("links", UNSET)
        links: PipelinesPipelineLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PipelinesPipelineLinks.from_dict(_links)

        pipeline = cls(
            type_=type_,
            uuid=uuid,
            build_number=build_number,
            creator=creator,
            repository=repository,
            target=target,
            trigger=trigger,
            state=state,
            variables=variables,
            created_on=created_on,
            completed_on=completed_on,
            build_seconds_used=build_seconds_used,
            configuration_sources=configuration_sources,
            links=links,
        )

        pipeline.additional_properties = d
        return pipeline

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
