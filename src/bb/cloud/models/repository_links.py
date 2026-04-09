from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="RepositoryLinks")


@_attrs_define
class RepositoryLinks:
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    avatar: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    pullrequests: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    commits: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    forks: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    watchers: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    downloads: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    clone: list[Link] | Unset = UNSET
    hooks: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        pullrequests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pullrequests, Unset):
            pullrequests = self.pullrequests.to_dict()

        commits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commits, Unset):
            commits = self.commits.to_dict()

        forks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forks, Unset):
            forks = self.forks.to_dict()

        watchers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watchers, Unset):
            watchers = self.watchers.to_dict()

        downloads: dict[str, Any] | Unset = UNSET
        if not isinstance(self.downloads, Unset):
            downloads = self.downloads.to_dict()

        clone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clone, Unset):
            clone = []
            for clone_item_data in self.clone:
                clone_item = clone_item_data.to_dict()
                clone.append(clone_item)

        hooks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if html is not UNSET:
            field_dict["html"] = html
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if pullrequests is not UNSET:
            field_dict["pullrequests"] = pullrequests
        if commits is not UNSET:
            field_dict["commits"] = commits
        if forks is not UNSET:
            field_dict["forks"] = forks
        if watchers is not UNSET:
            field_dict["watchers"] = watchers
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if clone is not UNSET:
            field_dict["clone"] = clone
        if hooks is not UNSET:
            field_dict["hooks"] = hooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Link | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        _html = d.pop("html", UNSET)
        html: Link | Unset
        if isinstance(_html, Unset):
            html = UNSET
        else:
            html = Link.from_dict(_html)

        _avatar = d.pop("avatar", UNSET)
        avatar: Link | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Link.from_dict(_avatar)

        _pullrequests = d.pop("pullrequests", UNSET)
        pullrequests: Link | Unset
        if isinstance(_pullrequests, Unset):
            pullrequests = UNSET
        else:
            pullrequests = Link.from_dict(_pullrequests)

        _commits = d.pop("commits", UNSET)
        commits: Link | Unset
        if isinstance(_commits, Unset):
            commits = UNSET
        else:
            commits = Link.from_dict(_commits)

        _forks = d.pop("forks", UNSET)
        forks: Link | Unset
        if isinstance(_forks, Unset):
            forks = UNSET
        else:
            forks = Link.from_dict(_forks)

        _watchers = d.pop("watchers", UNSET)
        watchers: Link | Unset
        if isinstance(_watchers, Unset):
            watchers = UNSET
        else:
            watchers = Link.from_dict(_watchers)

        _downloads = d.pop("downloads", UNSET)
        downloads: Link | Unset
        if isinstance(_downloads, Unset):
            downloads = UNSET
        else:
            downloads = Link.from_dict(_downloads)

        _clone = d.pop("clone", UNSET)
        clone: list[Link] | Unset = UNSET
        if _clone is not UNSET:
            clone = []
            for clone_item_data in _clone:
                clone_item = Link.from_dict(clone_item_data)

                clone.append(clone_item)

        _hooks = d.pop("hooks", UNSET)
        hooks: Link | Unset
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = Link.from_dict(_hooks)

        repository_links = cls(
            self_=self_,
            html=html,
            avatar=avatar,
            pullrequests=pullrequests,
            commits=commits,
            forks=forks,
            watchers=watchers,
            downloads=downloads,
            clone=clone,
            hooks=hooks,
        )

        return repository_links
