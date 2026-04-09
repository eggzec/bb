from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_annotation_annotation_type import ReportAnnotationAnnotationType
from ..models.report_annotation_result import ReportAnnotationResult
from ..models.report_annotation_severity import ReportAnnotationSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportAnnotation")


@_attrs_define
class ReportAnnotation:
    type_: str
    external_id: str | Unset = UNSET
    """ ID of the annotation provided by the annotation creator. It can be used to identify the annotation as an
    alternative to it's generated uuid. It is not used by Bitbucket, but only by the annotation creator for updating
    or deleting this specific annotation. Needs to be unique. """
    uuid: str | Unset = UNSET
    """ The UUID that can be used to identify the annotation. """
    annotation_type: ReportAnnotationAnnotationType | Unset = UNSET
    """ The type of the report. """
    path: str | Unset = UNSET
    """ The path of the file on which this annotation should be placed. This is the path of the file relative to the
    git repository. If no path is provided, then it will appear in the overview modal on all pull requests where the
    tip of the branch is the given commit, regardless of which files were modified. """
    line: int | Unset = UNSET
    """ The line number that the annotation should belong to. If no line number is provided, then it will default to
    0 and in a pull request it will appear at the top of the file specified by the path field. """
    summary: str | Unset = UNSET
    """ The message to display to users. """
    details: str | Unset = UNSET
    """ The details to show to users when clicking on the annotation. """
    result: ReportAnnotationResult | Unset = UNSET
    """ The state of the report. May be set to PENDING and later updated. """
    severity: ReportAnnotationSeverity | Unset = UNSET
    """ The severity of the annotation. """
    link: str | Unset = UNSET
    """ A URL linking to the annotation in an external tool. """
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the report was created. """
    updated_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the report was updated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        external_id = self.external_id

        uuid = self.uuid

        annotation_type: str | Unset = UNSET
        if not isinstance(self.annotation_type, Unset):
            annotation_type = self.annotation_type.value

        path = self.path

        line = self.line

        summary = self.summary

        details = self.details

        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        link = self.link

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
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if annotation_type is not UNSET:
            field_dict["annotation_type"] = annotation_type
        if path is not UNSET:
            field_dict["path"] = path
        if line is not UNSET:
            field_dict["line"] = line
        if summary is not UNSET:
            field_dict["summary"] = summary
        if details is not UNSET:
            field_dict["details"] = details
        if result is not UNSET:
            field_dict["result"] = result
        if severity is not UNSET:
            field_dict["severity"] = severity
        if link is not UNSET:
            field_dict["link"] = link
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        external_id = d.pop("external_id", UNSET)

        uuid = d.pop("uuid", UNSET)

        _annotation_type = d.pop("annotation_type", UNSET)
        annotation_type: ReportAnnotationAnnotationType | Unset
        if isinstance(_annotation_type, Unset):
            annotation_type = UNSET
        else:
            annotation_type = ReportAnnotationAnnotationType(_annotation_type)

        path = d.pop("path", UNSET)

        line = d.pop("line", UNSET)

        summary = d.pop("summary", UNSET)

        details = d.pop("details", UNSET)

        _result = d.pop("result", UNSET)
        result: ReportAnnotationResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ReportAnnotationResult(_result)

        _severity = d.pop("severity", UNSET)
        severity: ReportAnnotationSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = ReportAnnotationSeverity(_severity)

        link = d.pop("link", UNSET)

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

        report_annotation = cls(
            type_=type_,
            external_id=external_id,
            uuid=uuid,
            annotation_type=annotation_type,
            path=path,
            line=line,
            summary=summary,
            details=details,
            result=result,
            severity=severity,
            link=link,
            created_on=created_on,
            updated_on=updated_on,
        )

        report_annotation.additional_properties = d
        return report_annotation

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
