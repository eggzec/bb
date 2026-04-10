from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_repository_mirror_event_type import RestRepositoryMirrorEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryMirrorEvent")


@_attrs_define
class RestRepositoryMirrorEvent:
    type_: RestRepositoryMirrorEventType
    upstream_repo_id: str
    mirror_repo_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        upstream_repo_id = self.upstream_repo_id

        mirror_repo_id = self.mirror_repo_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "upstreamRepoId": upstream_repo_id,
            }
        )
        if mirror_repo_id is not UNSET:
            field_dict["mirrorRepoId"] = mirror_repo_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = RestRepositoryMirrorEventType(d.pop("type"))

        upstream_repo_id = d.pop("upstreamRepoId")

        mirror_repo_id = d.pop("mirrorRepoId", UNSET)

        rest_repository_mirror_event = cls(
            type_=type_,
            upstream_repo_id=upstream_repo_id,
            mirror_repo_id=mirror_repo_id,
        )

        rest_repository_mirror_event.additional_properties = d
        return rest_repository_mirror_event

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
