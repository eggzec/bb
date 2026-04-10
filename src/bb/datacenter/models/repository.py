from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_state import RepositoryState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project


T = TypeVar("T", bound="Repository")


@_attrs_define
class Repository:
    hierarchy_id: str
    name: str
    project: Project
    scm_id: str
    slug: str
    state: RepositoryState
    status_message: str
    archived: bool | Unset = UNSET
    description: str | Unset = UNSET
    fork: bool | Unset = UNSET
    forkable: bool | Unset = UNSET
    id: int | Unset = UNSET
    local: bool | Unset = UNSET
    offline: bool | Unset = UNSET
    origin: Repository | Unset = UNSET
    partition: int | Unset = UNSET
    public: bool | Unset = UNSET
    read_only: bool | Unset = UNSET
    remote: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hierarchy_id = self.hierarchy_id

        name = self.name

        project = self.project.to_dict()

        scm_id = self.scm_id

        slug = self.slug

        state = self.state.value

        status_message = self.status_message

        archived = self.archived

        description = self.description

        fork = self.fork

        forkable = self.forkable

        id = self.id

        local = self.local

        offline = self.offline

        origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        partition = self.partition

        public = self.public

        read_only = self.read_only

        remote = self.remote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hierarchyId": hierarchy_id,
                "name": name,
                "project": project,
                "scmId": scm_id,
                "slug": slug,
                "state": state,
                "statusMessage": status_message,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived
        if description is not UNSET:
            field_dict["description"] = description
        if fork is not UNSET:
            field_dict["fork"] = fork
        if forkable is not UNSET:
            field_dict["forkable"] = forkable
        if id is not UNSET:
            field_dict["id"] = id
        if local is not UNSET:
            field_dict["local"] = local
        if offline is not UNSET:
            field_dict["offline"] = offline
        if origin is not UNSET:
            field_dict["origin"] = origin
        if partition is not UNSET:
            field_dict["partition"] = partition
        if public is not UNSET:
            field_dict["public"] = public
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if remote is not UNSET:
            field_dict["remote"] = remote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project import Project

        d = dict(src_dict)
        hierarchy_id = d.pop("hierarchyId")

        name = d.pop("name")

        project = Project.from_dict(d.pop("project"))

        scm_id = d.pop("scmId")

        slug = d.pop("slug")

        state = RepositoryState(d.pop("state"))

        status_message = d.pop("statusMessage")

        archived = d.pop("archived", UNSET)

        description = d.pop("description", UNSET)

        fork = d.pop("fork", UNSET)

        forkable = d.pop("forkable", UNSET)

        id = d.pop("id", UNSET)

        local = d.pop("local", UNSET)

        offline = d.pop("offline", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Repository | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Repository.from_dict(_origin)

        partition = d.pop("partition", UNSET)

        public = d.pop("public", UNSET)

        read_only = d.pop("readOnly", UNSET)

        remote = d.pop("remote", UNSET)

        repository = cls(
            hierarchy_id=hierarchy_id,
            name=name,
            project=project,
            scm_id=scm_id,
            slug=slug,
            state=state,
            status_message=status_message,
            archived=archived,
            description=description,
            fork=fork,
            forkable=forkable,
            id=id,
            local=local,
            offline=offline,
            origin=origin,
            partition=partition,
            public=public,
            read_only=read_only,
            remote=remote,
        )

        repository.additional_properties = d
        return repository

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
