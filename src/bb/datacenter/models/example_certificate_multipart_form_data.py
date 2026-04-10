from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ExampleCertificateMultipartFormData")


@_attrs_define
class ExampleCertificateMultipartFormData:
    certificate: File | Unset = UNSET
    """ The X.509 certificate file to upload. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate: FileTypes | Unset = UNSET
        if not isinstance(self.certificate, Unset):
            certificate = self.certificate.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.certificate, Unset):
            files.append(("certificate", self.certificate.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _certificate = d.pop("certificate", UNSET)
        certificate: File | Unset
        if isinstance(_certificate, Unset):
            certificate = UNSET
        else:
            certificate = File(payload=BytesIO(_certificate))

        example_certificate_multipart_form_data = cls(
            certificate=certificate,
        )

        example_certificate_multipart_form_data.additional_properties = d
        return example_certificate_multipart_form_data

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
