from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_auto_merge_restricted_settings_restriction_state import (
    RestAutoMergeRestrictedSettingsRestrictionState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_auto_merge_restricted_settings_scope import RestAutoMergeRestrictedSettingsScope


T = TypeVar("T", bound="RestAutoMergeRestrictedSettings")


@_attrs_define
class RestAutoMergeRestrictedSettings:
    enabled: bool | Unset = UNSET
    restriction_state: RestAutoMergeRestrictedSettingsRestrictionState | Unset = UNSET
    """ The restriction state of this scope's project. """
    scope: RestAutoMergeRestrictedSettingsScope | Unset = UNSET
    """ The scope that these settings apply to. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        restriction_state: str | Unset = UNSET
        if not isinstance(self.restriction_state, Unset):
            restriction_state = self.restriction_state.value

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if restriction_state is not UNSET:
            field_dict["restrictionState"] = restriction_state
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_auto_merge_restricted_settings_scope import RestAutoMergeRestrictedSettingsScope

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _restriction_state = d.pop("restrictionState", UNSET)
        restriction_state: RestAutoMergeRestrictedSettingsRestrictionState | Unset
        if isinstance(_restriction_state, Unset):
            restriction_state = UNSET
        else:
            restriction_state = RestAutoMergeRestrictedSettingsRestrictionState(_restriction_state)

        _scope = d.pop("scope", UNSET)
        scope: RestAutoMergeRestrictedSettingsScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestAutoMergeRestrictedSettingsScope.from_dict(_scope)

        rest_auto_merge_restricted_settings = cls(
            enabled=enabled,
            restriction_state=restriction_state,
            scope=scope,
        )

        rest_auto_merge_restricted_settings.additional_properties = d
        return rest_auto_merge_restricted_settings

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
