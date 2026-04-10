from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestInsightAnnotation")


@_attrs_define
class RestInsightAnnotation:
    external_id: str | Unset = UNSET
    line: int | Unset = UNSET
    link: str | Unset = UNSET
    message: str | Unset = UNSET
    path: str | Unset = UNSET
    report_key: str | Unset = UNSET
    severity: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        line = self.line

        link = self.link

        message = self.message

        path = self.path

        report_key = self.report_key

        severity = self.severity

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if line is not UNSET:
            field_dict["line"] = line
        if link is not UNSET:
            field_dict["link"] = link
        if message is not UNSET:
            field_dict["message"] = message
        if path is not UNSET:
            field_dict["path"] = path
        if report_key is not UNSET:
            field_dict["reportKey"] = report_key
        if severity is not UNSET:
            field_dict["severity"] = severity
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("externalId", UNSET)

        line = d.pop("line", UNSET)

        link = d.pop("link", UNSET)

        message = d.pop("message", UNSET)

        path = d.pop("path", UNSET)

        report_key = d.pop("reportKey", UNSET)

        severity = d.pop("severity", UNSET)

        type_ = d.pop("type", UNSET)

        rest_insight_annotation = cls(
            external_id=external_id,
            line=line,
            link=link,
            message=message,
            path=path,
            report_key=report_key,
            severity=severity,
            type_=type_,
        )

        rest_insight_annotation.additional_properties = d
        return rest_insight_annotation

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
