from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.repository import Repository


T = TypeVar("T", bound="PullRequestRef")


@_attrs_define
class PullRequestRef:
    display_id: str
    id: str
    latest_commit: str
    repository: Repository
    type_: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        latest_commit = self.latest_commit

        repository = self.repository.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayId": display_id,
                "id": id,
                "latestCommit": latest_commit,
                "repository": repository,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository import Repository

        d = dict(src_dict)
        display_id = d.pop("displayId")

        id = d.pop("id")

        latest_commit = d.pop("latestCommit")

        repository = Repository.from_dict(d.pop("repository"))

        type_ = d.pop("type")

        pull_request_ref = cls(
            display_id=display_id,
            id=id,
            latest_commit=latest_commit,
            repository=repository,
            type_=type_,
        )

        pull_request_ref.additional_properties = d
        return pull_request_ref

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
