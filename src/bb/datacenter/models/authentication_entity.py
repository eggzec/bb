from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationEntity")


@_attrs_define
class AuthenticationEntity:
    captcha_challenge: str | Unset = UNSET
    captcha_id: str | Unset = UNSET
    password: str | Unset = UNSET
    remember_me: bool | Unset = UNSET
    target_url: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captcha_challenge = self.captcha_challenge

        captcha_id = self.captcha_id

        password = self.password

        remember_me = self.remember_me

        target_url = self.target_url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captcha_challenge is not UNSET:
            field_dict["captchaChallenge"] = captcha_challenge
        if captcha_id is not UNSET:
            field_dict["captchaId"] = captcha_id
        if password is not UNSET:
            field_dict["password"] = password
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me
        if target_url is not UNSET:
            field_dict["targetUrl"] = target_url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        captcha_challenge = d.pop("captchaChallenge", UNSET)

        captcha_id = d.pop("captchaId", UNSET)

        password = d.pop("password", UNSET)

        remember_me = d.pop("rememberMe", UNSET)

        target_url = d.pop("targetUrl", UNSET)

        username = d.pop("username", UNSET)

        authentication_entity = cls(
            captcha_challenge=captcha_challenge,
            captcha_id=captcha_id,
            password=password,
            remember_me=remember_me,
            target_url=target_url,
            username=username,
        )

        authentication_entity.additional_properties = d
        return authentication_entity

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
