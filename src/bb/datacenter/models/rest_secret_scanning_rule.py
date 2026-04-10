from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_secret_scanning_rule_scope import RestSecretScanningRuleScope


T = TypeVar("T", bound="RestSecretScanningRule")


@_attrs_define
class RestSecretScanningRule:
    id: int | Unset = UNSET
    """ The ID of the rule """
    line_regex: str | Unset = UNSET
    """ If present, regular expression for matching a secret on a code line """
    name: str | Unset = UNSET
    """ Human readable name for the rule """
    path_regex: str | Unset = UNSET
    """ If present, regular expression matching file names """
    scope: RestSecretScanningRuleScope | Unset = UNSET
    """ The scope in which this rule was configured for. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        line_regex = self.line_regex

        name = self.name

        path_regex = self.path_regex

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if line_regex is not UNSET:
            field_dict["lineRegex"] = line_regex
        if name is not UNSET:
            field_dict["name"] = name
        if path_regex is not UNSET:
            field_dict["pathRegex"] = path_regex
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_secret_scanning_rule_scope import RestSecretScanningRuleScope

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        line_regex = d.pop("lineRegex", UNSET)

        name = d.pop("name", UNSET)

        path_regex = d.pop("pathRegex", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: RestSecretScanningRuleScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestSecretScanningRuleScope.from_dict(_scope)

        rest_secret_scanning_rule = cls(
            id=id,
            line_regex=line_regex,
            name=name,
            path_regex=path_regex,
            scope=scope,
        )

        rest_secret_scanning_rule.additional_properties = d
        return rest_secret_scanning_rule

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
