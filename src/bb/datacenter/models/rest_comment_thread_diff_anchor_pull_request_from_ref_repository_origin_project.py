from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project_type import (
    RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project_links import (
        RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectLinks,
    )


T = TypeVar("T", bound="RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProject")


@_attrs_define
class RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProject:
    key: str
    name: str
    type_: RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectType
    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectLinks | Unset = UNSET
    public: bool | Unset = UNSET
    scope: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        type_ = self.type_.value

        avatar = self.avatar

        avatar_url = self.avatar_url

        description = self.description

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        public = self.public

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "type": type_,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if public is not UNSET:
            field_dict["public"] = public
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project_links import (
            RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectLinks,
        )

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        type_ = RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectType(d.pop("type"))

        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestCommentThreadDiffAnchorPullRequestFromRefRepositoryOriginProjectLinks.from_dict(_links)

        public = d.pop("public", UNSET)

        scope = d.pop("scope", UNSET)

        rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project = cls(
            key=key,
            name=name,
            type_=type_,
            avatar=avatar,
            avatar_url=avatar_url,
            description=description,
            id=id,
            links=links,
            public=public,
            scope=scope,
        )

        rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project.additional_properties = d
        return rest_comment_thread_diff_anchor_pull_request_from_ref_repository_origin_project

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
