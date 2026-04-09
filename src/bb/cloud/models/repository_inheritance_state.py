from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository_inheritance_state_override_settings import RepositoryInheritanceStateOverrideSettings


T = TypeVar("T", bound="RepositoryInheritanceState")


@_attrs_define
class RepositoryInheritanceState:
    """A json object representing the repository's inheritance state values"""

    type_: str
    override_settings: RepositoryInheritanceStateOverrideSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        override_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_settings, Unset):
            override_settings = self.override_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if override_settings is not UNSET:
            field_dict["override_settings"] = override_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository_inheritance_state_override_settings import RepositoryInheritanceStateOverrideSettings

        d = dict(src_dict)
        type_ = d.pop("type")

        _override_settings = d.pop("override_settings", UNSET)
        override_settings: RepositoryInheritanceStateOverrideSettings | Unset
        if isinstance(_override_settings, Unset):
            override_settings = UNSET
        else:
            override_settings = RepositoryInheritanceStateOverrideSettings.from_dict(_override_settings)

        repository_inheritance_state = cls(
            type_=type_,
            override_settings=override_settings,
        )

        repository_inheritance_state.additional_properties = d
        return repository_inheritance_state

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
