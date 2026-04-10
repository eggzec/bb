from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestSingleAddInsightAnnotationRequest")


@_attrs_define
class RestSingleAddInsightAnnotationRequest:
    message: str
    severity: str
    external_id: str | Unset = UNSET
    line: int | Unset = UNSET
    link: str | Unset = UNSET
    path: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        severity = self.severity

        external_id = self.external_id

        line = self.line

        link = self.link

        path = self.path

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "severity": severity,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if line is not UNSET:
            field_dict["line"] = line
        if link is not UNSET:
            field_dict["link"] = link
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        severity = d.pop("severity")

        external_id = d.pop("externalId", UNSET)

        line = d.pop("line", UNSET)

        link = d.pop("link", UNSET)

        path = d.pop("path", UNSET)

        type_ = d.pop("type", UNSET)

        rest_single_add_insight_annotation_request = cls(
            message=message,
            severity=severity,
            external_id=external_id,
            line=line,
            link=link,
            path=path,
            type_=type_,
        )

        rest_single_add_insight_annotation_request.additional_properties = d
        return rest_single_add_insight_annotation_request

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
