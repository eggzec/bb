from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBranch")


@_attrs_define
class RestBranch:
    default: bool | Unset = UNSET
    display_id: str | Unset = UNSET
    id: str | Unset = UNSET
    latest_changeset: str | Unset = UNSET
    latest_commit: str | Unset = UNSET
    type_: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        display_id = self.display_id

        id = self.id

        latest_changeset = self.latest_changeset

        latest_commit = self.latest_commit

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if display_id is not UNSET:
            field_dict["displayId"] = display_id
        if id is not UNSET:
            field_dict["id"] = id
        if latest_changeset is not UNSET:
            field_dict["latestChangeset"] = latest_changeset
        if latest_commit is not UNSET:
            field_dict["latestCommit"] = latest_commit
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default = d.pop("default", UNSET)

        display_id = d.pop("displayId", UNSET)

        id = d.pop("id", UNSET)

        latest_changeset = d.pop("latestChangeset", UNSET)

        latest_commit = d.pop("latestCommit", UNSET)

        type_ = d.pop("type", UNSET)

        rest_branch = cls(
            default=default,
            display_id=display_id,
            id=id,
            latest_changeset=latest_changeset,
            latest_commit=latest_commit,
            type_=type_,
        )

        rest_branch.additional_properties = d
        return rest_branch

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
