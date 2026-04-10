from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestEnhancedEntityLink")


@_attrs_define
class RestEnhancedEntityLink:
    application_link_id: str | Unset = UNSET
    display_url: str | Unset = UNSET
    project_id: int | Unset = UNSET
    project_key: str | Unset = UNSET
    project_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_link_id = self.application_link_id

        display_url = self.display_url

        project_id = self.project_id

        project_key = self.project_key

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_link_id is not UNSET:
            field_dict["applicationLinkId"] = application_link_id
        if display_url is not UNSET:
            field_dict["displayUrl"] = display_url
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_key is not UNSET:
            field_dict["projectKey"] = project_key
        if project_name is not UNSET:
            field_dict["projectName"] = project_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_link_id = d.pop("applicationLinkId", UNSET)

        display_url = d.pop("displayUrl", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_key = d.pop("projectKey", UNSET)

        project_name = d.pop("projectName", UNSET)

        rest_enhanced_entity_link = cls(
            application_link_id=application_link_id,
            display_url=display_url,
            project_id=project_id,
            project_key=project_key,
            project_name=project_name,
        )

        rest_enhanced_entity_link.additional_properties = d
        return rest_enhanced_entity_link

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
