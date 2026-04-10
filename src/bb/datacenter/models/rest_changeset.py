from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_changeset_changes import RestChangesetChanges
    from ..models.rest_changeset_from_commit import RestChangesetFromCommit
    from ..models.rest_changeset_links import RestChangesetLinks
    from ..models.rest_changeset_repository import RestChangesetRepository
    from ..models.rest_changeset_to_commit import RestChangesetToCommit


T = TypeVar("T", bound="RestChangeset")


@_attrs_define
class RestChangeset:
    changes: RestChangesetChanges | Unset = UNSET
    from_commit: RestChangesetFromCommit | Unset = UNSET
    links: RestChangesetLinks | Unset = UNSET
    repository: RestChangesetRepository | Unset = UNSET
    to_commit: RestChangesetToCommit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        from_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_commit, Unset):
            from_commit = self.from_commit.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        to_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_commit, Unset):
            to_commit = self.to_commit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changes is not UNSET:
            field_dict["changes"] = changes
        if from_commit is not UNSET:
            field_dict["fromCommit"] = from_commit
        if links is not UNSET:
            field_dict["links"] = links
        if repository is not UNSET:
            field_dict["repository"] = repository
        if to_commit is not UNSET:
            field_dict["toCommit"] = to_commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_changeset_changes import RestChangesetChanges
        from ..models.rest_changeset_from_commit import RestChangesetFromCommit
        from ..models.rest_changeset_links import RestChangesetLinks
        from ..models.rest_changeset_repository import RestChangesetRepository
        from ..models.rest_changeset_to_commit import RestChangesetToCommit

        d = dict(src_dict)
        _changes = d.pop("changes", UNSET)
        changes: RestChangesetChanges | Unset
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = RestChangesetChanges.from_dict(_changes)

        _from_commit = d.pop("fromCommit", UNSET)
        from_commit: RestChangesetFromCommit | Unset
        if isinstance(_from_commit, Unset):
            from_commit = UNSET
        else:
            from_commit = RestChangesetFromCommit.from_dict(_from_commit)

        _links = d.pop("links", UNSET)
        links: RestChangesetLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestChangesetLinks.from_dict(_links)

        _repository = d.pop("repository", UNSET)
        repository: RestChangesetRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestChangesetRepository.from_dict(_repository)

        _to_commit = d.pop("toCommit", UNSET)
        to_commit: RestChangesetToCommit | Unset
        if isinstance(_to_commit, Unset):
            to_commit = UNSET
        else:
            to_commit = RestChangesetToCommit.from_dict(_to_commit)

        rest_changeset = cls(
            changes=changes,
            from_commit=from_commit,
            links=links,
            repository=repository,
            to_commit=to_commit,
        )

        rest_changeset.additional_properties = d
        return rest_changeset

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
