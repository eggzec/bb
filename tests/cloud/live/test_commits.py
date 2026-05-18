"""Live tests for ``bb.cloud.sdk.commits``.

Seed data (never mutate):
- workspace:   beaverish
- repo:        bb-probe
- commit hash: 84952fad87fb39e3c6d61811a93769378dd4fad7
"""

from __future__ import annotations

import pytest

from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.commit import Commit
from bb.cloud.models.error import Error
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk import commits
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Seed constants
# ---------------------------------------------------------------------------
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_REPO = "bb-probe"


# ---------------------------------------------------------------------------
# TC-COMMITS-001 / TC-COMMITS-002: list
# ---------------------------------------------------------------------------


async def test_list_returns_commits(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """TC-COMMITS-001: list returns a non-empty list of BaseCommit objects."""
    result = await commits.list(client, workspace, probe_repo_slug, pagelen=10)
    assert not isinstance(result, Error), (
        f"commits.list errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), (
        f"commits.list must return list, got {type(result).__name__}"
    )
    assert result, f"commits.list returned an empty list for repo {probe_repo_slug!r}"
    for idx, commit in enumerate(result):
        assert isinstance(commit, BaseCommit), (
            f"commits.list[{idx}] is {type(commit).__name__}, expected BaseCommit"
        )
        assert commit.hash_, f"commits.list[{idx}] has empty hash: {commit!r}"


async def test_list_pagelen_integrity(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """TC-COMMITS-002: different pagelen values return the same total commit set."""
    small = await commits.list(client, workspace, probe_repo_slug, pagelen=1)
    large = await commits.list(client, workspace, probe_repo_slug, pagelen=5)

    assert not isinstance(small, Error), f"commits.list(pagelen=1) errored: {small!r}"
    assert not isinstance(large, Error), f"commits.list(pagelen=5) errored: {large!r}"

    assert len(small) == len(large), (
        f"pagination changed total: pagelen=1 gave {len(small)} commits, "
        f"pagelen=5 gave {len(large)} commits"
    )

    small_hashes = {c.hash_ for c in small if c.hash_}
    large_hashes = {c.hash_ for c in large if c.hash_}
    assert small_hashes == large_hashes, (
        f"pagination returned different commits at different page sizes: "
        f"only-in-small={small_hashes - large_hashes!r}, "
        f"only-in-large={large_hashes - small_hashes!r}"
    )


# ---------------------------------------------------------------------------
# TC-COMMITS-003 / TC-COMMITS-004: get
# ---------------------------------------------------------------------------


async def test_get_known_commit(
    client: BBClient, workspace: str
) -> None:
    """TC-COMMITS-003: get the seeded commit by its full hash."""
    result = await commits.get(client, workspace, SEED_REPO, SEED_COMMIT)
    assert not isinstance(result, Error), (
        f"commits.get({SEED_COMMIT!r}) errored: "
        f"{result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, Commit), (
        f"commits.get must return Commit for known hash, got {type(result).__name__}"
    )
    assert result.hash_ == SEED_COMMIT, (
        f"commits.get returned hash={result.hash_!r}, expected {SEED_COMMIT!r}"
    )


async def test_get_probe_commit_via_fixture(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    """TC-COMMITS-003 (fixture variant): get a commit discovered via the fixture."""
    result = await commits.get(client, workspace, probe_repo_slug, probe_commit_hash)
    assert not isinstance(result, Error), (
        f"commits.get({probe_commit_hash!r}) errored: "
        f"{result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, Commit), (
        f"commits.get must return Commit, got {type(result).__name__}"
    )
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
    """TC-COMMITS-004: a nonexistent hash must not raise — return Error or None."""
    result = await commits.get(
        client, workspace, probe_repo_slug, "0000000000000000000000000000000000000000"
    )
    assert not isinstance(result, Commit), (
        f"commits.get for a nonexistent hash must not return Commit, got {result!r}"
    )


# ---------------------------------------------------------------------------
# TC-COMMITS-005: prs (PRs that include a given commit)
# ---------------------------------------------------------------------------


async def test_prs_for_seed_commit(
    client: BBClient, workspace: str
) -> None:
    """TC-COMMITS-005: commits.prs returns list[Pullrequest] (may be empty)."""
    result = await commits.prs(client, workspace, SEED_REPO, SEED_COMMIT)
    assert not isinstance(result, Error), (
        f"commits.prs errored: "
        f"{result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), (
        f"commits.prs must return list, got {type(result).__name__}"
    )
    for idx, pr in enumerate(result):
        assert isinstance(pr, Pullrequest), (
            f"commits.prs[{idx}] is {type(pr).__name__}, expected Pullrequest"
        )
