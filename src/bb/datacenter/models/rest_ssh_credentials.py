from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestSshCredentials")


@_attrs_define
class RestSshCredentials:
    public_key: str
    """ The public key text in the OpenSSH format. The algorithm must be specified in case of the legacy X.509 keys
    """
    username: str
    algorithm: str | Unset = UNSET
    """ The key algorithm, if passing in a legacy X.509 encoded key. Do not specify for OpenSSH encoded keys """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        username = self.username

        algorithm = self.algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicKey": public_key,
                "username": username,
            }
        )
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_key = d.pop("publicKey")

        username = d.pop("username")

        algorithm = d.pop("algorithm", UNSET)

        rest_ssh_credentials = cls(
            public_key=public_key,
            username=username,
            algorithm=algorithm,
        )

        rest_ssh_credentials.additional_properties = d
        return rest_ssh_credentials

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
