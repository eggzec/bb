from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_part_input_stream import FilePartInputStream


T = TypeVar("T", bound="FilePart")


@_attrs_define
class FilePart:
    content_type: str | Unset = UNSET
    form_field: bool | Unset = UNSET
    input_stream: FilePartInputStream | Unset = UNSET
    name: str | Unset = UNSET
    size: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        form_field = self.form_field

        input_stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_stream, Unset):
            input_stream = self.input_stream.to_dict()

        name = self.name

        size = self.size

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if form_field is not UNSET:
            field_dict["formField"] = form_field
        if input_stream is not UNSET:
            field_dict["inputStream"] = input_stream
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_part_input_stream import FilePartInputStream

        d = dict(src_dict)
        content_type = d.pop("contentType", UNSET)

        form_field = d.pop("formField", UNSET)

        _input_stream = d.pop("inputStream", UNSET)
        input_stream: FilePartInputStream | Unset
        if isinstance(_input_stream, Unset):
            input_stream = UNSET
        else:
            input_stream = FilePartInputStream.from_dict(_input_stream)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        value = d.pop("value", UNSET)

        file_part = cls(
            content_type=content_type,
            form_field=form_field,
            input_stream=input_stream,
            name=name,
            size=size,
            value=value,
        )

        file_part.additional_properties = d
        return file_part

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
