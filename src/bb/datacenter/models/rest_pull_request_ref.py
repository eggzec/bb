from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_pull_request_ref_type import RestPullRequestRefType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_ref_repository import RestPullRequestRefRepository


T = TypeVar("T", bound="RestPullRequestRef")


@_attrs_define
class RestPullRequestRef:
    display_id: str | Unset = UNSET
    id: str | Unset = UNSET
    latest_commit: str | Unset = UNSET
    repository: RestPullRequestRefRepository | Unset = UNSET
    type_: RestPullRequestRefType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        latest_commit = self.latest_commit

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_id is not UNSET:
            field_dict["displayId"] = display_id
        if id is not UNSET:
            field_dict["id"] = id
        if latest_commit is not UNSET:
            field_dict["latestCommit"] = latest_commit
        if repository is not UNSET:
            field_dict["repository"] = repository
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_ref_repository import RestPullRequestRefRepository

        d = dict(src_dict)
        display_id = d.pop("displayId", UNSET)

        id = d.pop("id", UNSET)

        latest_commit = d.pop("latestCommit", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: RestPullRequestRefRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestPullRequestRefRepository.from_dict(_repository)

        _type_ = d.pop("type", UNSET)
        type_: RestPullRequestRefType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestPullRequestRefType(_type_)

        rest_pull_request_ref = cls(
            display_id=display_id,
            id=id,
            latest_commit=latest_commit,
            repository=repository,
            type_=type_,
        )

        rest_pull_request_ref.additional_properties = d
        return rest_pull_request_ref

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
