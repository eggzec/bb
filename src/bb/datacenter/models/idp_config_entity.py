from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.idp_config_entity_idp_type import IdpConfigEntityIdpType
from ..models.idp_config_entity_name_id_policy import IdpConfigEntityNameIdPolicy
from ..models.idp_config_entity_signature_algorithm import IdpConfigEntitySignatureAlgorithm
from ..models.idp_config_entity_sso_type import IdpConfigEntitySsoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jit_config_entity import JitConfigEntity


T = TypeVar("T", bound="IdpConfigEntity")


@_attrs_define
class IdpConfigEntity:
    additional_scopes: list[str] | Unset = UNSET
    authorization_endpoint: str | Unset = UNSET
    button_text: str | Unset = UNSET
    certificate: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    crowd_url: str | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    enable_remember_me: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: int | Unset = UNSET
    idp_type: IdpConfigEntityIdpType | Unset = UNSET
    include_customer_logins: bool | Unset = UNSET
    issuer_url: str | Unset = UNSET
    jit_configuration: JitConfigEntity | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    name_id_policy: IdpConfigEntityNameIdPolicy | Unset = UNSET
    sign_authnrequest: bool | Unset = UNSET
    signature_algorithm: IdpConfigEntitySignatureAlgorithm | Unset = UNSET
    sso_issuer: str | Unset = UNSET
    sso_type: IdpConfigEntitySsoType | Unset = UNSET
    sso_url: str | Unset = UNSET
    token_endpoint: str | Unset = UNSET
    userinfo_endpoint: str | Unset = UNSET
    username_attribute: str | Unset = UNSET
    username_claim: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_scopes: list[str] | Unset = UNSET
        if not isinstance(self.additional_scopes, Unset):
            additional_scopes = self.additional_scopes

        authorization_endpoint = self.authorization_endpoint

        button_text = self.button_text

        certificate = self.certificate

        client_id = self.client_id

        client_secret = self.client_secret

        crowd_url = self.crowd_url

        discovery_enabled = self.discovery_enabled

        enable_remember_me = self.enable_remember_me

        enabled = self.enabled

        id = self.id

        idp_type: str | Unset = UNSET
        if not isinstance(self.idp_type, Unset):
            idp_type = self.idp_type.value

        include_customer_logins = self.include_customer_logins

        issuer_url = self.issuer_url

        jit_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.jit_configuration, Unset):
            jit_configuration = self.jit_configuration.to_dict()

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        name = self.name

        name_id_policy: str | Unset = UNSET
        if not isinstance(self.name_id_policy, Unset):
            name_id_policy = self.name_id_policy.value

        sign_authnrequest = self.sign_authnrequest

        signature_algorithm: str | Unset = UNSET
        if not isinstance(self.signature_algorithm, Unset):
            signature_algorithm = self.signature_algorithm.value

        sso_issuer = self.sso_issuer

        sso_type: str | Unset = UNSET
        if not isinstance(self.sso_type, Unset):
            sso_type = self.sso_type.value

        sso_url = self.sso_url

        token_endpoint = self.token_endpoint

        userinfo_endpoint = self.userinfo_endpoint

        username_attribute = self.username_attribute

        username_claim = self.username_claim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_scopes is not UNSET:
            field_dict["additional-scopes"] = additional_scopes
        if authorization_endpoint is not UNSET:
            field_dict["authorization-endpoint"] = authorization_endpoint
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if client_id is not UNSET:
            field_dict["client-id"] = client_id
        if client_secret is not UNSET:
            field_dict["client-secret"] = client_secret
        if crowd_url is not UNSET:
            field_dict["crowd-url"] = crowd_url
        if discovery_enabled is not UNSET:
            field_dict["discovery-enabled"] = discovery_enabled
        if enable_remember_me is not UNSET:
            field_dict["enable-remember-me"] = enable_remember_me
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if idp_type is not UNSET:
            field_dict["idp-type"] = idp_type
        if include_customer_logins is not UNSET:
            field_dict["include-customer-logins"] = include_customer_logins
        if issuer_url is not UNSET:
            field_dict["issuer-url"] = issuer_url
        if jit_configuration is not UNSET:
            field_dict["jit-configuration"] = jit_configuration
        if last_updated is not UNSET:
            field_dict["last-updated"] = last_updated
        if name is not UNSET:
            field_dict["name"] = name
        if name_id_policy is not UNSET:
            field_dict["name-id-policy"] = name_id_policy
        if sign_authnrequest is not UNSET:
            field_dict["sign-authnrequest"] = sign_authnrequest
        if signature_algorithm is not UNSET:
            field_dict["signature-algorithm"] = signature_algorithm
        if sso_issuer is not UNSET:
            field_dict["sso-issuer"] = sso_issuer
        if sso_type is not UNSET:
            field_dict["sso-type"] = sso_type
        if sso_url is not UNSET:
            field_dict["sso-url"] = sso_url
        if token_endpoint is not UNSET:
            field_dict["token-endpoint"] = token_endpoint
        if userinfo_endpoint is not UNSET:
            field_dict["userinfo-endpoint"] = userinfo_endpoint
        if username_attribute is not UNSET:
            field_dict["username-attribute"] = username_attribute
        if username_claim is not UNSET:
            field_dict["username-claim"] = username_claim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jit_config_entity import JitConfigEntity

        d = dict(src_dict)
        additional_scopes = cast(list[str], d.pop("additional-scopes", UNSET))

        authorization_endpoint = d.pop("authorization-endpoint", UNSET)

        button_text = d.pop("buttonText", UNSET)

        certificate = d.pop("certificate", UNSET)

        client_id = d.pop("client-id", UNSET)

        client_secret = d.pop("client-secret", UNSET)

        crowd_url = d.pop("crowd-url", UNSET)

        discovery_enabled = d.pop("discovery-enabled", UNSET)

        enable_remember_me = d.pop("enable-remember-me", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _idp_type = d.pop("idp-type", UNSET)
        idp_type: IdpConfigEntityIdpType | Unset
        if isinstance(_idp_type, Unset):
            idp_type = UNSET
        else:
            idp_type = IdpConfigEntityIdpType(_idp_type)

        include_customer_logins = d.pop("include-customer-logins", UNSET)

        issuer_url = d.pop("issuer-url", UNSET)

        _jit_configuration = d.pop("jit-configuration", UNSET)
        jit_configuration: JitConfigEntity | Unset
        if isinstance(_jit_configuration, Unset):
            jit_configuration = UNSET
        else:
            jit_configuration = JitConfigEntity.from_dict(_jit_configuration)

        _last_updated = d.pop("last-updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        name = d.pop("name", UNSET)

        _name_id_policy = d.pop("name-id-policy", UNSET)
        name_id_policy: IdpConfigEntityNameIdPolicy | Unset
        if isinstance(_name_id_policy, Unset):
            name_id_policy = UNSET
        else:
            name_id_policy = IdpConfigEntityNameIdPolicy(_name_id_policy)

        sign_authnrequest = d.pop("sign-authnrequest", UNSET)

        _signature_algorithm = d.pop("signature-algorithm", UNSET)
        signature_algorithm: IdpConfigEntitySignatureAlgorithm | Unset
        if isinstance(_signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = IdpConfigEntitySignatureAlgorithm(_signature_algorithm)

        sso_issuer = d.pop("sso-issuer", UNSET)

        _sso_type = d.pop("sso-type", UNSET)
        sso_type: IdpConfigEntitySsoType | Unset
        if isinstance(_sso_type, Unset):
            sso_type = UNSET
        else:
            sso_type = IdpConfigEntitySsoType(_sso_type)

        sso_url = d.pop("sso-url", UNSET)

        token_endpoint = d.pop("token-endpoint", UNSET)

        userinfo_endpoint = d.pop("userinfo-endpoint", UNSET)

        username_attribute = d.pop("username-attribute", UNSET)

        username_claim = d.pop("username-claim", UNSET)

        idp_config_entity = cls(
            additional_scopes=additional_scopes,
            authorization_endpoint=authorization_endpoint,
            button_text=button_text,
            certificate=certificate,
            client_id=client_id,
            client_secret=client_secret,
            crowd_url=crowd_url,
            discovery_enabled=discovery_enabled,
            enable_remember_me=enable_remember_me,
            enabled=enabled,
            id=id,
            idp_type=idp_type,
            include_customer_logins=include_customer_logins,
            issuer_url=issuer_url,
            jit_configuration=jit_configuration,
            last_updated=last_updated,
            name=name,
            name_id_policy=name_id_policy,
            sign_authnrequest=sign_authnrequest,
            signature_algorithm=signature_algorithm,
            sso_issuer=sso_issuer,
            sso_type=sso_type,
            sso_url=sso_url,
            token_endpoint=token_endpoint,
            userinfo_endpoint=userinfo_endpoint,
            username_attribute=username_attribute,
            username_claim=username_claim,
        )

        idp_config_entity.additional_properties = d
        return idp_config_entity

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
