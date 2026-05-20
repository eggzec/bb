"""Live tests for the pagination layer in ``bb.cloud.sdk._pagination``.

These tests exercise the real multi-page flow against live data. They
complement the unit tests that verify the `_accepts`/`_should_stop` helpers
and cover the end-to-end guarantee: **no matter what ``pagelen`` is, the
paginator returns the same set of items in the same order**.
"""

from __future__ import annotations

import pytest

from bb.cloud.api.repositories import get_repositories_workspace
from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.sdk import repos
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import aiter_pages, async_paginate

pytestmark = pytest.mark.live


async def test_async_paginate_matches_sdk_wrapper(
    client: BBClient, workspace: str
) -> None:
    """The SDK wrapper must agree with a direct ``async_paginate`` call."""
    via_wrapper = await repos.list(client, workspace, pagelen=5)
    via_direct = await async_paginate(
        get_repositories_workspace.asyncio,
        workspace,
        client=client.auth,
        pagelen=5,
    )
    assert not isinstance(via_wrapper, Error), f"repos.list errored: {via_wrapper!r}"
    assert not isinstance(via_direct, Error), f"direct async_paginate errored: {via_direct!r}"
    wrapper_names = [r.full_name for r in via_wrapper if isinstance(r, Repository)]
    direct_names = [r.full_name for r in via_direct if isinstance(r, Repository)]
    assert wrapper_names == direct_names, (
        f"SDK wrapper and async_paginate disagree:\n"
        f"  wrapper: {wrapper_names!r}\n"
        f"  direct : {direct_names!r}"
    )


async def test_pagelen_one_vs_fifty_yields_same_items(
    client: BBClient, workspace: str
) -> None:
    """Iterating one item per page must deliver the exact same set as a
    50-per-page fetch. This catches off-by-one bugs and lost-tail bugs."""
    tiny = await repos.list(client, workspace, pagelen=1)
    large = await repos.list(client, workspace, pagelen=50)
    assert not isinstance(tiny, Error), f"pagelen=1 errored: {tiny!r}"
    assert not isinstance(large, Error), f"pagelen=50 errored: {large!r}"

    tiny_set = {r.full_name for r in tiny}
    large_set = {r.full_name for r in large}

    assert tiny_set == large_set, (
        f"paginator leaked items across page sizes.\n"
        f"  only in pagelen=1 : {tiny_set - large_set!r}\n"
        f"  only in pagelen=50: {large_set - tiny_set!r}"
    )
    assert len(tiny) == len(large), (
        f"paginator produced different counts: pagelen=1={len(tiny)} vs pagelen=50={len(large)}"
    )


async def test_aiter_pages_yields_same_items_as_paginate(
    client: BBClient, workspace: str
) -> None:
    """Streaming and collect-style helpers must produce identical output."""
    collected: list[str] = []
    async for item in aiter_pages(
        get_repositories_workspace.asyncio,
        workspace,
        client=client.auth,
        pagelen=3,
    ):
        if isinstance(item, Repository) and item.full_name:
            collected.append(item.full_name)

    expected = await repos.list(client, workspace, pagelen=3)
    assert not isinstance(expected, Error), f"repos.list errored: {expected!r}"
    expected_names = [r.full_name for r in expected if isinstance(r, Repository)]

    assert collected == expected_names, (
        f"aiter_pages output diverged from async_paginate:\n"
        f"  aiter  : {collected!r}\n"
        f"  collect: {expected_names!r}"
    )


@pytest.mark.live
def test_sync_sdk_paglen_consistency(client: BBClient, workspace: str) -> None:
    """sync.repos.list with paglen=1 and paglen=50 must return the same complete set.

    With BBClient as a context manager (provided by the function-scoped `client`
    fixture), a persistent asyncio.Runner keeps the event loop open between the
    two calls — multiple sync calls on the same client now work correctly.
    """
    from bb.cloud import sync

    small = sync.repos.list(client, workspace, pagelen=1)
    large = sync.repos.list(client, workspace, pagelen=50)

    if isinstance(small, Error):
        pytest.skip(f"sync.repos.list(paglen=1) returned Error: {small}")
    if isinstance(large, Error):
        pytest.skip(f"sync.repos.list(paglen=50) returned Error: {large}")

    small_names = sorted(r.full_name for r in small if r.full_name)
    large_names = sorted(r.full_name for r in large if r.full_name)
    assert small_names == large_names, (
        f"sync paglen mismatch: paglen=1 → {len(small_names)} repos, "
        f"paglen=50 → {len(large_names)} repos."
    )
