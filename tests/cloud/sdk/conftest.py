"""Shared fixtures for tests/cloud/sdk/."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

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
