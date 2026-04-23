"""Live tests for ``bb.cloud.sdk.search``."""

from __future__ import annotations

import os

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.search_code_search_result import SearchCodeSearchResult
from bb.cloud.sdk import search
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_code_search_returns_results(client: BBClient, workspace: str) -> None:
    query = os.environ.get("BB_SEARCH_QUERY", "def").strip() or "def"
    result = await search.code(client, workspace, query=query, pagelen=5)
    if isinstance(result, Error):
        pytest.skip(
            f"search.code not available for this workspace/auth: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"search.code must return list, got {type(result).__name__}"
    )
    for idx, hit in enumerate(result):
        assert isinstance(hit, SearchCodeSearchResult), (
            f"search.code[{idx}] is {type(hit).__name__}, expected SearchCodeSearchResult"
        )
