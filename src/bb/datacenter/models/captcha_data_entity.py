from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptchaDataEntity")


@_attrs_define
class CaptchaDataEntity:
    captcha_id: str | Unset = UNSET
    captcha_image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captcha_id = self.captcha_id

        captcha_image_url = self.captcha_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captcha_id is not UNSET:
            field_dict["captchaId"] = captcha_id
        if captcha_image_url is not UNSET:
            field_dict["captchaImageUrl"] = captcha_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        captcha_id = d.pop("captchaId", UNSET)

        captcha_image_url = d.pop("captchaImageUrl", UNSET)

        captcha_data_entity = cls(
            captcha_id=captcha_id,
            captcha_image_url=captcha_image_url,
        )

        captcha_data_entity.additional_properties = d
        return captcha_data_entity

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
