from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_mirrored_repository_status import RestMirroredRepositoryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_named_link import RestNamedLink


T = TypeVar("T", bound="RestMirroredRepository")


@_attrs_define
class RestMirroredRepository:
    available: bool | Unset = UNSET
    clone_urls: list[RestNamedLink] | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    mirror_name: str | Unset = UNSET
    push_urls: list[RestNamedLink] | Unset = UNSET
    repository_id: str | Unset = UNSET
    status: RestMirroredRepositoryStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        clone_urls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clone_urls, Unset):
            clone_urls = []
            for clone_urls_item_data in self.clone_urls:
                clone_urls_item = clone_urls_item_data.to_dict()
                clone_urls.append(clone_urls_item)

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        mirror_name = self.mirror_name

        push_urls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.push_urls, Unset):
            push_urls = []
            for push_urls_item_data in self.push_urls:
                push_urls_item = push_urls_item_data.to_dict()
                push_urls.append(push_urls_item)

        repository_id = self.repository_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if clone_urls is not UNSET:
            field_dict["cloneUrls"] = clone_urls
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if mirror_name is not UNSET:
            field_dict["mirrorName"] = mirror_name
        if push_urls is not UNSET:
            field_dict["pushUrls"] = push_urls
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_named_link import RestNamedLink

        d = dict(src_dict)
        available = d.pop("available", UNSET)

        _clone_urls = d.pop("cloneUrls", UNSET)
        clone_urls: list[RestNamedLink] | Unset = UNSET
        if _clone_urls is not UNSET:
            clone_urls = []
            for clone_urls_item_data in _clone_urls:
                clone_urls_item = RestNamedLink.from_dict(clone_urls_item_data)

                clone_urls.append(clone_urls_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        mirror_name = d.pop("mirrorName", UNSET)

        _push_urls = d.pop("pushUrls", UNSET)
        push_urls: list[RestNamedLink] | Unset = UNSET
        if _push_urls is not UNSET:
            push_urls = []
            for push_urls_item_data in _push_urls:
                push_urls_item = RestNamedLink.from_dict(push_urls_item_data)

                push_urls.append(push_urls_item)

        repository_id = d.pop("repositoryId", UNSET)

        _status = d.pop("status", UNSET)
        status: RestMirroredRepositoryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RestMirroredRepositoryStatus(_status)

        rest_mirrored_repository = cls(
            available=available,
            clone_urls=clone_urls,
            last_updated=last_updated,
            mirror_name=mirror_name,
            push_urls=push_urls,
            repository_id=repository_id,
            status=status,
        )

        rest_mirrored_repository.additional_properties = d
        return rest_mirrored_repository

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
