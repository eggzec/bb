from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.repository_fork_policy import RepositoryForkPolicy
from ..models.repository_scm import RepositoryScm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.branch import Branch
    from ..models.project import Project
    from ..models.repository_links import RepositoryLinks


T = TypeVar("T", bound="Repository")


@_attrs_define
class Repository:
    type_: str | Unset = UNSET
    links: RepositoryLinks | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The repository's immutable id. This can be used as a substitute for the slug segment in URLs. Doing this
    guarantees your URLs will survive renaming of the repository by its owner, or even transfer of the repository to
    a different user. """
    full_name: str | Unset = UNSET
    """ The concatenation of the repository owner's username and the slugified name, e.g. "evzijst/interruptingcow".
    This is the same string used in Bitbucket URLs. """
    is_private: bool | Unset = UNSET
    parent: None | Repository | Unset = UNSET
    scm: RepositoryScm | Unset = UNSET
    owner: Account | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    size: int | Unset = UNSET
    language: str | Unset = UNSET
    has_issues: bool | Unset = UNSET
    """
    The issue tracker for this repository is enabled. Issue Tracker
    features are not supported for repositories in workspaces
    administered through admin.atlassian.com.
     """
    has_wiki: bool | Unset = UNSET
    """
    The wiki for this repository is enabled. Wiki
    features are not supported for repositories in workspaces
    administered through admin.atlassian.com.
     """
    fork_policy: RepositoryForkPolicy | Unset = UNSET
    """
    Controls the rules for forking this repository.

    * **allow_forks**: unrestricted forking
    * **no_public_forks**: restrict forking to private forks (forks cannot
      be made public later)
    * **no_forks**: deny all forking
     """
    project: Project | Unset = UNSET
    mainbranch: Branch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        uuid = self.uuid

        full_name = self.full_name

        is_private = self.is_private

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, Repository):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        scm: str | Unset = UNSET
        if not isinstance(self.scm, Unset):
            scm = self.scm.value

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        name = self.name

        description = self.description

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        size = self.size

        language = self.language

        has_issues = self.has_issues

        has_wiki = self.has_wiki

        fork_policy: str | Unset = UNSET
        if not isinstance(self.fork_policy, Unset):
            fork_policy = self.fork_policy.value

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        mainbranch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mainbranch, Unset):
            mainbranch = self.mainbranch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if parent is not UNSET:
            field_dict["parent"] = parent
        if scm is not UNSET:
            field_dict["scm"] = scm
        if owner is not UNSET:
            field_dict["owner"] = owner
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if size is not UNSET:
            field_dict["size"] = size
        if language is not UNSET:
            field_dict["language"] = language
        if has_issues is not UNSET:
            field_dict["has_issues"] = has_issues
        if has_wiki is not UNSET:
            field_dict["has_wiki"] = has_wiki
        if fork_policy is not UNSET:
            field_dict["fork_policy"] = fork_policy
        if project is not UNSET:
            field_dict["project"] = project
        if mainbranch is not UNSET:
            field_dict["mainbranch"] = mainbranch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.branch import Branch
        from ..models.project import Project
        from ..models.repository_links import RepositoryLinks

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: RepositoryLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RepositoryLinks.from_dict(_links)

        uuid = d.pop("uuid", UNSET)

        full_name = d.pop("full_name", UNSET)

        is_private = d.pop("is_private", UNSET)

        def _parse_parent(data: object) -> None | Repository | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_0 = Repository.from_dict(data)

                return parent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Repository | Unset, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        _scm = d.pop("scm", UNSET)
        scm: RepositoryScm | Unset
        if isinstance(_scm, Unset):
            scm = UNSET
        else:
            scm = RepositoryScm(_scm)

        _owner = d.pop("owner", UNSET)
        owner: Account | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        size = d.pop("size", UNSET)

        language = d.pop("language", UNSET)

        has_issues = d.pop("has_issues", UNSET)

        has_wiki = d.pop("has_wiki", UNSET)

        _fork_policy = d.pop("fork_policy", UNSET)
        fork_policy: RepositoryForkPolicy | Unset
        if isinstance(_fork_policy, Unset):
            fork_policy = UNSET
        else:
            fork_policy = RepositoryForkPolicy(_fork_policy)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        _mainbranch = d.pop("mainbranch", UNSET)
        mainbranch: Branch | Unset
        if isinstance(_mainbranch, Unset):
            mainbranch = UNSET
        else:
            mainbranch = Branch.from_dict(_mainbranch)

        repository = cls(
            type_=type_,
            links=links,
            uuid=uuid,
            full_name=full_name,
            is_private=is_private,
            parent=parent,
            scm=scm,
            owner=owner,
            name=name,
            description=description,
            created_on=created_on,
            updated_on=updated_on,
            size=size,
            language=language,
            has_issues=has_issues,
            has_wiki=has_wiki,
            fork_policy=fork_policy,
            project=project,
            mainbranch=mainbranch,
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
