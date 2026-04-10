from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_gpg_sub_key import RestGpgSubKey


T = TypeVar("T", bound="RestGpgKey")


@_attrs_define
class RestGpgKey:
    email_address: str | Unset = UNSET
    expiry_date: int | Unset = UNSET
    fingerprint: str | Unset = UNSET
    id: str | Unset = UNSET
    sub_keys: list[RestGpgSubKey] | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_address = self.email_address

        expiry_date = self.expiry_date

        fingerprint = self.fingerprint

        id = self.id

        sub_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_keys, Unset):
            sub_keys = []
            for sub_keys_item_data in self.sub_keys:
                sub_keys_item = sub_keys_item_data.to_dict()
                sub_keys.append(sub_keys_item)

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if id is not UNSET:
            field_dict["id"] = id
        if sub_keys is not UNSET:
            field_dict["subKeys"] = sub_keys
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_gpg_sub_key import RestGpgSubKey

        d = dict(src_dict)
        email_address = d.pop("emailAddress", UNSET)

        expiry_date = d.pop("expiryDate", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        id = d.pop("id", UNSET)

        _sub_keys = d.pop("subKeys", UNSET)
        sub_keys: list[RestGpgSubKey] | Unset = UNSET
        if _sub_keys is not UNSET:
            sub_keys = []
            for sub_keys_item_data in _sub_keys:
                sub_keys_item = RestGpgSubKey.from_dict(sub_keys_item_data)

                sub_keys.append(sub_keys_item)

        text = d.pop("text", UNSET)

        rest_gpg_key = cls(
            email_address=email_address,
            expiry_date=expiry_date,
            fingerprint=fingerprint,
            id=id,
            sub_keys=sub_keys,
            text=text,
        )

        rest_gpg_key.additional_properties = d
        return rest_gpg_key

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
