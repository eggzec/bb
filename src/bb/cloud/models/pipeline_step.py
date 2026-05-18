from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_command import PipelineCommand
    from ..models.pipeline_image import PipelineImage
    from ..models.pipeline_step_state import PipelineStepState


T = TypeVar("T", bound="PipelineStep")


@_attrs_define
class PipelineStep:
    type_: str | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The UUID identifying the step. """
    started_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the step execution was started. This is not set when the step hasn't executed yet. """
    completed_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the step execution was completed. This is not set if the step is still in progress. """
    state: PipelineStepState | Unset = UNSET
    image: PipelineImage | Unset = UNSET
    """ The definition of a Docker image that can be used for a Bitbucket Pipelines step execution context. """
    setup_commands: list[PipelineCommand] | Unset = UNSET
    """ The list of commands that are executed as part of the setup phase of the build. These commands are executed
    outside the build container. """
    script_commands: list[PipelineCommand] | Unset = UNSET
    """ The list of build commands. These commands are executed in the build container. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        started_on: str | Unset = UNSET
        if not isinstance(self.started_on, Unset):
            started_on = self.started_on.isoformat()

        completed_on: str | Unset = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        setup_commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.setup_commands, Unset):
            setup_commands = []
            for setup_commands_item_data in self.setup_commands:
                setup_commands_item = setup_commands_item_data.to_dict()
                setup_commands.append(setup_commands_item)

        script_commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.script_commands, Unset):
            script_commands = []
            for script_commands_item_data in self.script_commands:
                script_commands_item = script_commands_item_data.to_dict()
                script_commands.append(script_commands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if started_on is not UNSET:
            field_dict["started_on"] = started_on
        if completed_on is not UNSET:
            field_dict["completed_on"] = completed_on
        if state is not UNSET:
            field_dict["state"] = state
        if image is not UNSET:
            field_dict["image"] = image
        if setup_commands is not UNSET:
            field_dict["setup_commands"] = setup_commands
        if script_commands is not UNSET:
            field_dict["script_commands"] = script_commands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_command import PipelineCommand
        from ..models.pipeline_image import PipelineImage
        from ..models.pipeline_step_state import PipelineStepState

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        _started_on = d.pop("started_on", UNSET)
        started_on: datetime.datetime | Unset
        if isinstance(_started_on, Unset):
            started_on = UNSET
        else:
            started_on = isoparse(_started_on)

        _completed_on = d.pop("completed_on", UNSET)
        completed_on: datetime.datetime | Unset
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        _state = d.pop("state", UNSET)
        state: PipelineStepState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PipelineStepState.from_dict(_state)

        _image = d.pop("image", UNSET)
        image: PipelineImage | Unset
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = PipelineImage.from_dict(_image)

        _setup_commands = d.pop("setup_commands", UNSET)
        setup_commands: list[PipelineCommand] | Unset = UNSET
        if _setup_commands is not UNSET:
            setup_commands = []
            for setup_commands_item_data in _setup_commands:
                setup_commands_item = PipelineCommand.from_dict(setup_commands_item_data)

                setup_commands.append(setup_commands_item)

        _script_commands = d.pop("script_commands", UNSET)
        script_commands: list[PipelineCommand] | Unset = UNSET
        if _script_commands is not UNSET:
            script_commands = []
            for script_commands_item_data in _script_commands:
                script_commands_item = PipelineCommand.from_dict(script_commands_item_data)

                script_commands.append(script_commands_item)

        pipeline_step = cls(
            type_=type_,
            uuid=uuid,
            started_on=started_on,
            completed_on=completed_on,
            state=state,
            image=image,
            setup_commands=setup_commands,
            script_commands=script_commands,
        )

        pipeline_step.additional_properties = d
        return pipeline_step

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
