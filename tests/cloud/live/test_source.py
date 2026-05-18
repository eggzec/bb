"""Live integration tests for ``bb.cloud.sdk.source``.

Context
-------
Source-tree access is available on **all** Bitbucket Cloud plans. These tests
exercise all four functions in ``bb.cloud.sdk.source`` against the ``bb-probe``
repository in the ``beaverish`` workspace.

Seed data (read-only — DO NOT mutate)
--------------------------------------
- workspace: beaverish
- repo: bb-probe
- known file: greet.py  (exists on main branch)
- seed commit: 84952fad87fb39e3c6d61811a93769378dd4fad7

Functions tested
----------------
- ``root``    — GET /repositories/{workspace}/{repo_slug}/src
- ``get``     — GET /repositories/{workspace}/{repo_slug}/src/{commit}/{path}
- ``history`` — GET /repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}
- ``upload``  — POST /repositories/{workspace}/{repo_slug}/src  (NOT tested — would mutate)
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.sdk import source
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

# ---------------------------------------------------------------------------
# Seed constants (probe data; DO NOT mutate)
# ---------------------------------------------------------------------------
SEED_FILE = "greet.py"
SEED_COMMIT = "84952fad87fb39e3c6d61811a93769378dd4fad7"
SEED_BRANCH = "main"


# ---------------------------------------------------------------------------
# source.root
# ---------------------------------------------------------------------------


async def test_root_returns_non_none_non_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.root must return a directory listing object for bb-probe."""
    try:
        result = await source.root(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.root raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising."
        )
    if isinstance(result, Error):
        pytest.fail(
            f"source.root returned Error for {probe_repo_slug!r}: "
            f"{result.error.message if result.error else result!r} — "
            f"source tree should be accessible on Free plan."
        )
    assert result is not None, (
        f"source.root returned None for {probe_repo_slug!r} — expected a directory listing."
    )


async def test_root_result_has_values(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.root result must expose a 'values' attribute with directory entries."""
    try:
        result = await source.root(client, workspace, probe_repo_slug)
    except UnexpectedStatus as exc:
        pytest.skip(f"source.root raised UnexpectedStatus({exc.status_code}) — skipping.")
    if isinstance(result, Error) or result is None:
        pytest.skip(f"source.root not available: {result!r}")
    # The response should have a 'values' attribute (paginated directory listing)
    assert hasattr(result, "values"), (
        f"source.root result lacks 'values' attribute — got {type(result).__name__}: {result!r}"
    )
    values = getattr(result, "values", None)
    assert values is not None, f"source.root result.values is None: {result!r}"


# ---------------------------------------------------------------------------
# source.get  —  happy path: known file at seed commit
# ---------------------------------------------------------------------------


async def test_get_known_file_at_seed_commit(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.get must return file content for greet.py at the seed commit."""
    try:
        result = await source.get(client, workspace, probe_repo_slug, SEED_COMMIT, SEED_FILE)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.get raised UnexpectedStatus({exc.status_code}) for "
            f"{SEED_FILE!r} at {SEED_COMMIT[:8]} — SDK should return Error/None instead."
        )
    if isinstance(result, Error):
        pytest.fail(
            f"source.get returned Error for known file {SEED_FILE!r}: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, (
        f"source.get returned None for known file {SEED_FILE!r} at commit {SEED_COMMIT[:8]}"
    )


async def test_get_known_file_at_branch(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.get must return file content for greet.py at the main branch."""
    try:
        result = await source.get(client, workspace, probe_repo_slug, SEED_BRANCH, SEED_FILE)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.get raised UnexpectedStatus({exc.status_code}) for "
            f"{SEED_FILE!r} at branch {SEED_BRANCH!r} — SDK should return Error/None instead."
        )
    if isinstance(result, Error):
        pytest.fail(
            f"source.get returned Error for known file {SEED_FILE!r} at branch {SEED_BRANCH!r}: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, (
        f"source.get returned None for known file {SEED_FILE!r} at branch {SEED_BRANCH!r}"
    )


async def test_get_root_listing_at_seed_commit(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.get with empty path returns the root directory listing at a specific commit."""
    try:
        result = await source.get(client, workspace, probe_repo_slug, SEED_COMMIT, "")
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.get(commit, '') raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead."
        )
    if isinstance(result, Error):
        pytest.skip(
            f"source.get root at {SEED_COMMIT[:8]} returned Error: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, (
        f"source.get root at {SEED_COMMIT[:8]} returned None unexpectedly."
    )


