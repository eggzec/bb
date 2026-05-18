from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineSshPublicKey")


@_attrs_define
class PipelineSshPublicKey:
    type_: str | Unset = UNSET
    key_type: str | Unset = UNSET
    """ The type of the public key. """
    key: str | Unset = UNSET
    """ The base64 encoded public key. """
    md5_fingerprint: str | Unset = UNSET
    """ The MD5 fingerprint of the public key. """
    sha256_fingerprint: str | Unset = UNSET
    """ The SHA-256 fingerprint of the public key. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        key_type = self.key_type

        key = self.key

        md5_fingerprint = self.md5_fingerprint

        sha256_fingerprint = self.sha256_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key is not UNSET:
            field_dict["key"] = key
        if md5_fingerprint is not UNSET:
            field_dict["md5_fingerprint"] = md5_fingerprint
        if sha256_fingerprint is not UNSET:
            field_dict["sha256_fingerprint"] = sha256_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        key_type = d.pop("key_type", UNSET)

        key = d.pop("key", UNSET)

        md5_fingerprint = d.pop("md5_fingerprint", UNSET)

        sha256_fingerprint = d.pop("sha256_fingerprint", UNSET)

        pipeline_ssh_public_key = cls(
            type_=type_,
            key_type=key_type,
            key=key,
            md5_fingerprint=md5_fingerprint,
            sha256_fingerprint=sha256_fingerprint,
        )

        pipeline_ssh_public_key.additional_properties = d
        return pipeline_ssh_public_key

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
