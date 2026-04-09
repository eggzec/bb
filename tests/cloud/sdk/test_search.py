"""Tests for bb.cloud.sdk.search."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.search_code_search_result import SearchCodeSearchResult
from bb.cloud.sdk import search
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.search"


async def test_code_returns_results(mock_client, make_page):
    item = MagicMock(spec=SearchCodeSearchResult)
    with patch(f"{_API}.search_workspace.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await search.code(mock_client, "ws", query="query")
    assert result == [item]


async def test_code_returns_none(mock_client, make_page):
    with patch(f"{_API}.search_workspace.asyncio", new=AsyncMock(return_value=None)):
        result = await search.code(mock_client, "ws", query="query")
    assert result == []


async def test_account_returns_results(mock_client, make_page):
    item = MagicMock(spec=SearchCodeSearchResult)
    with patch(f"{_API}.search_account.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await search.account(mock_client, "user", search_query="query")
    assert result == [item]


async def test_account_returns_none(mock_client, make_page):
    with patch(f"{_API}.search_account.asyncio", new=AsyncMock(return_value=None)):
        result = await search.account(mock_client, "user", search_query="query")
    assert result == []


async def test_team_returns_results(mock_client, make_page):
    item = MagicMock(spec=SearchCodeSearchResult)
    with patch(f"{_API}.search_team.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await search.team(mock_client, "team", search_query="query")
    assert result == [item]


async def test_code_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await search.code(bad_auth_client, "ws", query="query")
