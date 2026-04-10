from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestSecretScanningRuleSetRequest")


@_attrs_define
class RestSecretScanningRuleSetRequest:
    line_regex: str | Unset = UNSET
    """ Regular expression for matching a secret on a code line """
    name: str | Unset = UNSET
    """ Human readable name for the rule """
    path_regex: str | Unset = UNSET
    """ Regular expression matching file names """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_regex = self.line_regex

        name = self.name

        path_regex = self.path_regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_regex is not UNSET:
            field_dict["lineRegex"] = line_regex
        if name is not UNSET:
            field_dict["name"] = name
        if path_regex is not UNSET:
            field_dict["pathRegex"] = path_regex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_regex = d.pop("lineRegex", UNSET)

        name = d.pop("name", UNSET)

        path_regex = d.pop("pathRegex", UNSET)

        rest_secret_scanning_rule_set_request = cls(
            line_regex=line_regex,
            name=name,
            path_regex=path_regex,
        )

        rest_secret_scanning_rule_set_request.additional_properties = d
        return rest_secret_scanning_rule_set_request

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
