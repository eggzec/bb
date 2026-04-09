from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_report_type import ReportReportType
from ..models.report_result import ReportResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_data import ReportData


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    type_: str
    uuid: str | Unset = UNSET
    """ The UUID that can be used to identify the report. """
    title: str | Unset = UNSET
    """ The title of the report. """
    details: str | Unset = UNSET
    """ A string to describe the purpose of the report. """
    external_id: str | Unset = UNSET
    """ ID of the report provided by the report creator. It can be used to identify the report as an alternative to
    it's generated uuid. It is not used by Bitbucket, but only by the report creator for updating or deleting this
    specific report. Needs to be unique. """
    reporter: str | Unset = UNSET
    """ A string to describe the tool or company who created the report. """
    link: str | Unset = UNSET
    """ A URL linking to the results of the report in an external tool. """
    remote_link_enabled: bool | Unset = UNSET
    """ If enabled, a remote link is created in Jira for the work item associated with the commit the report belongs
    to. """
    logo_url: str | Unset = UNSET
    """ A URL to the report logo. If none is provided, the default insights logo will be used. """
    report_type: ReportReportType | Unset = UNSET
    """ The type of the report. """
    result: ReportResult | Unset = UNSET
    """ The state of the report. May be set to PENDING and later updated. """
    data: list[ReportData] | Unset = UNSET
    """ An array of data fields to display information on the report. Maximum 10. """
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the report was created. """
    updated_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the report was updated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        title = self.title

        details = self.details

        external_id = self.external_id

        reporter = self.reporter

        link = self.link

        remote_link_enabled = self.remote_link_enabled

        logo_url = self.logo_url

        report_type: str | Unset = UNSET
        if not isinstance(self.report_type, Unset):
            report_type = self.report_type.value

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if title is not UNSET:
            field_dict["title"] = title
        if details is not UNSET:
            field_dict["details"] = details
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if link is not UNSET:
            field_dict["link"] = link
        if remote_link_enabled is not UNSET:
            field_dict["remote_link_enabled"] = remote_link_enabled
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if report_type is not UNSET:
            field_dict["report_type"] = report_type
        if result is not UNSET:
            field_dict["result"] = result
        if data is not UNSET:
            field_dict["data"] = data
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_data import ReportData

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        title = d.pop("title", UNSET)

        details = d.pop("details", UNSET)

        external_id = d.pop("external_id", UNSET)

        reporter = d.pop("reporter", UNSET)

        link = d.pop("link", UNSET)

        remote_link_enabled = d.pop("remote_link_enabled", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        _report_type = d.pop("report_type", UNSET)
        report_type: ReportReportType | Unset
        if isinstance(_report_type, Unset):
            report_type = UNSET
        else:
            report_type = ReportReportType(_report_type)

        _result = d.pop("result", UNSET)
        result: ReportResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ReportResult(_result)

        _data = d.pop("data", UNSET)
        data: list[ReportData] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ReportData.from_dict(data_item_data)

                data.append(data_item)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        report = cls(
            type_=type_,
            uuid=uuid,
            title=title,
            details=details,
            external_id=external_id,
            reporter=reporter,
            link=link,
            remote_link_enabled=remote_link_enabled,
            logo_url=logo_url,
            report_type=report_type,
            result=result,
            data=data,
            created_on=created_on,
            updated_on=updated_on,
        )

        report.additional_properties = d
        return report

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
