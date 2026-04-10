from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_node_connectivity_report_node import RestNodeConnectivityReportNode
    from ..models.rest_node_connectivity_summary import RestNodeConnectivitySummary


T = TypeVar("T", bound="RestNodeConnectivityReport")


@_attrs_define
class RestNodeConnectivityReport:
    node: RestNodeConnectivityReportNode | Unset = UNSET
    summaries: list[RestNodeConnectivitySummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        summaries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = []
            for summaries_item_data in self.summaries:
                summaries_item = summaries_item_data.to_dict()
                summaries.append(summaries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node is not UNSET:
            field_dict["node"] = node
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_node_connectivity_report_node import RestNodeConnectivityReportNode
        from ..models.rest_node_connectivity_summary import RestNodeConnectivitySummary

        d = dict(src_dict)
        _node = d.pop("node", UNSET)
        node: RestNodeConnectivityReportNode | Unset
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = RestNodeConnectivityReportNode.from_dict(_node)

        _summaries = d.pop("summaries", UNSET)
        summaries: list[RestNodeConnectivitySummary] | Unset = UNSET
        if _summaries is not UNSET:
            summaries = []
            for summaries_item_data in _summaries:
                summaries_item = RestNodeConnectivitySummary.from_dict(summaries_item_data)

                summaries.append(summaries_item)

        rest_node_connectivity_report = cls(
            node=node,
            summaries=summaries,
        )

        rest_node_connectivity_report.additional_properties = d
        return rest_node_connectivity_report

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
