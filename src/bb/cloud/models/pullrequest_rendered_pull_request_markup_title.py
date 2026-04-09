from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.pullrequest_rendered_pull_request_markup_title_markup import (
    PullrequestRenderedPullRequestMarkupTitleMarkup,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullrequestRenderedPullRequestMarkupTitle")


@_attrs_define
class PullrequestRenderedPullRequestMarkupTitle:
    raw: str | Unset = UNSET
    """ The text as it was typed by a user. """
    markup: PullrequestRenderedPullRequestMarkupTitleMarkup | Unset = UNSET
    """ The type of markup language the raw content is to be interpreted in. """
    html: str | Unset = UNSET
    """ The user's content rendered as HTML. """

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        markup: str | Unset = UNSET
        if not isinstance(self.markup, Unset):
            markup = self.markup.value

        html = self.html

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if markup is not UNSET:
            field_dict["markup"] = markup
        if html is not UNSET:
            field_dict["html"] = html

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw = d.pop("raw", UNSET)

        _markup = d.pop("markup", UNSET)
        markup: PullrequestRenderedPullRequestMarkupTitleMarkup | Unset
        if isinstance(_markup, Unset):
            markup = UNSET
        else:
            markup = PullrequestRenderedPullRequestMarkupTitleMarkup(_markup)

        html = d.pop("html", UNSET)

        pullrequest_rendered_pull_request_markup_title = cls(
            raw=raw,
            markup=markup,
            html=html,
        )

        return pullrequest_rendered_pull_request_markup_title
