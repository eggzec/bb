from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_state import (
    RestUserReactionCommentAnchorPullRequestFromRefRepositoryState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_links import (
        RestUserReactionCommentAnchorPullRequestFromRefRepositoryLinks,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_origin import (
        RestUserReactionCommentAnchorPullRequestFromRefRepositoryOrigin,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_project import (
        RestUserReactionCommentAnchorPullRequestFromRefRepositoryProject,
    )
    from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_related_links import (
        RestUserReactionCommentAnchorPullRequestFromRefRepositoryRelatedLinks,
    )


T = TypeVar("T", bound="RestUserReactionCommentAnchorPullRequestFromRefRepository")


@_attrs_define
class RestUserReactionCommentAnchorPullRequestFromRefRepository:
    archived: bool | Unset = UNSET
    default_branch: str | Unset = UNSET
    description: str | Unset = UNSET
    forkable: bool | Unset = UNSET
    hierarchy_id: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestUserReactionCommentAnchorPullRequestFromRefRepositoryLinks | Unset = UNSET
    name: str | Unset = UNSET
    origin: RestUserReactionCommentAnchorPullRequestFromRefRepositoryOrigin | Unset = UNSET
    partition: int | Unset = UNSET
    project: RestUserReactionCommentAnchorPullRequestFromRefRepositoryProject | Unset = UNSET
    public: bool | Unset = UNSET
    related_links: RestUserReactionCommentAnchorPullRequestFromRefRepositoryRelatedLinks | Unset = UNSET
    scm_id: str | Unset = UNSET
    scope: str | Unset = UNSET
    slug: str | Unset = UNSET
    state: RestUserReactionCommentAnchorPullRequestFromRefRepositoryState | Unset = UNSET
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

        origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

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
        if origin is not UNSET:
            field_dict["origin"] = origin
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
        from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_links import (
            RestUserReactionCommentAnchorPullRequestFromRefRepositoryLinks,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_origin import (
            RestUserReactionCommentAnchorPullRequestFromRefRepositoryOrigin,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_project import (
            RestUserReactionCommentAnchorPullRequestFromRefRepositoryProject,
        )
        from ..models.rest_user_reaction_comment_anchor_pull_request_from_ref_repository_related_links import (
            RestUserReactionCommentAnchorPullRequestFromRefRepositoryRelatedLinks,
        )

        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        default_branch = d.pop("defaultBranch", UNSET)

        description = d.pop("description", UNSET)

        forkable = d.pop("forkable", UNSET)

        hierarchy_id = d.pop("hierarchyId", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestUserReactionCommentAnchorPullRequestFromRefRepositoryLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestUserReactionCommentAnchorPullRequestFromRefRepositoryLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: RestUserReactionCommentAnchorPullRequestFromRefRepositoryOrigin | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = RestUserReactionCommentAnchorPullRequestFromRefRepositoryOrigin.from_dict(_origin)

        partition = d.pop("partition", UNSET)

        _project = d.pop("project", UNSET)
        project: RestUserReactionCommentAnchorPullRequestFromRefRepositoryProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RestUserReactionCommentAnchorPullRequestFromRefRepositoryProject.from_dict(_project)

        public = d.pop("public", UNSET)

        _related_links = d.pop("relatedLinks", UNSET)
        related_links: RestUserReactionCommentAnchorPullRequestFromRefRepositoryRelatedLinks | Unset
        if isinstance(_related_links, Unset):
            related_links = UNSET
        else:
            related_links = RestUserReactionCommentAnchorPullRequestFromRefRepositoryRelatedLinks.from_dict(
                _related_links
            )

        scm_id = d.pop("scmId", UNSET)

        scope = d.pop("scope", UNSET)

        slug = d.pop("slug", UNSET)

        _state = d.pop("state", UNSET)
        state: RestUserReactionCommentAnchorPullRequestFromRefRepositoryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestUserReactionCommentAnchorPullRequestFromRefRepositoryState(_state)

        status_message = d.pop("statusMessage", UNSET)

        rest_user_reaction_comment_anchor_pull_request_from_ref_repository = cls(
            archived=archived,
            default_branch=default_branch,
            description=description,
            forkable=forkable,
            hierarchy_id=hierarchy_id,
            id=id,
            links=links,
            name=name,
            origin=origin,
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

        rest_user_reaction_comment_anchor_pull_request_from_ref_repository.additional_properties = d
        return rest_user_reaction_comment_anchor_pull_request_from_ref_repository

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
