from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_insight_report_data import RestInsightReportData


T = TypeVar("T", bound="RestSetInsightReportRequest")


@_attrs_define
class RestSetInsightReportRequest:
    data: list[RestInsightReportData]
    title: str
    coverage_provider_key: str | Unset = UNSET
    created_date: int | Unset = UNSET
    details: str | Unset = UNSET
    link: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    reporter: str | Unset = UNSET
    result: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        title = self.title

        coverage_provider_key = self.coverage_provider_key

        created_date = self.created_date

        details = self.details

        link = self.link

        logo_url = self.logo_url

        reporter = self.reporter

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "title": title,
            }
        )
        if coverage_provider_key is not UNSET:
            field_dict["coverageProviderKey"] = coverage_provider_key
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if details is not UNSET:
            field_dict["details"] = details
        if link is not UNSET:
            field_dict["link"] = link
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_insight_report_data import RestInsightReportData

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = RestInsightReportData.from_dict(data_item_data)

            data.append(data_item)

        title = d.pop("title")

        coverage_provider_key = d.pop("coverageProviderKey", UNSET)

        created_date = d.pop("createdDate", UNSET)

        details = d.pop("details", UNSET)

        link = d.pop("link", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        reporter = d.pop("reporter", UNSET)

        result = d.pop("result", UNSET)

        rest_set_insight_report_request = cls(
            data=data,
            title=title,
            coverage_provider_key=coverage_provider_key,
            created_date=created_date,
            details=details,
            link=link,
            logo_url=logo_url,
            reporter=reporter,
            result=result,
        )

        rest_set_insight_report_request.additional_properties = d
        return rest_set_insight_report_request

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
