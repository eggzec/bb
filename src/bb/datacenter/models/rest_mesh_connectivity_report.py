from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_node_connectivity_report import RestNodeConnectivityReport


T = TypeVar("T", bound="RestMeshConnectivityReport")


@_attrs_define
class RestMeshConnectivityReport:
    reports: list[RestNodeConnectivityReport] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reports is not UNSET:
            field_dict["reports"] = reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_node_connectivity_report import RestNodeConnectivityReport

        d = dict(src_dict)
        _reports = d.pop("reports", UNSET)
        reports: list[RestNodeConnectivityReport] | Unset = UNSET
        if _reports is not UNSET:
            reports = []
            for reports_item_data in _reports:
                reports_item = RestNodeConnectivityReport.from_dict(reports_item_data)

                reports.append(reports_item)

        rest_mesh_connectivity_report = cls(
            reports=reports,
        )

        rest_mesh_connectivity_report.additional_properties = d
        return rest_mesh_connectivity_report

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
