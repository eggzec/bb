"""Tests for bb.cloud.sdk._pagination helpers."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from bb.cloud.models.error import Error
from bb.cloud.sdk._pagination import (
    aiter_pages,
    async_paginate,
    iter_pages,
    paginate,
)
from bb.cloud.types import UNSET


def _page(values, next_=UNSET):
    p = MagicMock()
    p.values = values
    p.next_ = next_
    return p


# ---------------------------------------------------------------------------
# paginate (sync, collect → list | Error)
# ---------------------------------------------------------------------------


def test_paginate_single_page_collects_all_items():
    fn = MagicMock(return_value=_page([1, 2, 3]))
    assert paginate(fn) == [1, 2, 3]


def test_paginate_multi_page_collects_all_items():
    fn = MagicMock(side_effect=[_page([1, 2], "https://next"), _page([3])])
    assert paginate(fn) == [1, 2, 3]
    assert fn.call_count == 2


def test_paginate_empty_values_stops_immediately():
    fn = MagicMock(return_value=_page([]))
    assert paginate(fn) == []
    assert fn.call_count == 1


def test_paginate_none_result_stops_immediately():
    fn = MagicMock(return_value=None)
    assert paginate(fn) == []


def test_paginate_respects_pagelen():
    fn = MagicMock(return_value=_page(["x"]))
    paginate(fn, pagelen=10)
    fn.assert_called_once_with(page=1, pagelen=10)


def test_paginate_returns_error_on_first_error_response():
    err = Error(type_="error")
    fn = MagicMock(side_effect=[_page([1], "https://next"), err])
    assert paginate(fn) is err


@pytest.mark.parametrize("n_pages", [2, 3])
def test_paginate_page_number_increments(n_pages):
    pages = [_page([i], "https://next" if i < n_pages - 1 else UNSET) for i in range(n_pages)]
    fn = MagicMock(side_effect=pages)
    paginate(fn)
    for expected, call in enumerate(fn.call_args_list, start=1):
        assert call.kwargs["page"] == expected


def test_paginate_forwards_positional_and_keyword_args():
    fn = MagicMock(return_value=_page(["x"]))
    paginate(fn, "ws", "repo", q="foo")
    fn.assert_called_once_with("ws", "repo", page=1, pagelen=25, q="foo")


# ---------------------------------------------------------------------------
# async_paginate (async, collect → list | Error)
# ---------------------------------------------------------------------------


async def test_async_paginate_single_page():
    fn = AsyncMock(return_value=_page(["a", "b"]))
    assert await async_paginate(fn) == ["a", "b"]


async def test_async_paginate_multi_page():
    fn = AsyncMock(side_effect=[_page(["x"], "https://next"), _page(["y", "z"])])
    assert await async_paginate(fn) == ["x", "y", "z"]
    assert fn.await_count == 2


async def test_async_paginate_empty():
    fn = AsyncMock(return_value=_page([]))
    assert await async_paginate(fn) == []


async def test_async_paginate_none_result_stops():
    fn = AsyncMock(return_value=None)
    assert await async_paginate(fn) == []


async def test_async_paginate_respects_pagelen():
    fn = AsyncMock(return_value=_page(["a"]))
    await async_paginate(fn, pagelen=5)
    fn.assert_awaited_once_with(page=1, pagelen=5)


async def test_async_paginate_returns_error_on_error_response():
    err = Error(type_="error")
    fn = AsyncMock(return_value=err)
    assert await async_paginate(fn) is err


@pytest.mark.parametrize("n_pages", [2, 3])
async def test_async_paginate_page_number_increments(n_pages):
    pages = [_page([i], "https://next" if i < n_pages - 1 else UNSET) for i in range(n_pages)]
    fn = AsyncMock(side_effect=pages)
    await async_paginate(fn)
    for expected, call in enumerate(fn.await_args_list, start=1):
        assert call.kwargs["page"] == expected


# ---------------------------------------------------------------------------
# iter_pages (sync, lazy generator)
# ---------------------------------------------------------------------------


def test_iter_pages_yields_items_across_pages():
    fn = MagicMock(side_effect=[_page([1, 2], "next"), _page([3])])
    assert list(iter_pages(fn)) == [1, 2, 3]


def test_iter_pages_stops_on_error():
    err = Error(type_="error")
    fn = MagicMock(side_effect=[_page([1], "next"), err])
    assert list(iter_pages(fn)) == [1]


def test_iter_pages_stops_on_none():
    fn = MagicMock(return_value=None)
    assert list(iter_pages(fn)) == []


# ---------------------------------------------------------------------------
# aiter_pages (async, lazy generator)
# ---------------------------------------------------------------------------


async def test_aiter_pages_yields_items_across_pages():
    fn = AsyncMock(side_effect=[_page(["a"], "next"), _page(["b", "c"])])
    assert [item async for item in aiter_pages(fn)] == ["a", "b", "c"]


async def test_aiter_pages_stops_on_error():
    err = Error(type_="error")
    fn = AsyncMock(side_effect=[_page(["a"], "next"), err])
    assert [item async for item in aiter_pages(fn)] == ["a"]
