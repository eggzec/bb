"""Tests for bb.datacenter.sdk.security."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.datacenter.models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from bb.datacenter.models.rest_secret_scanning_allowlist_rule_set_request import (
    RestSecretScanningAllowlistRuleSetRequest,
)
from bb.datacenter.sdk import security
from bb.datacenter.sdk._errors import AuthenticationError

_SEC_API = "bb.datacenter.api.security"


# ---------------------------------------------------------------------------
# security.list_allowlist_rules
# ---------------------------------------------------------------------------


async def test_list_allowlist_rules_returns_rules(mock_dc_client, make_dc_page):
    rule = MagicMock(spec=RestSecretScanningAllowlistRule)
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(return_value=make_dc_page([rule]))):
        assert await security.list_allowlist_rules(mock_dc_client, "PRJ") == [rule]


async def test_list_allowlist_rules_multi_page(mock_dc_client, make_dc_page):
    r1, r2 = MagicMock(spec=RestSecretScanningAllowlistRule), MagicMock(spec=RestSecretScanningAllowlistRule)
    pages = [make_dc_page([r1], is_last=False, next_start=1), make_dc_page([r2])]
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(side_effect=pages)):
        assert await security.list_allowlist_rules(mock_dc_client, "PRJ") == [r1, r2]


async def test_list_allowlist_rules_empty(mock_dc_client, make_dc_page):
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(return_value=make_dc_page([]))):
        assert await security.list_allowlist_rules(mock_dc_client, "PRJ") == []


async def test_list_allowlist_rules_wrong_type_filtered(mock_dc_client, make_dc_page):
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(return_value=make_dc_page([MagicMock()]))):
        assert await security.list_allowlist_rules(mock_dc_client, "PRJ") == []


async def test_list_allowlist_rules_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await security.list_allowlist_rules(bad_auth_dc_client, "PRJ")


async def test_list_allowlist_rules_basic_auth_accepted(basic_mock_dc_client, make_dc_page):
    rule = MagicMock(spec=RestSecretScanningAllowlistRule)
    with patch(f"{_SEC_API}.search_allowlist_rule.asyncio", new=AsyncMock(return_value=make_dc_page([rule]))):
        assert await security.list_allowlist_rules(basic_mock_dc_client, "PRJ") == [rule]


# ---------------------------------------------------------------------------
# security.create_allowlist_rule
# ---------------------------------------------------------------------------


async def test_create_allowlist_rule_returns_rule(mock_dc_client):
    rule = MagicMock(spec=RestSecretScanningAllowlistRule)
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.create_allowlist_rule.asyncio", new=AsyncMock(return_value=rule)):
        assert await security.create_allowlist_rule(mock_dc_client, "PRJ", body=body) == rule


async def test_create_allowlist_rule_error_returns_none(mock_dc_client):
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.create_allowlist_rule.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await security.create_allowlist_rule(mock_dc_client, "PRJ", body=body) is None


async def test_create_allowlist_rule_bad_auth_raises(bad_auth_dc_client):
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.create_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await security.create_allowlist_rule(bad_auth_dc_client, "PRJ", body=body)


# ---------------------------------------------------------------------------
# security.get_allowlist_rule
# ---------------------------------------------------------------------------


async def test_get_allowlist_rule_returns_rule(mock_dc_client):
    rule = MagicMock(spec=RestSecretScanningAllowlistRule)
    with patch(f"{_SEC_API}.get_allowlist_rule.asyncio", new=AsyncMock(return_value=rule)):
        assert await security.get_allowlist_rule(mock_dc_client, "PRJ", "rule-1") == rule


async def test_get_allowlist_rule_not_found_returns_none(mock_dc_client):
    with patch(f"{_SEC_API}.get_allowlist_rule.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await security.get_allowlist_rule(mock_dc_client, "PRJ", "rule-1") is None


async def test_get_allowlist_rule_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_SEC_API}.get_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await security.get_allowlist_rule(bad_auth_dc_client, "PRJ", "rule-1")


# ---------------------------------------------------------------------------
# security.update_allowlist_rule
# ---------------------------------------------------------------------------


async def test_update_allowlist_rule_returns_rule(mock_dc_client):
    rule = MagicMock(spec=RestSecretScanningAllowlistRule)
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.edit_allowlist_rule.asyncio", new=AsyncMock(return_value=rule)):
        assert await security.update_allowlist_rule(mock_dc_client, "PRJ", "rule-1", body=body) == rule


async def test_update_allowlist_rule_error_returns_none(mock_dc_client):
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.edit_allowlist_rule.asyncio", new=AsyncMock(return_value=MagicMock())):
        assert await security.update_allowlist_rule(mock_dc_client, "PRJ", "rule-1", body=body) is None


async def test_update_allowlist_rule_bad_auth_raises(bad_auth_dc_client):
    body = MagicMock(spec=RestSecretScanningAllowlistRuleSetRequest)
    with patch(f"{_SEC_API}.edit_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await security.update_allowlist_rule(bad_auth_dc_client, "PRJ", "rule-1", body=body)


# ---------------------------------------------------------------------------
# security.delete_allowlist_rule
# ---------------------------------------------------------------------------


async def test_delete_allowlist_rule_calls_api(mock_dc_client):
    with patch(f"{_SEC_API}.delete_allowlist_rule.asyncio", new=AsyncMock(return_value=None)) as mock_del:
        await security.delete_allowlist_rule(mock_dc_client, "PRJ", "rule-1")
        mock_del.assert_awaited_once()


async def test_delete_allowlist_rule_returns_none(mock_dc_client):
    with patch(f"{_SEC_API}.delete_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        assert await security.delete_allowlist_rule(mock_dc_client, "PRJ", "rule-1") is None


async def test_delete_allowlist_rule_bad_auth_raises(bad_auth_dc_client):
    with patch(f"{_SEC_API}.delete_allowlist_rule.asyncio", new=AsyncMock(return_value=None)):
        with pytest.raises(AuthenticationError):
            await security.delete_allowlist_rule(bad_auth_dc_client, "PRJ", "rule-1")
