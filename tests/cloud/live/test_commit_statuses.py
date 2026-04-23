"""Live tests for ``bb.cloud.sdk.commit_statuses``."""

from __future__ import annotations

import pytest

from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.models.error import Error
from bb.cloud.sdk import commit_statuses
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_statuses(
    client: BBClient,
    workspace: str,
    probe_repo_slug: str,
    probe_commit_hash: str,
) -> None:
    result = await commit_statuses.list(
        client, workspace, probe_repo_slug, probe_commit_hash, pagelen=10
    )
    if isinstance(result, Error):
        pytest.skip(
            f"commit_statuses.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"commit_statuses.list must return list, got {type(result).__name__}"
    )
    for idx, status in enumerate(result):
        assert isinstance(status, Commitstatus), (
            f"commit_statuses.list[{idx}] is {type(status).__name__}, expected Commitstatus"
        )
