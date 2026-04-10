from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSshKeyBody")


@_attrs_define
class AddSshKeyBody:
    algorithm_type: str | Unset = UNSET
    bit_length: int | Unset = UNSET
    created_date: datetime.datetime | Unset = UNSET
    expiry_days: int | Unset = UNSET
    fingerprint: str | Unset = UNSET
    id: int | Unset = UNSET
    label: str | Unset = UNSET
    last_authenticated: str | Unset = UNSET
    text: str | Unset = UNSET
    warning: str | Unset = UNSET
    """ Contains a warning about the key, for example that it's deprecated """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm_type = self.algorithm_type

        bit_length = self.bit_length

        created_date: str | Unset = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        expiry_days = self.expiry_days

        fingerprint = self.fingerprint

        id = self.id

        label = self.label

        last_authenticated = self.last_authenticated

        text = self.text

        warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm_type is not UNSET:
            field_dict["algorithmType"] = algorithm_type
        if bit_length is not UNSET:
            field_dict["bitLength"] = bit_length
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if expiry_days is not UNSET:
            field_dict["expiryDays"] = expiry_days
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if last_authenticated is not UNSET:
            field_dict["lastAuthenticated"] = last_authenticated
        if text is not UNSET:
            field_dict["text"] = text
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm_type = d.pop("algorithmType", UNSET)

        bit_length = d.pop("bitLength", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: datetime.datetime | Unset
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        expiry_days = d.pop("expiryDays", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        last_authenticated = d.pop("lastAuthenticated", UNSET)

        text = d.pop("text", UNSET)

        warning = d.pop("warning", UNSET)

        add_ssh_key_body = cls(
            algorithm_type=algorithm_type,
            bit_length=bit_length,
            created_date=created_date,
            expiry_days=expiry_days,
            fingerprint=fingerprint,
            id=id,
            label=label,
            last_authenticated=last_authenticated,
            text=text,
            warning=warning,
        )

        add_ssh_key_body.additional_properties = d
        return add_ssh_key_body

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
