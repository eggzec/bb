from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.branchrestriction_branch_match_kind import BranchrestrictionBranchMatchKind
from ..models.branchrestriction_branch_type import BranchrestrictionBranchType
from ..models.branchrestriction_kind import BranchrestrictionKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.branchrestriction_links import BranchrestrictionLinks
    from ..models.group import Group


T = TypeVar("T", bound="Branchrestriction")


@_attrs_define
class Branchrestriction:
    kind: BranchrestrictionKind
    """ The type of restriction that is being applied. """
    branch_match_kind: BranchrestrictionBranchMatchKind
    """ Indicates how the restriction is matched against a branch. The default is `glob`. """
    pattern: str
    """ Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will
    be empty when `branch_match_kind` is `branching_model`. """
    type_: str | Unset = UNSET
    links: BranchrestrictionLinks | Unset = UNSET
    id: int | Unset = UNSET
    """ The branch restriction status' id. """
    branch_type: BranchrestrictionBranchType | Unset = UNSET
    """ Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The
    branch type will be calculated using the branching model configured for the repository. """
    value: int | Unset = UNSET
    """ Value with kind-specific semantics:

    * `require_approvals_to_merge` uses it to require a minimum number of approvals on a PR.

    * `require_default_reviewer_approvals_to_merge` uses it to require a minimum number of approvals from default
    reviewers on a PR.

    * `require_passing_builds_to_merge` uses it to require a minimum number of passing builds.

    * `require_commits_behind` uses it to require the current branch is up to a maximum number of commits behind it
    destination. """
    users: list[Account] | Unset = UNSET
    groups: list[Group] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        branch_match_kind = self.branch_match_kind.value

        pattern = self.pattern

        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        id = self.id

        branch_type: str | Unset = UNSET
        if not isinstance(self.branch_type, Unset):
            branch_type = self.branch_type.value

        value = self.value

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "branch_match_kind": branch_match_kind,
                "pattern": pattern,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if branch_type is not UNSET:
            field_dict["branch_type"] = branch_type
        if value is not UNSET:
            field_dict["value"] = value
        if users is not UNSET:
            field_dict["users"] = users
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.branchrestriction_links import BranchrestrictionLinks
        from ..models.group import Group

        d = dict(src_dict)
        kind = BranchrestrictionKind(d.pop("kind"))

        branch_match_kind = BranchrestrictionBranchMatchKind(d.pop("branch_match_kind"))

        pattern = d.pop("pattern")

        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: BranchrestrictionLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BranchrestrictionLinks.from_dict(_links)

        id = d.pop("id", UNSET)

        _branch_type = d.pop("branch_type", UNSET)
        branch_type: BranchrestrictionBranchType | Unset
        if isinstance(_branch_type, Unset):
            branch_type = UNSET
        else:
            branch_type = BranchrestrictionBranchType(_branch_type)

        value = d.pop("value", UNSET)

        _users = d.pop("users", UNSET)
        users: list[Account] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = Account.from_dict(users_item_data)

                users.append(users_item)

        _groups = d.pop("groups", UNSET)
        groups: list[Group] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = Group.from_dict(groups_item_data)

                groups.append(groups_item)

        branchrestriction = cls(
            kind=kind,
            branch_match_kind=branch_match_kind,
            pattern=pattern,
            type_=type_,
            links=links,
            id=id,
            branch_type=branch_type,
            value=value,
            users=users,
            groups=groups,
        )

        branchrestriction.additional_properties = d
        return branchrestriction

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
