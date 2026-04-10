from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_mail_configuration_auth_type import RestMailConfigurationAuthType
from ..models.rest_mail_configuration_protocol import RestMailConfigurationProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMailConfiguration")


@_attrs_define
class RestMailConfiguration:
    auth_type: RestMailConfigurationAuthType | Unset = UNSET
    hostname: str | Unset = UNSET
    oauth_2_provider_id: str | Unset = UNSET
    password: str | Unset = UNSET
    port: int | Unset = UNSET
    protocol: RestMailConfigurationProtocol | Unset = UNSET
    require_start_tls: bool | Unset = UNSET
    sender_address: str | Unset = UNSET
    token_id: str | Unset = UNSET
    use_start_tls: bool | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        hostname = self.hostname

        oauth_2_provider_id = self.oauth_2_provider_id

        password = self.password

        port = self.port

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        require_start_tls = self.require_start_tls

        sender_address = self.sender_address

        token_id = self.token_id

        use_start_tls = self.use_start_tls

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if oauth_2_provider_id is not UNSET:
            field_dict["oauth2ProviderId"] = oauth_2_provider_id
        if password is not UNSET:
            field_dict["password"] = password
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if require_start_tls is not UNSET:
            field_dict["requireStartTls"] = require_start_tls
        if sender_address is not UNSET:
            field_dict["senderAddress"] = sender_address
        if token_id is not UNSET:
            field_dict["tokenId"] = token_id
        if use_start_tls is not UNSET:
            field_dict["useStartTls"] = use_start_tls
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_type = d.pop("authType", UNSET)
        auth_type: RestMailConfigurationAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = RestMailConfigurationAuthType(_auth_type)

        hostname = d.pop("hostname", UNSET)

        oauth_2_provider_id = d.pop("oauth2ProviderId", UNSET)

        password = d.pop("password", UNSET)

        port = d.pop("port", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: RestMailConfigurationProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = RestMailConfigurationProtocol(_protocol)

        require_start_tls = d.pop("requireStartTls", UNSET)

        sender_address = d.pop("senderAddress", UNSET)

        token_id = d.pop("tokenId", UNSET)

        use_start_tls = d.pop("useStartTls", UNSET)

        username = d.pop("username", UNSET)

        rest_mail_configuration = cls(
            auth_type=auth_type,
            hostname=hostname,
            oauth_2_provider_id=oauth_2_provider_id,
            password=password,
            port=port,
            protocol=protocol,
            require_start_tls=require_start_tls,
            sender_address=sender_address,
            token_id=token_id,
            use_start_tls=use_start_tls,
            username=username,
        )

        rest_mail_configuration.additional_properties = d
        return rest_mail_configuration

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
