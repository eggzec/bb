from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_runner_oauth_client import PipelineRunnerOauthClient
    from ..models.pipeline_runner_state import PipelineRunnerState


T = TypeVar("T", bound="PipelineRunner")


@_attrs_define
class PipelineRunner:
    type_: str
    uuid: str | Unset = UNSET
    """ The UUID identifying the runner. """
    name: str | Unset = UNSET
    """ The name of the runner. """
    labels: list[str] | Unset = UNSET
    """ Labels assigned to the runner for identification and routing. """
    state: PipelineRunnerState | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the runner was created. """
    updated_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the runner was last updated. """
    oauth_client: PipelineRunnerOauthClient | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        name = self.name

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        oauth_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oauth_client, Unset):
            oauth_client = self.oauth_client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if state is not UNSET:
            field_dict["state"] = state
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if oauth_client is not UNSET:
            field_dict["oauth_client"] = oauth_client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_runner_oauth_client import PipelineRunnerOauthClient
        from ..models.pipeline_runner_state import PipelineRunnerState

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        _state = d.pop("state", UNSET)
        state: PipelineRunnerState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PipelineRunnerState.from_dict(_state)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        _oauth_client = d.pop("oauth_client", UNSET)
        oauth_client: PipelineRunnerOauthClient | Unset
        if isinstance(_oauth_client, Unset):
            oauth_client = UNSET
        else:
            oauth_client = PipelineRunnerOauthClient.from_dict(_oauth_client)

        pipeline_runner = cls(
            type_=type_,
            uuid=uuid,
            name=name,
            labels=labels,
            state=state,
            created_on=created_on,
            updated_on=updated_on,
            oauth_client=oauth_client,
        )

        pipeline_runner.additional_properties = d
        return pipeline_runner

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
