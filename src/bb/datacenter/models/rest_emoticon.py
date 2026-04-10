from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestEmoticon")


@_attrs_define
class RestEmoticon:
    shortcut: str | Unset = UNSET
    url: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shortcut = self.shortcut

        url = self.url

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shortcut is not UNSET:
            field_dict["shortcut"] = shortcut
        if url is not UNSET:
            field_dict["url"] = url
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shortcut = d.pop("shortcut", UNSET)

        url = d.pop("url", UNSET)

        value = d.pop("value", UNSET)

        rest_emoticon = cls(
            shortcut=shortcut,
            url=url,
            value=value,
        )

        rest_emoticon.additional_properties = d
        return rest_emoticon

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
