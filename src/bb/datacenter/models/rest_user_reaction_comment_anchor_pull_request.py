from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_reaction_comment_anchor_pull_request_state import RestUserReactionCommentAnchorPullRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_participant import RestPullRequestParticipant
    from ..models.rest_user_reaction_comment_anchor_pull_request_author import (
        RestUserReactionCommentAnchorPullRequestAuthor,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref import (
        RestUserReactionCommentAnchorPullRequestFromRef,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_links import (
        RestUserReactionCommentAnchorPullRequestLinks,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref import (
        RestUserReactionCommentAnchorPullRequestToRef,
    )


T = TypeVar("T", bound="RestUserReactionCommentAnchorPullRequest")


@_attrs_define
class RestUserReactionCommentAnchorPullRequest:
    author: RestUserReactionCommentAnchorPullRequestAuthor | Unset = UNSET
    closed: bool | Unset = UNSET
    closed_date: int | Unset = UNSET
    created_date: int | Unset = UNSET
    description: str | Unset = UNSET
    description_as_html: str | Unset = UNSET
    draft: bool | Unset = UNSET
    from_ref: RestUserReactionCommentAnchorPullRequestFromRef | Unset = UNSET
    html_description: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestUserReactionCommentAnchorPullRequestLinks | Unset = UNSET
    locked: bool | Unset = UNSET
    open_: bool | Unset = UNSET
    participants: list[RestPullRequestParticipant] | Unset = UNSET
    reviewers: list[RestPullRequestParticipant] | Unset = UNSET
    state: RestUserReactionCommentAnchorPullRequestState | Unset = UNSET
    title: str | Unset = UNSET
    to_ref: RestUserReactionCommentAnchorPullRequestToRef | Unset = UNSET
    updated_date: int | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        closed = self.closed

        closed_date = self.closed_date

        created_date = self.created_date

        description = self.description

        description_as_html = self.description_as_html

        draft = self.draft

        from_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_ref, Unset):
            from_ref = self.from_ref.to_dict()

        html_description = self.html_description

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        locked = self.locked

        open_ = self.open_

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        reviewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = reviewers_item_data.to_dict()
                reviewers.append(reviewers_item)

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        title = self.title

        to_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_ref, Unset):
            to_ref = self.to_ref.to_dict()

        updated_date = self.updated_date

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if closed is not UNSET:
            field_dict["closed"] = closed
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if description is not UNSET:
            field_dict["description"] = description
        if description_as_html is not UNSET:
            field_dict["descriptionAsHtml"] = description_as_html
        if draft is not UNSET:
            field_dict["draft"] = draft
        if from_ref is not UNSET:
            field_dict["fromRef"] = from_ref
        if html_description is not UNSET:
            field_dict["htmlDescription"] = html_description
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if locked is not UNSET:
            field_dict["locked"] = locked
        if open_ is not UNSET:
            field_dict["open"] = open_
        if participants is not UNSET:
            field_dict["participants"] = participants
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if to_ref is not UNSET:
            field_dict["toRef"] = to_ref
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_participant import RestPullRequestParticipant
        from ..models.rest_user_reaction_comment_anchor_pull_request_author import (
            RestUserReactionCommentAnchorPullRequestAuthor,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref import (
            RestUserReactionCommentAnchorPullRequestFromRef,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_links import (
            RestUserReactionCommentAnchorPullRequestLinks,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref import (
            RestUserReactionCommentAnchorPullRequestToRef,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: RestUserReactionCommentAnchorPullRequestAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = RestUserReactionCommentAnchorPullRequestAuthor.from_dict(_author)

        closed = d.pop("closed", UNSET)

        closed_date = d.pop("closedDate", UNSET)

        created_date = d.pop("createdDate", UNSET)

        description = d.pop("description", UNSET)

        description_as_html = d.pop("descriptionAsHtml", UNSET)

        draft = d.pop("draft", UNSET)

        _from_ref = d.pop("fromRef", UNSET)
        from_ref: RestUserReactionCommentAnchorPullRequestFromRef | Unset
        if isinstance(_from_ref, Unset):
            from_ref = UNSET
        else:
            from_ref = RestUserReactionCommentAnchorPullRequestFromRef.from_dict(_from_ref)

        html_description = d.pop("htmlDescription", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestUserReactionCommentAnchorPullRequestLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestUserReactionCommentAnchorPullRequestLinks.from_dict(_links)

        locked = d.pop("locked", UNSET)

        open_ = d.pop("open", UNSET)

        _participants = d.pop("participants", UNSET)
        participants: list[RestPullRequestParticipant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = RestPullRequestParticipant.from_dict(participants_item_data)

                participants.append(participants_item)

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: list[RestPullRequestParticipant] | Unset = UNSET
        if _reviewers is not UNSET:
            reviewers = []
            for reviewers_item_data in _reviewers:
                reviewers_item = RestPullRequestParticipant.from_dict(reviewers_item_data)

                reviewers.append(reviewers_item)

        _state = d.pop("state", UNSET)
        state: RestUserReactionCommentAnchorPullRequestState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestUserReactionCommentAnchorPullRequestState(_state)

        title = d.pop("title", UNSET)

        _to_ref = d.pop("toRef", UNSET)
        to_ref: RestUserReactionCommentAnchorPullRequestToRef | Unset
        if isinstance(_to_ref, Unset):
            to_ref = UNSET
        else:
            to_ref = RestUserReactionCommentAnchorPullRequestToRef.from_dict(_to_ref)

        updated_date = d.pop("updatedDate", UNSET)

        version = d.pop("version", UNSET)

        rest_user_reaction_comment_anchor_pull_request = cls(
            author=author,
            closed=closed,
            closed_date=closed_date,
            created_date=created_date,
            description=description,
            description_as_html=description_as_html,
            draft=draft,
            from_ref=from_ref,
            html_description=html_description,
            id=id,
            links=links,
            locked=locked,
            open_=open_,
            participants=participants,
            reviewers=reviewers,
            state=state,
            title=title,
            to_ref=to_ref,
            updated_date=updated_date,
            version=version,
        )

        rest_user_reaction_comment_anchor_pull_request.additional_properties = d
        return rest_user_reaction_comment_anchor_pull_request

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
