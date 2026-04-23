"""Live tests for ``bb.cloud.sdk.branches``."""

from __future__ import annotations

import pytest

from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.tag import Tag
from bb.cloud.sdk import branches
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_branches(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.list(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"branches.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"branches.list must return list, got {type(result).__name__}"
    )
    for idx, branch in enumerate(result):
        assert isinstance(branch, Branch), (
            f"branches.list[{idx}] is {type(branch).__name__}, expected Branch"
        )
        assert branch.name, f"branches.list[{idx}] has empty name: {branch!r}"


async def test_get_returns_branch(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_branch_name: str,
) -> None:
    result = await branches.get(client, workspace, probe_repo_slug, probe_branch_name)
    assert not isinstance(result, Error), (
        f"branches.get({probe_branch_name!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Branch), (
        f"branches.get must return Branch, got {type(result).__name__}"
    )
    assert result.name == probe_branch_name, (
        f"branches.get returned name={result.name!r}, expected {probe_branch_name!r}"
    )


async def test_get_missing_branch_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.get(
        client, workspace, probe_repo_slug, "this-branch-does-not-exist-zzz"
    )
    assert not isinstance(result, Branch), (
        f"branches.get for a nonexistent branch must not return Branch, got {result!r}"
    )


async def test_tags_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branches.tags(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"branches.tags errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"branches.tags must return list, got {type(result).__name__}"
    )
    for idx, tag in enumerate(result):
        assert isinstance(tag, Tag), (
            f"branches.tags[{idx}] is {type(tag).__name__}, expected Tag"
        )
