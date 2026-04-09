from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pullrequest_rendered_pull_request_markup_description import (
        PullrequestRenderedPullRequestMarkupDescription,
    )
    from ..models.pullrequest_rendered_pull_request_markup_reason import PullrequestRenderedPullRequestMarkupReason
    from ..models.pullrequest_rendered_pull_request_markup_title import PullrequestRenderedPullRequestMarkupTitle


T = TypeVar("T", bound="PullrequestRenderedPullRequestMarkup")


@_attrs_define
class PullrequestRenderedPullRequestMarkup:
    """User provided pull request text, interpreted in a markup language and rendered in HTML"""

    title: PullrequestRenderedPullRequestMarkupTitle | Unset = UNSET
    description: PullrequestRenderedPullRequestMarkupDescription | Unset = UNSET
    reason: PullrequestRenderedPullRequestMarkupReason | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pullrequest_rendered_pull_request_markup_description import (
            PullrequestRenderedPullRequestMarkupDescription,
        )
        from ..models.pullrequest_rendered_pull_request_markup_reason import PullrequestRenderedPullRequestMarkupReason
        from ..models.pullrequest_rendered_pull_request_markup_title import PullrequestRenderedPullRequestMarkupTitle

        d = dict(src_dict)
        _title = d.pop("title", UNSET)
        title: PullrequestRenderedPullRequestMarkupTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = PullrequestRenderedPullRequestMarkupTitle.from_dict(_title)

        _description = d.pop("description", UNSET)
        description: PullrequestRenderedPullRequestMarkupDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = PullrequestRenderedPullRequestMarkupDescription.from_dict(_description)

        _reason = d.pop("reason", UNSET)
        reason: PullrequestRenderedPullRequestMarkupReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = PullrequestRenderedPullRequestMarkupReason.from_dict(_reason)

        pullrequest_rendered_pull_request_markup = cls(
            title=title,
            description=description,
            reason=reason,
        )

        return pullrequest_rendered_pull_request_markup
