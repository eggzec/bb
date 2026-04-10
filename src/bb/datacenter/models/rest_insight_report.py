from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_insight_report_result import RestInsightReportResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_insight_report_data import RestInsightReportData


T = TypeVar("T", bound="RestInsightReport")


@_attrs_define
class RestInsightReport:
    created_date: float | Unset = UNSET
    data: list[RestInsightReportData] | Unset = UNSET
    details: str | Unset = UNSET
    key: str | Unset = UNSET
    link: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    reporter: str | Unset = UNSET
    result: RestInsightReportResult | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date = self.created_date

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        details = self.details

        key = self.key

        link = self.link

        logo_url = self.logo_url

        reporter = self.reporter

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if data is not UNSET:
            field_dict["data"] = data
        if details is not UNSET:
            field_dict["details"] = details
        if key is not UNSET:
            field_dict["key"] = key
        if link is not UNSET:
            field_dict["link"] = link
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if result is not UNSET:
            field_dict["result"] = result
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_insight_report_data import RestInsightReportData

        d = dict(src_dict)
        created_date = d.pop("createdDate", UNSET)

        _data = d.pop("data", UNSET)
        data: list[RestInsightReportData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RestInsightReportData.from_dict(data_item_data)

                data.append(data_item)

        details = d.pop("details", UNSET)

        key = d.pop("key", UNSET)

        link = d.pop("link", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        reporter = d.pop("reporter", UNSET)

        _result = d.pop("result", UNSET)
        result: RestInsightReportResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = RestInsightReportResult(_result)

        title = d.pop("title", UNSET)

        rest_insight_report = cls(
            created_date=created_date,
            data=data,
            details=details,
            key=key,
            link=link,
            logo_url=logo_url,
            reporter=reporter,
            result=result,
            title=title,
        )

        rest_insight_report.additional_properties = d
        return rest_insight_report

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