# ---------------------------------------------------------------------------
# source.get  —  negative path: nonexistent file / bad commit
# ---------------------------------------------------------------------------


async def test_get_nonexistent_file_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.get for a missing file must return Error or None, not file content."""
    try:
        result = await source.get(
            client, workspace, probe_repo_slug, SEED_COMMIT, "nonexistent-file-zzz.txt"
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.get for missing file raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising."
        )
    # Acceptable: Error or None.
    # NOT acceptable: a truthy non-Error object that looks like file content.
    if result is None or isinstance(result, Error):
        return
    # Some repos may return an empty directory for unknown paths — check for empty values
    values = getattr(result, "values", None)
    assert values is None or not values, (
        f"source.get for missing file returned content-like object: {result!r}"
    )


async def test_get_bad_commit_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.get with a nonexistent commit hash must return Error or None."""
    try:
        result = await source.get(
            client, workspace, probe_repo_slug,
            "0000000000000000000000000000000000000000",
            SEED_FILE,
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.get with bad commit raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising."
        )
    # Must NOT return actual file content
    if isinstance(result, Error) or result is None:
        return
    # If it returned something, it should not have file-like content
    assert not isinstance(result, (str, bytes)), (
        f"source.get with bad commit returned file-like content: {result!r}"
    )


# ---------------------------------------------------------------------------
# source.history
# ---------------------------------------------------------------------------


async def test_history_known_file_returns_result(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.history must return a history object for greet.py."""
    try:
        result = await source.history(client, workspace, probe_repo_slug, SEED_COMMIT, SEED_FILE)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.history raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead."
        )
    if isinstance(result, Error):
        pytest.fail(
            f"source.history returned Error for known file {SEED_FILE!r}: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, (
        f"source.history returned None for known file {SEED_FILE!r} at {SEED_COMMIT[:8]}"
    )


async def test_history_result_has_values(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.history result must expose 'values' with commit entries."""
    try:
        result = await source.history(client, workspace, probe_repo_slug, SEED_COMMIT, SEED_FILE)
    except UnexpectedStatus as exc:
        pytest.skip(f"source.history raised UnexpectedStatus({exc.status_code}) — skipping.")
    if isinstance(result, Error) or result is None:
        pytest.skip(f"source.history not available: {result!r}")
    assert hasattr(result, "values"), (
        f"source.history result lacks 'values' attribute — got {type(result).__name__}: {result!r}"
    )
    values = getattr(result, "values", None)
    assert values, (
        f"source.history result.values is empty for known file {SEED_FILE!r}: {result!r}"
    )


async def test_history_nonexistent_path_returns_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """source.history for a missing file path must return Error or None."""
    try:
        result = await source.history(
            client, workspace, probe_repo_slug, SEED_COMMIT, "no-such-file-zzz.py"
        )
    except UnexpectedStatus as exc:
        pytest.fail(
            f"source.history for missing path raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising."
        )
    # Acceptable: Error, None, or empty history result
    if isinstance(result, Error) or result is None:
        return
    values = getattr(result, "values", None)
    # Empty history for a file that doesn't exist is also acceptable
    if values:
        assert not list(values), (
            f"source.history for nonexistent path returned non-empty history: {result!r}"
        )


# ---------------------------------------------------------------------------
# source.upload  —  intentionally NOT tested (write operation)
# ---------------------------------------------------------------------------
# upload() would POST to the repository src endpoint, mutating the repo.
# Skipped to preserve seed data integrity.
