from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_insight_report_data_value import RestInsightReportDataValue


T = TypeVar("T", bound="RestInsightReportData")


@_attrs_define
class RestInsightReportData:
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: RestInsightReportDataValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        type_ = self.type_

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_insight_report_data_value import RestInsightReportDataValue

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        _value = d.pop("value", UNSET)
        value: RestInsightReportDataValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RestInsightReportDataValue.from_dict(_value)

        rest_insight_report_data = cls(
            title=title,
            type_=type_,
            value=value,
        )

        rest_insight_report_data.additional_properties = d
        return rest_insight_report_data

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
