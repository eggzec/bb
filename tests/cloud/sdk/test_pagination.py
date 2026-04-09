"""Tests for bb.cloud.sdk.pagination helpers."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from bb.cloud.sdk._pagination import async_paginate, paginate
from bb.cloud.types import UNSET

# ---------------------------------------------------------------------------
# paginate (sync)
# ---------------------------------------------------------------------------


def test_paginate_single_page_yields_all_items():
    page = MagicMock()
    page.values = [1, 2, 3]
    page.next_ = UNSET
    result = list(paginate(MagicMock(return_value=page)))
    assert result == [1, 2, 3]


def test_paginate_multi_page_yields_all_items():
    page1 = MagicMock()
    page1.values = [1, 2]
    page1.next_ = "https://api.bitbucket.org/2.0/next"
    page2 = MagicMock()
    page2.values = [3]
    page2.next_ = UNSET
    fn = MagicMock(side_effect=[page1, page2])
    result = list(paginate(fn))
    assert result == [1, 2, 3]
    assert fn.call_count == 2


def test_paginate_empty_values_stops_immediately():
    page = MagicMock()
    page.values = []
    fn = MagicMock(return_value=page)
    result = list(paginate(fn))
    assert result == []
    assert fn.call_count == 1


def test_paginate_none_result_stops_immediately():
    fn = MagicMock(return_value=None)
    result = list(paginate(fn))
    assert result == []


def test_paginate_respects_pagelen():
    page = MagicMock()
    page.values = ["x"]
    page.next_ = UNSET
    fn = MagicMock(return_value=page)
    list(paginate(fn, pagelen=10))
    fn.assert_called_once_with(page=1, pagelen=10)


@pytest.mark.parametrize(
    "n_pages",
    [
        pytest.param(2, id="2-pages"),
        pytest.param(3, id="3-pages"),
    ],
)
def test_paginate_page_number_increments(n_pages):
    pages = []
    for i in range(n_pages):
        p = MagicMock()
        p.values = [i]
        p.next_ = "https://next" if i < n_pages - 1 else UNSET
        pages.append(p)
    fn = MagicMock(side_effect=pages)
    list(paginate(fn))
    for expected_page, call in enumerate(fn.call_args_list, start=1):
        assert call.kwargs.get("page") == expected_page or call.args == () or True
        # page is passed as kwarg
        assert fn.call_args_list[expected_page - 1].kwargs["page"] == expected_page


# ---------------------------------------------------------------------------
# async_paginate
# ---------------------------------------------------------------------------


async def test_async_paginate_single_page():
    page = MagicMock()
    page.values = ["a", "b"]
    page.next_ = UNSET
    fn = AsyncMock(return_value=page)
    result = [item async for item in async_paginate(fn)]
    assert result == ["a", "b"]


async def test_async_paginate_multi_page():
    page1 = MagicMock()
    page1.values = ["x"]
    page1.next_ = "https://next"
    page2 = MagicMock()
    page2.values = ["y", "z"]
    page2.next_ = UNSET
    fn = AsyncMock(side_effect=[page1, page2])
    result = [item async for item in async_paginate(fn)]
    assert result == ["x", "y", "z"]
    assert fn.await_count == 2


async def test_async_paginate_empty():
    page = MagicMock()
    page.values = []
    fn = AsyncMock(return_value=page)
    result = [item async for item in async_paginate(fn)]
    assert result == []


async def test_async_paginate_none_result_stops():
    fn = AsyncMock(return_value=None)
    result = [item async for item in async_paginate(fn)]
    assert result == []


async def test_async_paginate_respects_pagelen():
    page = MagicMock()
    page.values = ["a"]
    page.next_ = UNSET
    fn = AsyncMock(return_value=page)
    [item async for item in async_paginate(fn, pagelen=5)]
    fn.assert_awaited_once_with(page=1, pagelen=5)


@pytest.mark.parametrize(
    "n_pages",
    [
        pytest.param(2, id="2-pages"),
        pytest.param(3, id="3-pages"),
    ],
)
async def test_async_paginate_page_number_increments(n_pages):
    pages = []
    for i in range(n_pages):
        p = MagicMock()
        p.values = [i]
        p.next_ = "https://next" if i < n_pages - 1 else UNSET
        pages.append(p)
    fn = AsyncMock(side_effect=pages)
    [item async for item in async_paginate(fn)]
    for expected_page, call in enumerate(fn.await_args_list, start=1):
        assert call.kwargs["page"] == expected_page
