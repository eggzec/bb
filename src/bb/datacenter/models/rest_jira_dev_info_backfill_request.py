from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_repository_selector import RestRepositorySelector


T = TypeVar("T", bound="RestJiraDevInfoBackfillRequest")


@_attrs_define
class RestJiraDevInfoBackfillRequest:
    jira_site_ids: list[int]
    repositories: list[RestRepositorySelector]
    from_date: int | Unset = UNSET
    """ The starting timestamp in milliseconds for looking for backfill items, non-inclusive """
    to_date: int | Unset = UNSET
    """ The ending timestamp in milliseconds for looking for backfill items, non-inclusive """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jira_site_ids = self.jira_site_ids

        repositories = []
        for repositories_item_data in self.repositories:
            repositories_item = repositories_item_data.to_dict()
            repositories.append(repositories_item)

        from_date = self.from_date

        to_date = self.to_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jiraSiteIds": jira_site_ids,
                "repositories": repositories,
            }
        )
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_repository_selector import RestRepositorySelector

        d = dict(src_dict)
        jira_site_ids = cast(list[int], d.pop("jiraSiteIds"))

        repositories = []
        _repositories = d.pop("repositories")
        for repositories_item_data in _repositories:
            repositories_item = RestRepositorySelector.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        from_date = d.pop("fromDate", UNSET)

        to_date = d.pop("toDate", UNSET)

        rest_jira_dev_info_backfill_request = cls(
            jira_site_ids=jira_site_ids,
            repositories=repositories,
            from_date=from_date,
            to_date=to_date,
        )

        rest_jira_dev_info_backfill_request.additional_properties = d
        return rest_jira_dev_info_backfill_request

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
