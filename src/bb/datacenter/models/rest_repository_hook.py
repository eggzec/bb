from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_hook_details import RepositoryHookDetails
    from ..models.rest_repository_hook_scope import RestRepositoryHookScope


T = TypeVar("T", bound="RestRepositoryHook")


@_attrs_define
class RestRepositoryHook:
    configured: bool | Unset = UNSET
    details: RepositoryHookDetails | Unset = UNSET
    enabled: bool | Unset = UNSET
    scope: RestRepositoryHookScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        enabled = self.enabled

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configured is not UNSET:
            field_dict["configured"] = configured
        if details is not UNSET:
            field_dict["details"] = details
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_hook_details import RepositoryHookDetails
        from ..models.rest_repository_hook_scope import RestRepositoryHookScope

        d = dict(src_dict)
        configured = d.pop("configured", UNSET)

        _details = d.pop("details", UNSET)
        details: RepositoryHookDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RepositoryHookDetails.from_dict(_details)

        enabled = d.pop("enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: RestRepositoryHookScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestRepositoryHookScope.from_dict(_scope)

        rest_repository_hook = cls(
            configured=configured,
            details=details,
            enabled=enabled,
            scope=scope,
        )

        rest_repository_hook.additional_properties = d
        return rest_repository_hook

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
