from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_job_message_severity import RestJobMessageSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestJobMessage")


@_attrs_define
class RestJobMessage:
    created_date: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    severity: RestJobMessageSeverity | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        id = self.id

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if id is not UNSET:
            field_dict["id"] = id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        id = d.pop("id", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: RestJobMessageSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = RestJobMessageSeverity(_severity)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_job_message = cls(
            created_date=created_date,
            id=id,
            severity=severity,
            subject=subject,
            text=text,
        )

        rest_job_message.additional_properties = d
        return rest_job_message

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
