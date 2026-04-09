from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestEndpointPullRequestCommit")


@_attrs_define
class PullRequestEndpointPullRequestCommit:
    hash_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash", UNSET)

        pull_request_endpoint_pull_request_commit = cls(
            hash_=hash_,
        )

        return pull_request_endpoint_pull_request_commit
