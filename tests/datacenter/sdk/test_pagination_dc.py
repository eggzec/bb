"""Tests for bb.datacenter.sdk._pagination — sync paginate and async_paginate."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

from bb.datacenter.sdk._pagination import async_paginate, paginate
from bb.datacenter.types import UNSET

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _page(items: list, is_last: bool = True, next_start: int | None = None):
    p = MagicMock()
    p.values = items
    p.is_last_page = is_last
    p.next_page_start = UNSET if (is_last or next_start is None) else next_start
    return p


# ---------------------------------------------------------------------------
# paginate (sync)
# ---------------------------------------------------------------------------


def test_paginate_single_page():
    fn = MagicMock(return_value=_page(["a", "b", "c"]))
    assert list(paginate(fn)) == ["a", "b", "c"]


def test_paginate_multi_page():
    fn = MagicMock(side_effect=[_page([1, 2], is_last=False, next_start=2), _page([3, 4])])
    assert list(paginate(fn)) == [1, 2, 3, 4]


def test_paginate_none_response_stops():
    assert list(paginate(MagicMock(return_value=None))) == []


def test_paginate_empty_values_stops():
    assert list(paginate(MagicMock(return_value=_page([])))) == []


def test_paginate_unset_next_page_start_stops():
    fn = MagicMock(return_value=_page([1, 2], is_last=False, next_start=None))
    result = list(paginate(fn))
    assert result == [1, 2]
    assert fn.call_count == 1


def test_paginate_passes_start_and_limit():
    p1 = _page(["x"], is_last=False, next_start=10)
    p2 = _page(["y"])
    fn = MagicMock(side_effect=[p1, p2])
    list(paginate(fn, "arg1", limit=10))
    calls = fn.call_args_list
    assert calls[0].kwargs["start"] == 0
    assert calls[0].kwargs["limit"] == 10
    assert calls[1].kwargs["start"] == 10


def test_paginate_three_pages():
    fn = MagicMock(
        side_effect=[
            _page([1], is_last=False, next_start=1),
            _page([2], is_last=False, next_start=2),
            _page([3]),
        ]
    )
    assert list(paginate(fn)) == [1, 2, 3]


# ---------------------------------------------------------------------------
# async_paginate (async)
# ---------------------------------------------------------------------------


async def test_async_paginate_single_page(make_dc_page):
    fn = AsyncMock(return_value=make_dc_page(["a", "b"]))
    assert [i async for i in async_paginate(fn)] == ["a", "b"]


async def test_async_paginate_multi_page(make_dc_page):
    fn = AsyncMock(side_effect=[make_dc_page([1, 2], is_last=False, next_start=2), make_dc_page([3, 4])])
    assert [i async for i in async_paginate(fn)] == [1, 2, 3, 4]


async def test_async_paginate_none_stops():
    fn = AsyncMock(return_value=None)
    assert [i async for i in async_paginate(fn)] == []


async def test_async_paginate_empty_stops(make_dc_page):
    fn = AsyncMock(return_value=make_dc_page([]))
    assert [i async for i in async_paginate(fn)] == []


async def test_async_paginate_unset_next_page_start_stops():
    fn = AsyncMock(return_value=_page([10, 20], is_last=False, next_start=None))
    result = [i async for i in async_paginate(fn)]
    assert result == [10, 20]
    assert fn.call_count == 1


async def test_async_paginate_passes_start_and_limit(make_dc_page):
    fn = AsyncMock(side_effect=[make_dc_page(["x"], is_last=False, next_start=5), make_dc_page(["y"])])
    async for _ in async_paginate(fn, "arg", limit=5, key="val"):
        pass
    assert fn.call_args_list[0].kwargs["start"] == 0
    assert fn.call_args_list[0].kwargs["limit"] == 5
    assert fn.call_args_list[1].kwargs["start"] == 5


async def test_async_paginate_three_pages(make_dc_page):
    fn = AsyncMock(
        side_effect=[
            make_dc_page([1], is_last=False, next_start=1),
            make_dc_page([2], is_last=False, next_start=2),
            make_dc_page([3]),
        ]
    )
    assert [i async for i in async_paginate(fn)] == [1, 2, 3]


async def test_async_paginate_is_last_page_stops(make_dc_page):
    fn = AsyncMock(return_value=make_dc_page(["only"]))
    result = [i async for i in async_paginate(fn)]
    assert result == ["only"]
    assert fn.call_count == 1
