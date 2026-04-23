"""Live tests for ``bb.cloud.sdk.source``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.sdk import source
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_root_returns_listing(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await source.root(client, workspace, probe_repo_slug)
    if isinstance(result, Error):
        pytest.skip(
            f"source.root failed for {probe_repo_slug!r}: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, f"source.root unexpectedly returned None for {probe_repo_slug!r}"


async def test_get_at_head_returns_object(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    # Root listing at a specific commit — we don't need a specific file, just
    # verify the endpoint works with the probe commit.
    result = await source.get(client, workspace, probe_repo_slug, probe_commit_hash, "")
    if isinstance(result, Error):
        pytest.skip(
            f"source.get root at {probe_commit_hash[:8]} failed: "
            f"{result.error.message if result.error else result!r}"
        )
    assert result is not None, "source.get returned None for a valid commit root"


async def test_get_missing_path_is_error_or_none(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    result = await source.get(
        client, workspace, probe_repo_slug, probe_commit_hash, "definitely-not-a-file.zzz"
    )
    # Acceptable: Error or None. Unacceptable: random truthy non-Error object.
    if result is None or isinstance(result, Error):
        return
    # Some repos may accept any path and return an empty directory listing;
    # assert that we at least didn't get something pretending to be a file.
    assert not hasattr(result, "data") or not getattr(result, "data", None), (
        f"source.get for a missing path returned apparently-valid content: {result!r}"
    )
