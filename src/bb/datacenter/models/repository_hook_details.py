from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_hook_details_supported_scopes_item import RepositoryHookDetailsSupportedScopesItem
from ..models.repository_hook_details_type import RepositoryHookDetailsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryHookDetails")


@_attrs_define
class RepositoryHookDetails:
    config_form_key: str | Unset = UNSET
    config_form_view: str | Unset = UNSET
    description: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    supported_scopes: list[RepositoryHookDetailsSupportedScopesItem] | Unset = UNSET
    type_: RepositoryHookDetailsType | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_form_key = self.config_form_key

        config_form_view = self.config_form_view

        description = self.description

        key = self.key

        name = self.name

        supported_scopes: list[str] | Unset = UNSET
        if not isinstance(self.supported_scopes, Unset):
            supported_scopes = []
            for supported_scopes_item_data in self.supported_scopes:
                supported_scopes_item = supported_scopes_item_data.value
                supported_scopes.append(supported_scopes_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_form_key is not UNSET:
            field_dict["configFormKey"] = config_form_key
        if config_form_view is not UNSET:
            field_dict["configFormView"] = config_form_view
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if supported_scopes is not UNSET:
            field_dict["supportedScopes"] = supported_scopes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_form_key = d.pop("configFormKey", UNSET)

        config_form_view = d.pop("configFormView", UNSET)

        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        _supported_scopes = d.pop("supportedScopes", UNSET)
        supported_scopes: list[RepositoryHookDetailsSupportedScopesItem] | Unset = UNSET
        if _supported_scopes is not UNSET:
            supported_scopes = []
            for supported_scopes_item_data in _supported_scopes:
                supported_scopes_item = RepositoryHookDetailsSupportedScopesItem(supported_scopes_item_data)

                supported_scopes.append(supported_scopes_item)

        _type_ = d.pop("type", UNSET)
        type_: RepositoryHookDetailsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RepositoryHookDetailsType(_type_)

        version = d.pop("version", UNSET)

        repository_hook_details = cls(
            config_form_key=config_form_key,
            config_form_view=config_form_view,
            description=description,
            key=key,
            name=name,
            supported_scopes=supported_scopes,
            type_=type_,
            version=version,
        )

        repository_hook_details.additional_properties = d
        return repository_hook_details

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
