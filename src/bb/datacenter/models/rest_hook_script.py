from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_hook_script_type import RestHookScriptType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestHookScript")


@_attrs_define
class RestHookScript:
    created_date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    plugin_key: str | Unset = UNSET
    type_: RestHookScriptType | Unset = UNSET
    updated_date: datetime.datetime | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        description = self.description

        id = self.id

        name = self.name

        plugin_key = self.plugin_key

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_date: str | Unset = UNSET
        if not isinstance(self.updated_date, Unset):
            updated_date = self.updated_date.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if plugin_key is not UNSET:
            field_dict["pluginKey"] = plugin_key
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        plugin_key = d.pop("pluginKey", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestHookScriptType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestHookScriptType(_type_)

        _updated_date = d.pop("updatedDate", UNSET)
        updated_date: datetime.datetime | Unset
        if isinstance(_updated_date, Unset):
            updated_date = UNSET
        else:
            updated_date = isoparse(_updated_date)

        version = d.pop("version", UNSET)

        rest_hook_script = cls(
            created_date=created_date,
            description=description,
            id=id,
            name=name,
            plugin_key=plugin_key,
            type_=type_,
            updated_date=updated_date,
            version=version,
        )

        rest_hook_script.additional_properties = d
        return rest_hook_script

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
