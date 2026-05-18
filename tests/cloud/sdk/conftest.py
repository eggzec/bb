"""Shared fixtures for tests/cloud/sdk/."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bb.cloud.sdk._pagination import _accepts
from bb.cloud.types import UNSET


@pytest.fixture
def make_page():
    """Factory: ``make_page(items, has_next=False)`` → paginated result mock.

    The returned object has ``.values`` and ``.next_`` matching what
    ``async_paginate`` reads to decide whether to fetch the next page.
    """

    def _make(items: list, has_next: bool = False):
        mock = MagicMock()
        mock.values = items
        mock.next_ = "https://api.bitbucket.org/2.0/next" if has_next else UNSET
        return mock

    return _make


@pytest.fixture(autouse=True)
def _clear_accepts_cache():
    """Clear the _accepts lru_cache before and after each test.

    Prevents stale introspection results from bleeding between tests,
    especially important when tests use real callables (not MagicMock)
    that have the same identity across parameterised runs.
    """
    _accepts.cache_clear()
    yield
    _accepts.cache_clear()
