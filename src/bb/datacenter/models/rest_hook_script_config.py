from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_hook_script_config_scope import RestHookScriptConfigScope
    from ..models.rest_hook_script_config_script import RestHookScriptConfigScript


T = TypeVar("T", bound="RestHookScriptConfig")


@_attrs_define
class RestHookScriptConfig:
    scope: RestHookScriptConfigScope | Unset = UNSET
    script: RestHookScriptConfigScript | Unset = UNSET
    trigger_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        script: dict[str, Any] | Unset = UNSET
        if not isinstance(self.script, Unset):
            script = self.script.to_dict()

        trigger_ids: list[str] | Unset = UNSET
        if not isinstance(self.trigger_ids, Unset):
            trigger_ids = self.trigger_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if script is not UNSET:
            field_dict["script"] = script
        if trigger_ids is not UNSET:
            field_dict["triggerIds"] = trigger_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_hook_script_config_scope import RestHookScriptConfigScope
        from ..models.rest_hook_script_config_script import RestHookScriptConfigScript

        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: RestHookScriptConfigScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestHookScriptConfigScope.from_dict(_scope)

        _script = d.pop("script", UNSET)
        script: RestHookScriptConfigScript | Unset
        if isinstance(_script, Unset):
            script = UNSET
        else:
            script = RestHookScriptConfigScript.from_dict(_script)

        trigger_ids = cast(list[str], d.pop("triggerIds", UNSET))

        rest_hook_script_config = cls(
            scope=scope,
            script=script,
            trigger_ids=trigger_ids,
        )

        rest_hook_script_config.additional_properties = d
        return rest_hook_script_config

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
