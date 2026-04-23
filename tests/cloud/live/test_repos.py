"""Live tests for ``bb.cloud.sdk.repos``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.sdk import repos
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_repositories(client: BBClient, workspace: str) -> None:
    result = await repos.list(client, workspace, pagelen=10)
    assert not isinstance(result, Error), (
        f"repos.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"repos.list must return list, got {type(result).__name__}"
    for idx, repo in enumerate(result):
        assert isinstance(repo, Repository), (
            f"repos.list[{idx}] is {type(repo).__name__}, expected Repository"
        )
        assert repo.full_name, f"repos.list[{idx}] has empty full_name: {repo!r}"
        assert repo.full_name.startswith(f"{workspace}/") or workspace in str(repo.workspace), (
            f"repos.list[{idx}] full_name {repo.full_name!r} is not in workspace {workspace!r}"
        )


async def test_get_returns_expected_repo(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await repos.get(client, workspace, probe_repo_slug)
    assert not isinstance(result, Error), (
        f"repos.get({probe_repo_slug!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Repository), (
        f"repos.get must return Repository, got {type(result).__name__}"
    )
    assert result.full_name, f"repo has no full_name: {result!r}"
    assert probe_repo_slug in result.full_name, (
        f"repos.get returned full_name={result.full_name!r}, expected to contain {probe_repo_slug!r}"
    )


async def test_get_missing_repo_is_error_or_none(client: BBClient, workspace: str) -> None:
    result = await repos.get(client, workspace, "definitely-does-not-exist-zzz-9999")
    assert not isinstance(result, Repository), (
        f"repos.get for a nonexistent repo must not return Repository, got {result!r}"
    )


async def test_list_pagelen_does_not_affect_total_count(
    client: BBClient, workspace: str
) -> None:
    """Pagination integrity: page size must not change the total count."""
    small = await repos.list(client, workspace, pagelen=1)
    big = await repos.list(client, workspace, pagelen=50)
    assert not isinstance(small, Error), f"repos.list(pagelen=1) errored: {small!r}"
    assert not isinstance(big, Error), f"repos.list(pagelen=50) errored: {big!r}"
    assert len(small) == len(big), (
        f"pagination lost/duplicated items: pagelen=1 returned {len(small)} "
        f"but pagelen=50 returned {len(big)}"
    )
    # Slugs must match as a set, too.
    small_slugs = {r.full_name for r in small}
    big_slugs = {r.full_name for r in big}
    assert small_slugs == big_slugs, (
        f"pagination returned different repos at different page sizes: "
        f"only-in-small={small_slugs - big_slugs!r}, only-in-big={big_slugs - small_slugs!r}"
    )


async def test_forks_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await repos.forks(client, workspace, probe_repo_slug)
    if isinstance(result, Error):
        pytest.skip(
            f"repos.forks not available: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), f"repos.forks must return list, got {type(result).__name__}"
    for idx, fork in enumerate(result):
        assert isinstance(fork, Repository), (
            f"repos.forks[{idx}] is {type(fork).__name__}, expected Repository"
        )


async def test_watchers_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await repos.watchers(client, workspace, probe_repo_slug)
    if isinstance(result, Error):
        pytest.skip(
            f"repos.watchers not available: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"repos.watchers must return list, got {type(result).__name__}"
    )


async def test_my_permissions_returns_list(client: BBClient) -> None:
    result = await repos.my_permissions(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"repos.my_permissions errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"repos.my_permissions must return list, got {type(result).__name__}"
    )
