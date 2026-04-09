from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportOptions")


@_attrs_define
class ExportOptions:
    """Options for issue export."""

    type_: str
    project_key: str | Unset = UNSET
    project_name: str | Unset = UNSET
    send_email: bool | Unset = UNSET
    include_attachments: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        project_key = self.project_key

        project_name = self.project_name

        send_email = self.send_email

        include_attachments = self.include_attachments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if project_key is not UNSET:
            field_dict["project_key"] = project_key
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if send_email is not UNSET:
            field_dict["send_email"] = send_email
        if include_attachments is not UNSET:
            field_dict["include_attachments"] = include_attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        project_key = d.pop("project_key", UNSET)

        project_name = d.pop("project_name", UNSET)

        send_email = d.pop("send_email", UNSET)

        include_attachments = d.pop("include_attachments", UNSET)

        export_options = cls(
            type_=type_,
            project_key=project_key,
            project_name=project_name,
            send_email=send_email,
            include_attachments=include_attachments,
        )

        export_options.additional_properties = d
        return export_options

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
