from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_data_type import ReportDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportData")


@_attrs_define
class ReportData:
    """A key-value element that will be displayed along with the report."""

    type_: ReportDataType | Unset = UNSET
    """ The type of data contained in the value field. If not provided, then the value will be detected as a
    boolean, number or string. """
    title: str | Unset = UNSET
    """ A string describing what this data field represents. """
    value: Any | Unset = UNSET
    """ The value of the data element. Can be a number, string, boolean, or object depending on the data type
    (PERCENTAGE, DATE, DURATION, TEXT, NUMBER, BOOLEAN, LINK). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        title = self.title

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ReportDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ReportDataType(_type_)

        title = d.pop("title", UNSET)

        value = d.pop("value", UNSET)

        report_data = cls(
            type_=type_,
            title=title,
            value=value,
        )

        report_data.additional_properties = d
        return report_data

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
