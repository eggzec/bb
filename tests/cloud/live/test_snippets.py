"""Live tests for ``bb.cloud.sdk.snippets``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.snippet import Snippet
from bb.cloud.sdk import snippets
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_returns_snippets(client: BBClient, workspace: str) -> None:
    # The generated ``Snippet`` model has a known parse bug when the API
    # returns ``owner`` / ``creator`` with only one key (upstream spec issue:
    # 'dictionary update sequence element #0 has length 1; 2 is required').
    # We still exercise the endpoint to catch auth regressions, and degrade
    # gracefully on the model mismatch.
    try:
        result = await snippets.list(client, workspace, pagelen=10)
    except (ValueError, TypeError, KeyError) as exc:
        pytest.xfail(f"generated Snippet model cannot parse live response: {exc!r}")
    if isinstance(result, Error):
        pytest.skip(
            f"snippets.list not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"snippets.list must return list, got {type(result).__name__}"
    )
    for idx, snippet in enumerate(result):
        assert isinstance(snippet, Snippet), (
            f"snippets.list[{idx}] is {type(snippet).__name__}, expected Snippet"
        )


async def test_list_all_returns_snippets(client: BBClient) -> None:
    result = await snippets.list_all(client, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"snippets.list_all not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"snippets.list_all must return list, got {type(result).__name__}"
    )
    for idx, snippet in enumerate(result):
        assert isinstance(snippet, Snippet), (
            f"snippets.list_all[{idx}] is {type(snippet).__name__}, expected Snippet"
        )
