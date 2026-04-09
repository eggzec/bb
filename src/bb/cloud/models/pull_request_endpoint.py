from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pull_request_endpoint_pull_request_branch import PullRequestEndpointPullRequestBranch
    from ..models.pull_request_endpoint_pull_request_commit import PullRequestEndpointPullRequestCommit
    from ..models.repository import Repository


T = TypeVar("T", bound="PullRequestEndpoint")


@_attrs_define
class PullRequestEndpoint:
    repository: Repository | Unset = UNSET
    branch: PullRequestEndpointPullRequestBranch | Unset = UNSET
    commit: PullRequestEndpointPullRequestCommit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch, Unset):
            branch = self.branch.to_dict()

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if branch is not UNSET:
            field_dict["branch"] = branch
        if commit is not UNSET:
            field_dict["commit"] = commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pull_request_endpoint_pull_request_branch import PullRequestEndpointPullRequestBranch
        from ..models.pull_request_endpoint_pull_request_commit import PullRequestEndpointPullRequestCommit
        from ..models.repository import Repository

        d = dict(src_dict)
        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _branch = d.pop("branch", UNSET)
        branch: PullRequestEndpointPullRequestBranch | Unset
        if isinstance(_branch, Unset):
            branch = UNSET
        else:
            branch = PullRequestEndpointPullRequestBranch.from_dict(_branch)

        _commit = d.pop("commit", UNSET)
        commit: PullRequestEndpointPullRequestCommit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = PullRequestEndpointPullRequestCommit.from_dict(_commit)

        pull_request_endpoint = cls(
            repository=repository,
            branch=branch,
            commit=commit,
        )

        return pull_request_endpoint
