from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pullrequest_state import PullrequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.participant import Participant
    from ..models.pull_request_endpoint import PullRequestEndpoint
    from ..models.pullrequest_links import PullrequestLinks
    from ..models.pullrequest_pull_request_commit import PullrequestPullRequestCommit
    from ..models.pullrequest_rendered_pull_request_markup import PullrequestRenderedPullRequestMarkup
    from ..models.pullrequest_summary import PullrequestSummary


T = TypeVar("T", bound="Pullrequest")


@_attrs_define
class Pullrequest:
    type_: str
    links: PullrequestLinks | Unset = UNSET
    id: int | Unset = UNSET
    """ The pull request's unique ID. Note that pull request IDs are only unique within their associated repository.
    """
    title: str | Unset = UNSET
    """ Title of the pull request. """
    rendered: PullrequestRenderedPullRequestMarkup | Unset = UNSET
    """ User provided pull request text, interpreted in a markup language and rendered in HTML """
    summary: PullrequestSummary | Unset = UNSET
    state: PullrequestState | Unset = UNSET
    """ The pull request's current status. """
    author: Account | Unset = UNSET
    source: PullRequestEndpoint | Unset = UNSET
    destination: PullRequestEndpoint | Unset = UNSET
    merge_commit: PullrequestPullRequestCommit | Unset = UNSET
    comment_count: int | Unset = UNSET
    """ The number of comments for a specific pull request. """
    task_count: int | Unset = UNSET
    """ The number of open tasks for a specific pull request. """
    close_source_branch: bool | Unset = UNSET
    """ A boolean flag indicating if merging the pull request closes the source branch. """
    closed_by: Account | Unset = UNSET
    reason: str | Unset = UNSET
    """ Explains why a pull request was declined. This field is only applicable to pull requests in rejected state.
    """
    created_on: datetime.datetime | Unset = UNSET
    """ The ISO8601 timestamp the request was created. """
    updated_on: datetime.datetime | Unset = UNSET
    """ The ISO8601 timestamp the request was last updated. """
    reviewers: list[Account] | Unset = UNSET
    """ The list of users that were added as reviewers on this pull request when it was created. For performance
    reasons, the API only includes this list on a pull request's `self` URL. """
    participants: list[Participant] | Unset = UNSET
    """         The list of users that are collaborating on this pull request.
            Collaborators are user that:

            * are added to the pull request as a reviewer (part of the reviewers
              list)
            * are not explicit reviewers, but have commented on the pull request
            * are not explicit reviewers, but have approved the pull request

            Each user is wrapped in an object that indicates the user's role and
            whether they have approved the pull request. For performance reasons,
            the API only returns this list when an API requests a pull request by
            id.
             """
    draft: bool | Unset = UNSET
    """ A boolean flag indicating whether the pull request is a draft. """
    queued: bool | Unset = UNSET
    """ A boolean flag indicating whether the pull request is queued """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        id = self.id

        title = self.title

        rendered: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rendered, Unset):
            rendered = self.rendered.to_dict()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        merge_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_commit, Unset):
            merge_commit = self.merge_commit.to_dict()

        comment_count = self.comment_count

        task_count = self.task_count

        close_source_branch = self.close_source_branch

        closed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.closed_by, Unset):
            closed_by = self.closed_by.to_dict()

        reason = self.reason

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        reviewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = reviewers_item_data.to_dict()
                reviewers.append(reviewers_item)

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        draft = self.draft

        queued = self.queued

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if rendered is not UNSET:
            field_dict["rendered"] = rendered
        if summary is not UNSET:
            field_dict["summary"] = summary
        if state is not UNSET:
            field_dict["state"] = state
        if author is not UNSET:
            field_dict["author"] = author
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination
        if merge_commit is not UNSET:
            field_dict["merge_commit"] = merge_commit
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if task_count is not UNSET:
            field_dict["task_count"] = task_count
        if close_source_branch is not UNSET:
            field_dict["close_source_branch"] = close_source_branch
        if closed_by is not UNSET:
            field_dict["closed_by"] = closed_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if participants is not UNSET:
            field_dict["participants"] = participants
        if draft is not UNSET:
            field_dict["draft"] = draft
        if queued is not UNSET:
            field_dict["queued"] = queued

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.participant import Participant
        from ..models.pull_request_endpoint import PullRequestEndpoint
        from ..models.pullrequest_links import PullrequestLinks
        from ..models.pullrequest_pull_request_commit import PullrequestPullRequestCommit
        from ..models.pullrequest_rendered_pull_request_markup import PullrequestRenderedPullRequestMarkup
        from ..models.pullrequest_summary import PullrequestSummary

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: PullrequestLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PullrequestLinks.from_dict(_links)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _rendered = d.pop("rendered", UNSET)
        rendered: PullrequestRenderedPullRequestMarkup | Unset
        if isinstance(_rendered, Unset):
            rendered = UNSET
        else:
            rendered = PullrequestRenderedPullRequestMarkup.from_dict(_rendered)

        _summary = d.pop("summary", UNSET)
        summary: PullrequestSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = PullrequestSummary.from_dict(_summary)

        _state = d.pop("state", UNSET)
        state: PullrequestState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PullrequestState(_state)

        _author = d.pop("author", UNSET)
        author: Account | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = Account.from_dict(_author)

        _source = d.pop("source", UNSET)
        source: PullRequestEndpoint | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PullRequestEndpoint.from_dict(_source)

        _destination = d.pop("destination", UNSET)
        destination: PullRequestEndpoint | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = PullRequestEndpoint.from_dict(_destination)

        _merge_commit = d.pop("merge_commit", UNSET)
        merge_commit: PullrequestPullRequestCommit | Unset
        if isinstance(_merge_commit, Unset):
            merge_commit = UNSET
        else:
            merge_commit = PullrequestPullRequestCommit.from_dict(_merge_commit)

        comment_count = d.pop("comment_count", UNSET)

        task_count = d.pop("task_count", UNSET)

        close_source_branch = d.pop("close_source_branch", UNSET)

        _closed_by = d.pop("closed_by", UNSET)
        closed_by: Account | Unset
        if isinstance(_closed_by, Unset):
            closed_by = UNSET
        else:
            closed_by = Account.from_dict(_closed_by)

        reason = d.pop("reason", UNSET)

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

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: list[Account] | Unset = UNSET
        if _reviewers is not UNSET:
            reviewers = []
            for reviewers_item_data in _reviewers:
                reviewers_item = Account.from_dict(reviewers_item_data)

                reviewers.append(reviewers_item)

        _participants = d.pop("participants", UNSET)
        participants: list[Participant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = Participant.from_dict(participants_item_data)

                participants.append(participants_item)

        draft = d.pop("draft", UNSET)

        queued = d.pop("queued", UNSET)

        pullrequest = cls(
            type_=type_,
            links=links,
            id=id,
            title=title,
            rendered=rendered,
            summary=summary,
            state=state,
            author=author,
            source=source,
            destination=destination,
            merge_commit=merge_commit,
            comment_count=comment_count,
            task_count=task_count,
            close_source_branch=close_source_branch,
            closed_by=closed_by,
            reason=reason,
            created_on=created_on,
            updated_on=updated_on,
            reviewers=reviewers,
            participants=participants,
            draft=draft,
            queued=queued,
        )

        pullrequest.additional_properties = d
        return pullrequest

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
