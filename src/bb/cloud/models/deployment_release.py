from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit


T = TypeVar("T", bound="DeploymentRelease")


@_attrs_define
class DeploymentRelease:
    type_: str | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The UUID identifying the release. """
    name: str | Unset = UNSET
    """ The name of the release. """
    url: str | Unset = UNSET
    """ Link to the pipeline that produced the release. """
    commit: Commit | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the release was created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        name = self.name

        url = self.url

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if commit is not UNSET:
            field_dict["commit"] = commit
        if created_on is not UNSET:
            field_dict["created_on"] = created_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _commit = d.pop("commit", UNSET)
        commit: Commit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = Commit.from_dict(_commit)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        deployment_release = cls(
            type_=type_,
            uuid=uuid,
            name=name,
            url=url,
            commit=commit,
            created_on=created_on,
        )

        deployment_release.additional_properties = d
        return deployment_release

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
