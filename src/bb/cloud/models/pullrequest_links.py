from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="PullrequestLinks")


@_attrs_define
class PullrequestLinks:
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    commits: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    approve: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    diff: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    diffstat: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    comments: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    activity: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    merge: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    decline: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        commits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commits, Unset):
            commits = self.commits.to_dict()

        approve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.approve, Unset):
            approve = self.approve.to_dict()

        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        diffstat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diffstat, Unset):
            diffstat = self.diffstat.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        activity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        merge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge, Unset):
            merge = self.merge.to_dict()

        decline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decline, Unset):
            decline = self.decline.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if html is not UNSET:
            field_dict["html"] = html
        if commits is not UNSET:
            field_dict["commits"] = commits
        if approve is not UNSET:
            field_dict["approve"] = approve
        if diff is not UNSET:
            field_dict["diff"] = diff
        if diffstat is not UNSET:
            field_dict["diffstat"] = diffstat
        if comments is not UNSET:
            field_dict["comments"] = comments
        if activity is not UNSET:
            field_dict["activity"] = activity
        if merge is not UNSET:
            field_dict["merge"] = merge
        if decline is not UNSET:
            field_dict["decline"] = decline

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

        _commits = d.pop("commits", UNSET)
        commits: Link | Unset
        if isinstance(_commits, Unset):
            commits = UNSET
        else:
            commits = Link.from_dict(_commits)

        _approve = d.pop("approve", UNSET)
        approve: Link | Unset
        if isinstance(_approve, Unset):
            approve = UNSET
        else:
            approve = Link.from_dict(_approve)

        _diff = d.pop("diff", UNSET)
        diff: Link | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = Link.from_dict(_diff)

        _diffstat = d.pop("diffstat", UNSET)
        diffstat: Link | Unset
        if isinstance(_diffstat, Unset):
            diffstat = UNSET
        else:
            diffstat = Link.from_dict(_diffstat)

        _comments = d.pop("comments", UNSET)
        comments: Link | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = Link.from_dict(_comments)

        _activity = d.pop("activity", UNSET)
        activity: Link | Unset
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = Link.from_dict(_activity)

        _merge = d.pop("merge", UNSET)
        merge: Link | Unset
        if isinstance(_merge, Unset):
            merge = UNSET
        else:
            merge = Link.from_dict(_merge)

        _decline = d.pop("decline", UNSET)
        decline: Link | Unset
        if isinstance(_decline, Unset):
            decline = UNSET
        else:
            decline = Link.from_dict(_decline)

        pullrequest_links = cls(
            self_=self_,
            html=html,
            commits=commits,
            approve=approve,
            diff=diff,
            diffstat=diffstat,
            comments=comments,
            activity=activity,
            merge=merge,
            decline=decline,
        )

        return pullrequest_links
