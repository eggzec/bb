"""Live tests for ``bb.cloud.sdk.downloads``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.sdk import downloads
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await downloads.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"downloads.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"downloads.list must return list, got {type(result).__name__}"
    )
