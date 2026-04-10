"""Tests for bb.datacenter.sdk.prs."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_pull_request import RestPullRequest
from bb.datacenter.models.rest_pull_request_merge_request import RestPullRequestMergeRequest
from bb.datacenter.sdk import prs
from bb.datacenter.sdk._errors import AuthenticationError

_API = "bb.datacenter.api.pull_requests"


# ---------------------------------------------------------------------------
# prs.list
# ---------------------------------------------------------------------------


async def test_prs_list_returns_prs(mock_dc_client, make_dc_page):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(return_value=make_dc_page([pr]))):
        assert await prs.list(mock_dc_client, "PRJ", "repo") == [pr]


async def test_prs_list_multi_page(mock_dc_client, make_dc_page):
    pr1, pr2 = MagicMock(spec=RestPullRequest), MagicMock(spec=RestPullRequest)
    pages = [make_dc_page([pr1], is_last=False, next_start=1), make_dc_page([pr2])]
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(side_effect=pages)):
        assert await prs.list(mock_dc_client, "PRJ", "repo") == [pr1, pr2]


async def test_prs_list_empty(mock_dc_client, make_dc_page):
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await prs.list(mock_dc_client, "PRJ", "repo") == []


async def test_prs_list_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await prs.list(mock_dc_client, "PRJ", "repo") == []


async def test_prs_list_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.list(bad_auth_dc_client, "PRJ", "repo")


async def test_prs_list_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.get_page.asyncio", new=AsyncMock(return_value=make_dc_page([pr]))):
        assert await prs.list(basic_mock_dc_client, "PRJ", "repo") == [pr]


# ---------------------------------------------------------------------------
# prs.get
# ---------------------------------------------------------------------------


async def test_prs_get_returns_pr(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.get_3.asyncio", new=AsyncMock(return_value=pr)):
        assert await prs.get(mock_dc_client, "PRJ", "repo", "42") is pr


async def test_prs_get_none_on_wrong_type(mock_dc_client):
    with patch(f"{_API}.get_3.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await prs.get(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_get_none_on_none(mock_dc_client):
    with patch(f"{_API}.get_3.asyncio", new=AsyncMock(return_value=None)):
        assert await prs.get(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_get_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.get_3.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.get(bad_auth_dc_client, "PRJ", "repo", "42")


# ---------------------------------------------------------------------------
# prs.create
# ---------------------------------------------------------------------------


async def test_prs_create_returns_pr(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.create.asyncio", new=AsyncMock(return_value=pr)):
        assert await prs.create(mock_dc_client, "PRJ", "repo") is pr


async def test_prs_create_none_on_wrong_type(mock_dc_client):
    with patch(f"{_API}.create.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await prs.create(mock_dc_client, "PRJ", "repo") is None


async def test_prs_create_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.create.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.create(bad_auth_dc_client, "PRJ", "repo")


# ---------------------------------------------------------------------------
# prs.update
# ---------------------------------------------------------------------------


async def test_prs_update_returns_pr(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.update.asyncio", new=AsyncMock(return_value=pr)):
        assert await prs.update(mock_dc_client, "PRJ", "repo", "42") is pr


async def test_prs_update_none_on_wrong_type(mock_dc_client):
    with patch(f"{_API}.update.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await prs.update(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_update_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.update.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.update(bad_auth_dc_client, "PRJ", "repo", "42")


# ---------------------------------------------------------------------------
# prs.merge
# ---------------------------------------------------------------------------


async def test_prs_merge_returns_pr(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.merge.asyncio", new=AsyncMock(return_value=pr)):
        assert await prs.merge(mock_dc_client, "PRJ", "repo", "42") is pr


async def test_prs_merge_none_on_wrong_type(mock_dc_client):
    with patch(f"{_API}.merge.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await prs.merge(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_merge_passes_body_and_version(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    mock_fn = AsyncMock(return_value=pr)
    body = MagicMock(spec=RestPullRequestMergeRequest)
    with patch(f"{_API}.merge.asyncio", new=mock_fn):
        await prs.merge(mock_dc_client, "PRJ", "repo", "42", body=body, version="3")
    assert mock_fn.call_args.kwargs["body"] is body
    assert mock_fn.call_args.kwargs["version"] == "3"


async def test_prs_merge_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.merge.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.merge(bad_auth_dc_client, "PRJ", "repo", "42")


# ---------------------------------------------------------------------------
# prs.decline
# ---------------------------------------------------------------------------


async def test_prs_decline_returns_pr(mock_dc_client):
    pr = MagicMock(spec=RestPullRequest)
    with patch(f"{_API}.decline.asyncio", new=AsyncMock(return_value=pr)):
        assert await prs.decline(mock_dc_client, "PRJ", "repo", "42") is pr


async def test_prs_decline_none_on_wrong_type(mock_dc_client):
    with patch(f"{_API}.decline.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await prs.decline(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_decline_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.decline.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.decline(bad_auth_dc_client, "PRJ", "repo", "42")


# ---------------------------------------------------------------------------
# prs.approve  (deprecated endpoint)
# ---------------------------------------------------------------------------


async def test_prs_approve_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_API}.approve.asyncio", new=mock_fn):
        await prs.approve(mock_dc_client, "PRJ", "repo", "42")
    mock_fn.assert_called_once()


async def test_prs_approve_returns_none(mock_dc_client):
    with patch(f"{_API}.approve.asyncio", new=AsyncMock(return_value=None)):
        assert await prs.approve(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_approve_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.approve.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.approve(bad_auth_dc_client, "PRJ", "repo", "42")


async def test_prs_approve_basic_auth_accepted(basic_mock_dc_client):
    with patch(f"{_API}.approve.asyncio", new=AsyncMock(return_value=None)):
        await prs.approve(basic_mock_dc_client, "PRJ", "repo", "42")  # no raise


# ---------------------------------------------------------------------------
# prs.unapprove  (deprecated endpoint)
# ---------------------------------------------------------------------------


async def test_prs_unapprove_calls_api(mock_dc_client):
    mock_fn = AsyncMock(return_value=None)
    with patch(f"{_API}.withdraw_approval.asyncio", new=mock_fn):
        await prs.unapprove(mock_dc_client, "PRJ", "repo", "42")
    mock_fn.assert_called_once()


async def test_prs_unapprove_returns_none(mock_dc_client):
    with patch(f"{_API}.withdraw_approval.asyncio", new=AsyncMock(return_value=None)):
        assert await prs.unapprove(mock_dc_client, "PRJ", "repo", "42") is None


async def test_prs_unapprove_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_API}.withdraw_approval.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await prs.unapprove(bad_auth_dc_client, "PRJ", "repo", "42")


async def test_prs_unapprove_basic_auth_accepted(basic_mock_dc_client):
    with patch(f"{_API}.withdraw_approval.asyncio", new=AsyncMock(return_value=None)):
        await prs.unapprove(basic_mock_dc_client, "PRJ", "repo", "42")  # no raise
