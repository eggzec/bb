"""Live tests for ``bb.cloud.sdk.branch_restrictions``."""

from __future__ import annotations

import pytest

from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.models.error import Error
from bb.cloud.sdk import branch_restrictions
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_restrictions(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await branch_restrictions.list(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"branch_restrictions.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"branch_restrictions.list must return list, got {type(result).__name__}"
    )
    for idx, item in enumerate(result):
        assert isinstance(item, Branchrestriction), (
            f"branch_restrictions.list[{idx}] is {type(item).__name__}, expected Branchrestriction"
        )
