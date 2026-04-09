"""Tests for bb.cloud.sdk.reports."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.report import Report
from bb.cloud.models.report_annotation import ReportAnnotation
from bb.cloud.sdk import reports
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.reports"


async def test_list_returns_reports(mock_client, make_page):
    item = MagicMock(spec=Report)
    with patch(f"{_API}.get_reports_for_commit.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await reports.list(mock_client, "ws", "slug", "abc123")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(f"{_API}.get_reports_for_commit.asyncio", new=AsyncMock(return_value=make_page([]))):
        result = await reports.list(mock_client, "ws", "slug", "abc123")
    assert result == []


async def test_get_returns_report(mock_client):
    report = MagicMock(spec=Report)
    with patch(f"{_API}.get_report.asyncio", new=AsyncMock(return_value=report)):
        result = await reports.get(mock_client, "ws", "slug", "abc123", "report-1")
    assert result is report


async def test_get_returns_none(mock_client):
    with patch(f"{_API}.get_report.asyncio", new=AsyncMock(return_value=None)):
        result = await reports.get(mock_client, "ws", "slug", "abc123", "report-1")
    assert result is None


async def test_create_or_update_returns_report(mock_client):
    report = MagicMock(spec=Report)
    with patch(f"{_API}.create_or_update_report.asyncio", new=AsyncMock(return_value=report)):
        result = await reports.create_or_update(mock_client, "ws", "slug", "abc123", "report-1")
    assert result is report


async def test_delete_returns_none(mock_client):
    with patch(f"{_API}.delete_report.asyncio", new=AsyncMock(return_value=None), create=True):
        result = await reports.delete(mock_client, "ws", "slug", "abc123", "report-1")
    assert result is None


async def test_annotations_returns_list(mock_client, make_page):
    item = MagicMock(spec=ReportAnnotation)
    with patch(f"{_API}.get_annotations_for_report.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await reports.annotations(mock_client, "ws", "slug", "abc123", "report-1")
    assert result == [item]


async def test_get_annotation_returns_annotation(mock_client):
    annotation = MagicMock(spec=ReportAnnotation)
    with patch(f"{_API}.get_annotation.asyncio", new=AsyncMock(return_value=annotation)):
        result = await reports.get_annotation(mock_client, "ws", "slug", "abc123", "report-1", "ann-1")
    assert result is annotation


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await reports.list(bad_auth_client, "ws", "slug", "abc123")
