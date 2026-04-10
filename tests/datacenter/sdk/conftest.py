"""Shared fixtures for tests/datacenter/sdk/."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bb.datacenter.types import UNSET


@pytest.fixture
def make_dc_page():
    """Factory: ``make_dc_page(items, is_last=True, next_start=None)`` → DC pagination mock.

    Uses ``is_last_page`` / ``next_page_start`` cursor semantics as required by
    :func:`~bb.datacenter.sdk._pagination.async_paginate`.
    """

    def _make(items: list, is_last: bool = True, next_start: int | None = None):
        mock = MagicMock()
        mock.values = items
        mock.is_last_page = is_last
        mock.next_page_start = UNSET if (is_last or next_start is None) else next_start
        return mock

    return _make
