from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineCache")


@_attrs_define
class PipelineCache:
    type_: str
    uuid: str | Unset = UNSET
    """ The UUID identifying the pipeline cache. """
    pipeline_uuid: str | Unset = UNSET
    """ The UUID of the pipeline that created the cache. """
    step_uuid: str | Unset = UNSET
    """ The uuid of the step that created the cache. """
    name: str | Unset = UNSET
    """ The name of the cache. """
    key_hash: str | Unset = UNSET
    """ The key hash of the cache version. """
    path: str | Unset = UNSET
    """ The path where the cache contents were retrieved from. """
    file_size_bytes: int | Unset = UNSET
    """ The size of the file containing the archive of the cache. """
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the cache was created. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        pipeline_uuid = self.pipeline_uuid

        step_uuid = self.step_uuid

        name = self.name

        key_hash = self.key_hash

        path = self.path

        file_size_bytes = self.file_size_bytes

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if pipeline_uuid is not UNSET:
            field_dict["pipeline_uuid"] = pipeline_uuid
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if key_hash is not UNSET:
            field_dict["key_hash"] = key_hash
        if path is not UNSET:
            field_dict["path"] = path
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if created_on is not UNSET:
            field_dict["created_on"] = created_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        pipeline_uuid = d.pop("pipeline_uuid", UNSET)

        step_uuid = d.pop("step_uuid", UNSET)

        name = d.pop("name", UNSET)

        key_hash = d.pop("key_hash", UNSET)

        path = d.pop("path", UNSET)

        file_size_bytes = d.pop("file_size_bytes", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        pipeline_cache = cls(
            type_=type_,
            uuid=uuid,
            pipeline_uuid=pipeline_uuid,
            step_uuid=step_uuid,
            name=name,
            key_hash=key_hash,
            path=path,
            file_size_bytes=file_size_bytes,
            created_on=created_on,
        )

        pipeline_cache.additional_properties = d
        return pipeline_cache

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
