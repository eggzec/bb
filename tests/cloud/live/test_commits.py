"""Live tests for ``bb.cloud.sdk.commits``."""

from __future__ import annotations

import pytest

from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.commit import Commit
from bb.cloud.models.error import Error
from bb.cloud.sdk import commits
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_commits(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await commits.list(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"commits.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"commits.list must return list, got {type(result).__name__}"
    )
    for idx, commit in enumerate(result):
        assert isinstance(commit, BaseCommit), (
            f"commits.list[{idx}] is {type(commit).__name__}, expected BaseCommit"
        )
        assert commit.hash_, f"commits.list[{idx}] has empty hash: {commit!r}"


async def test_get_returns_commit(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    result = await commits.get(client, workspace, probe_repo_slug, probe_commit_hash)
    assert not isinstance(result, Error), (
        f"commits.get({probe_commit_hash!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Commit), (
        f"commits.get must return Commit, got {type(result).__name__}"
    )
    # The returned hash should either equal the probe hash exactly (full SHA)
    # or start with it (if the probe was abbreviated) / vice versa.
    assert result.hash_ and (
        result.hash_ == probe_commit_hash
        or result.hash_.startswith(probe_commit_hash)
        or probe_commit_hash.startswith(result.hash_)
    ), (
        f"commits.get returned hash={result.hash_!r}, expected {probe_commit_hash!r}"
    )


async def test_get_missing_commit_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await commits.get(
        client, workspace, probe_repo_slug, "0000000000000000000000000000000000000000"
    )
    assert not isinstance(result, Commit), (
        f"commits.get for a nonexistent hash must not return Commit, got {result!r}"
    )
