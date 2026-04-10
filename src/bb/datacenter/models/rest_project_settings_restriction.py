from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_project_settings_restriction_processed_state import RestProjectSettingsRestrictionProcessedState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_project_settings_restriction_project import RestProjectSettingsRestrictionProject


T = TypeVar("T", bound="RestProjectSettingsRestriction")


@_attrs_define
class RestProjectSettingsRestriction:
    component_key: str | Unset = UNSET
    feature_key: str | Unset = UNSET
    namespace: str | Unset = UNSET
    processed_state: RestProjectSettingsRestrictionProcessedState | Unset = UNSET
    project: RestProjectSettingsRestrictionProject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_key = self.component_key

        feature_key = self.feature_key

        namespace = self.namespace

        processed_state: str | Unset = UNSET
        if not isinstance(self.processed_state, Unset):
            processed_state = self.processed_state.value

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_key is not UNSET:
            field_dict["componentKey"] = component_key
        if feature_key is not UNSET:
            field_dict["featureKey"] = feature_key
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if processed_state is not UNSET:
            field_dict["processedState"] = processed_state
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_project_settings_restriction_project import RestProjectSettingsRestrictionProject

        d = dict(src_dict)
        component_key = d.pop("componentKey", UNSET)

        feature_key = d.pop("featureKey", UNSET)

        namespace = d.pop("namespace", UNSET)

        _processed_state = d.pop("processedState", UNSET)
        processed_state: RestProjectSettingsRestrictionProcessedState | Unset
        if isinstance(_processed_state, Unset):
            processed_state = UNSET
        else:
            processed_state = RestProjectSettingsRestrictionProcessedState(_processed_state)

        _project = d.pop("project", UNSET)
        project: RestProjectSettingsRestrictionProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RestProjectSettingsRestrictionProject.from_dict(_project)

        rest_project_settings_restriction = cls(
            component_key=component_key,
            feature_key=feature_key,
            namespace=namespace,
            processed_state=processed_state,
            project=project,
        )

        rest_project_settings_restriction.additional_properties = d
        return rest_project_settings_restriction

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
