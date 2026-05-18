from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branching_model_settings_branch_types_item import BranchingModelSettingsBranchTypesItem
    from ..models.branching_model_settings_development import BranchingModelSettingsDevelopment
    from ..models.branching_model_settings_links import BranchingModelSettingsLinks
    from ..models.branching_model_settings_production import BranchingModelSettingsProduction


T = TypeVar("T", bound="BranchingModelSettings")


@_attrs_define
class BranchingModelSettings:
    type_: str | Unset = UNSET
    links: BranchingModelSettingsLinks | Unset = UNSET
    branch_types: list[BranchingModelSettingsBranchTypesItem] | Unset = UNSET
    development: BranchingModelSettingsDevelopment | Unset = UNSET
    production: BranchingModelSettingsProduction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        branch_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branch_types, Unset):
            branch_types = []
            for branch_types_item_data in self.branch_types:
                branch_types_item = branch_types_item_data.to_dict()
                branch_types.append(branch_types_item)

        development: dict[str, Any] | Unset = UNSET
        if not isinstance(self.development, Unset):
            development = self.development.to_dict()

        production: dict[str, Any] | Unset = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if branch_types is not UNSET:
            field_dict["branch_types"] = branch_types
        if development is not UNSET:
            field_dict["development"] = development
        if production is not UNSET:
            field_dict["production"] = production

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branching_model_settings_branch_types_item import BranchingModelSettingsBranchTypesItem
        from ..models.branching_model_settings_development import BranchingModelSettingsDevelopment
        from ..models.branching_model_settings_links import BranchingModelSettingsLinks
        from ..models.branching_model_settings_production import BranchingModelSettingsProduction

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: BranchingModelSettingsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BranchingModelSettingsLinks.from_dict(_links)

        _branch_types = d.pop("branch_types", UNSET)
        branch_types: list[BranchingModelSettingsBranchTypesItem] | Unset = UNSET
        if _branch_types is not UNSET:
            branch_types = []
            for branch_types_item_data in _branch_types:
                branch_types_item = BranchingModelSettingsBranchTypesItem.from_dict(branch_types_item_data)

                branch_types.append(branch_types_item)

        _development = d.pop("development", UNSET)
        development: BranchingModelSettingsDevelopment | Unset
        if isinstance(_development, Unset):
            development = UNSET
        else:
            development = BranchingModelSettingsDevelopment.from_dict(_development)

        _production = d.pop("production", UNSET)
        production: BranchingModelSettingsProduction | Unset
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = BranchingModelSettingsProduction.from_dict(_production)

        branching_model_settings = cls(
            type_=type_,
            links=links,
            branch_types=branch_types,
            development=development,
            production=production,
        )

        branching_model_settings.additional_properties = d
        return branching_model_settings

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
