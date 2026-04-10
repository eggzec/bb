"""Tests for bb.datacenter.sdk.builds."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_required_build_condition import RestRequiredBuildCondition
from bb.datacenter.models.rest_required_build_condition_set_request import RestRequiredBuildConditionSetRequest
from bb.datacenter.sdk import builds
from bb.datacenter.sdk._errors import AuthenticationError

_BUILDS_API = "bb.datacenter.api.builds_and_deployments"


# ---------------------------------------------------------------------------
# builds.add_build_status
# ---------------------------------------------------------------------------


async def test_add_build_status_calls_api(mock_dc_client):
    with patch(f"{_BUILDS_API}.add.asyncio", new=AsyncMock(return_value=None)) as mock_add:
        await builds.add_build_status(mock_dc_client, "PRJ", "repo", "abc123")
        mock_add.assert_awaited_once()


async def test_add_build_status_returns_none(mock_dc_client):
    with patch(f"{_BUILDS_API}.add.asyncio", new=AsyncMock(return_value=None)):
        result = await builds.add_build_status(mock_dc_client, "PRJ", "repo", "abc123")
        assert result is None


async def test_add_build_status_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_BUILDS_API}.add.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await builds.add_build_status(bad_auth_dc_client, "PRJ", "repo", "abc123")


async def test_add_build_status_basic_auth_accepted(basic_mock_dc_client):
    with patch(f"{_BUILDS_API}.add.asyncio", new=AsyncMock(return_value=None)):
        await builds.add_build_status(basic_mock_dc_client, "PRJ", "repo", "abc123")


# ---------------------------------------------------------------------------
# builds.list_required_builds
# ---------------------------------------------------------------------------


async def test_list_required_builds_returns_conditions(mock_dc_client, make_dc_page):
    cond = MagicMock(spec=RestRequiredBuildCondition)
    with patch(
        f"{_BUILDS_API}.get_page_of_required_builds_merge_checks.asyncio",
        new=AsyncMock(return_value=make_dc_page([cond])),
    ):
        assert await builds.list_required_builds(mock_dc_client, "PRJ", "repo") == [cond]


async def test_list_required_builds_multi_page(mock_dc_client, make_dc_page):
    c1, c2 = MagicMock(spec=RestRequiredBuildCondition), MagicMock(spec=RestRequiredBuildCondition)
    pages = [make_dc_page([c1], is_last=False, next_start=1), make_dc_page([c2])]
    with patch(
        f"{_BUILDS_API}.get_page_of_required_builds_merge_checks.asyncio",
        new=AsyncMock(side_effect=pages),
    ):
        assert await builds.list_required_builds(mock_dc_client, "PRJ", "repo") == [c1, c2]


async def test_list_required_builds_empty(mock_dc_client, make_dc_page):
    with patch(
        f"{_BUILDS_API}.get_page_of_required_builds_merge_checks.asyncio",
        new=AsyncMock(return_value=make_dc_page([])),
    ):
        assert await builds.list_required_builds(mock_dc_client, "PRJ", "repo") == []


async def test_list_required_builds_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(
        f"{_BUILDS_API}.get_page_of_required_builds_merge_checks.asyncio",
        new=AsyncMock(return_value=make_dc_page([MagicMock()])),
    ):
        assert await builds.list_required_builds(mock_dc_client, "PRJ", "repo") == []


async def test_list_required_builds_bad_auth_raises(bad_auth_dc_client):
    with patch(
        f"{_BUILDS_API}.get_page_of_required_builds_merge_checks.asyncio",
        new=AsyncMock(return_value=None),
    ):
        with pytest.raises(AuthenticationError):
            await builds.list_required_builds(bad_auth_dc_client, "PRJ", "repo")


# ---------------------------------------------------------------------------
# builds.create_required_build
# ---------------------------------------------------------------------------


async def test_create_required_build_returns_condition(mock_dc_client):
    cond = MagicMock(spec=RestRequiredBuildCondition)
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.create_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=cond),
    ):
        assert await builds.create_required_build(mock_dc_client, "PRJ", "repo", body=body) == cond


async def test_create_required_build_error_returns_none(mock_dc_client):
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.create_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=MagicMock()),
    ):
        assert await builds.create_required_build(mock_dc_client, "PRJ", "repo", body=body) is None


async def test_create_required_build_bad_auth_raises(bad_auth_dc_client):
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.create_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=None),
    ):
        with pytest.raises(AuthenticationError):
            await builds.create_required_build(bad_auth_dc_client, "PRJ", "repo", body=body)


# ---------------------------------------------------------------------------
# builds.update_required_build
# ---------------------------------------------------------------------------


async def test_update_required_build_returns_condition(mock_dc_client):
    cond = MagicMock(spec=RestRequiredBuildCondition)
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.update_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=cond),
    ):
        assert await builds.update_required_build(mock_dc_client, "PRJ", "repo", 42, body=body) == cond


async def test_update_required_build_error_returns_none(mock_dc_client):
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.update_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=MagicMock()),
    ):
        assert await builds.update_required_build(mock_dc_client, "PRJ", "repo", 42, body=body) is None


async def test_update_required_build_bad_auth_raises(bad_auth_dc_client):
    body = MagicMock(spec=RestRequiredBuildConditionSetRequest)
    with patch(
        f"{_BUILDS_API}.update_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=None),
    ):
        with pytest.raises(AuthenticationError):
            await builds.update_required_build(bad_auth_dc_client, "PRJ", "repo", 1, body=body)


# ---------------------------------------------------------------------------
# builds.delete_required_build
# ---------------------------------------------------------------------------


async def test_delete_required_build_calls_api(mock_dc_client):
    with patch(
        f"{_BUILDS_API}.delete_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=None),
    ) as mock_del:
        await builds.delete_required_build(mock_dc_client, "PRJ", "repo", 7)
        mock_del.assert_awaited_once()


async def test_delete_required_build_returns_none(mock_dc_client):
    with patch(
        f"{_BUILDS_API}.delete_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=None),
    ):
        assert await builds.delete_required_build(mock_dc_client, "PRJ", "repo", 7) is None


async def test_delete_required_build_bad_auth_raises(bad_auth_dc_client):
    with patch(
        f"{_BUILDS_API}.delete_required_builds_merge_check.asyncio",
        new=AsyncMock(return_value=None),
    ):
        with pytest.raises(AuthenticationError):
            await builds.delete_required_build(bad_auth_dc_client, "PRJ", "repo", 7)
