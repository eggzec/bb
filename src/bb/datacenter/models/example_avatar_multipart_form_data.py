from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ExampleAvatarMultipartFormData")


@_attrs_define
class ExampleAvatarMultipartFormData:
    avatar: File | Unset = UNSET
    """ The avatar file to upload. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: FileTypes | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.avatar, Unset):
            files.append(("avatar", self.avatar.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _avatar = d.pop("avatar", UNSET)
        avatar: File | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = File(payload=BytesIO(_avatar))

        example_avatar_multipart_form_data = cls(
            avatar=avatar,
        )

        example_avatar_multipart_form_data.additional_properties = d
        return example_avatar_multipart_form_data

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
