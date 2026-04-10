from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestProjectSettingsRestrictionRequest")


@_attrs_define
class RestProjectSettingsRestrictionRequest:
    feature_key: str
    namespace: str
    component_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_key = self.feature_key

        namespace = self.namespace

        component_key = self.component_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureKey": feature_key,
                "namespace": namespace,
            }
        )
        if component_key is not UNSET:
            field_dict["componentKey"] = component_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature_key = d.pop("featureKey")

        namespace = d.pop("namespace")

        component_key = d.pop("componentKey", UNSET)

        rest_project_settings_restriction_request = cls(
            feature_key=feature_key,
            namespace=namespace,
            component_key=component_key,
        )

        rest_project_settings_restriction_request.additional_properties = d
        return rest_project_settings_restriction_request

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
