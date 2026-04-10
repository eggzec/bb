from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_state import (
    RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_links import (
        RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginLinks,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_project import (
        RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginProject,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_related_links import (
        RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginRelatedLinks,
    )


T = TypeVar("T", bound="RestUserReactionCommentAnchorPullRequestToRefRepositoryOrigin")


@_attrs_define
class RestUserReactionCommentAnchorPullRequestToRefRepositoryOrigin:
    archived: bool | Unset = UNSET
    default_branch: str | Unset = UNSET
    description: str | Unset = UNSET
    forkable: bool | Unset = UNSET
    hierarchy_id: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginLinks | Unset = UNSET
    name: str | Unset = UNSET
    partition: int | Unset = UNSET
    project: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginProject | Unset = UNSET
    public: bool | Unset = UNSET
    related_links: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginRelatedLinks | Unset = UNSET
    scm_id: str | Unset = UNSET
    scope: str | Unset = UNSET
    slug: str | Unset = UNSET
    state: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginState | Unset = UNSET
    status_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        default_branch = self.default_branch

        description = self.description

        forkable = self.forkable

        hierarchy_id = self.hierarchy_id

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        partition = self.partition

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        public = self.public

        related_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_links, Unset):
            related_links = self.related_links.to_dict()

        scm_id = self.scm_id

        scope = self.scope

        slug = self.slug

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        status_message = self.status_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch
        if description is not UNSET:
            field_dict["description"] = description
        if forkable is not UNSET:
            field_dict["forkable"] = forkable
        if hierarchy_id is not UNSET:
            field_dict["hierarchyId"] = hierarchy_id
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if partition is not UNSET:
            field_dict["partition"] = partition
        if project is not UNSET:
            field_dict["project"] = project
        if public is not UNSET:
            field_dict["public"] = public
        if related_links is not UNSET:
            field_dict["relatedLinks"] = related_links
        if scm_id is not UNSET:
            field_dict["scmId"] = scm_id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if slug is not UNSET:
            field_dict["slug"] = slug
        if state is not UNSET:
            field_dict["state"] = state
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_links import (
            RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginLinks,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_project import (
            RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginProject,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin_related_links import (
            RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginRelatedLinks,
        )

        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        default_branch = d.pop("defaultBranch", UNSET)

        description = d.pop("description", UNSET)

        forkable = d.pop("forkable", UNSET)

        hierarchy_id = d.pop("hierarchyId", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        partition = d.pop("partition", UNSET)

        _project = d.pop("project", UNSET)
        project: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginProject.from_dict(_project)

        public = d.pop("public", UNSET)

        _related_links = d.pop("relatedLinks", UNSET)
        related_links: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginRelatedLinks | Unset
        if isinstance(_related_links, Unset):
            related_links = UNSET
        else:
            related_links = RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginRelatedLinks.from_dict(
                _related_links
            )

        scm_id = d.pop("scmId", UNSET)

        scope = d.pop("scope", UNSET)

        slug = d.pop("slug", UNSET)

        _state = d.pop("state", UNSET)
        state: RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestUserReactionCommentAnchorPullRequestToRefRepositoryOriginState(_state)

        status_message = d.pop("statusMessage", UNSET)

        rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin = cls(
            archived=archived,
            default_branch=default_branch,
            description=description,
            forkable=forkable,
            hierarchy_id=hierarchy_id,
            id=id,
            links=links,
            name=name,
            partition=partition,
            project=project,
            public=public,
            related_links=related_links,
            scm_id=scm_id,
            scope=scope,
            slug=slug,
            state=state,
            status_message=status_message,
        )

        rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin.additional_properties = d
        return rest_user_reaction_comment_anchor_pull_request_to_ref_repository_origin

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
