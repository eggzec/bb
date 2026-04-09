"""Tests for bb.cloud.sdk.issues."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.component import Component
from bb.cloud.models.issue import Issue
from bb.cloud.models.issue_change import IssueChange
from bb.cloud.models.issue_comment import IssueComment
from bb.cloud.models.milestone import Milestone
from bb.cloud.models.version import Version
from bb.cloud.sdk import issues
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.issue_tracker"


async def test_list_returns_issues(mock_client, make_page):
    item = MagicMock(spec=Issue)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await issues.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues.asyncio", new=AsyncMock(return_value=make_page([]))
    ):
        result = await issues.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_issue(mock_client):
    issue = MagicMock(spec=Issue)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues_issue_id.asyncio", new=AsyncMock(return_value=issue)
    ):
        result = await issues.get(mock_client, "ws", "slug", 1)
    assert result is issue


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues_issue_id.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await issues.get(mock_client, "ws", "slug", 1)
    assert result is None


async def test_create_returns_issue(mock_client):
    issue = MagicMock(spec=Issue)
    with patch(f"{_API}.post_repositories_workspace_repo_slug_issues.asyncio", new=AsyncMock(return_value=issue)):
        result = await issues.create(mock_client, "ws", "slug")
    assert result is issue


async def test_update_returns_issue(mock_client):
    issue = MagicMock(spec=Issue)
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_issues_issue_id.asyncio", new=AsyncMock(return_value=issue)
    ):
        result = await issues.update(mock_client, "ws", "slug", 1)
    assert result is issue


async def test_delete_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_issues_issue_id.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await issues.delete(mock_client, "ws", "slug", 1)
    assert result is None


async def test_vote_returns_none(mock_client):
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_issues_issue_id_vote.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await issues.vote(mock_client, "ws", "slug", 1)
    assert result is None


async def test_unvote_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_issues_issue_id_vote.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await issues.unvote(mock_client, "ws", "slug", 1)
    assert result is None


async def test_watch_returns_none(mock_client):
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_issues_issue_id_watch.asyncio", new=AsyncMock(return_value=None)
    ):
        result = await issues.watch(mock_client, "ws", "slug", 1)
    assert result is None


async def test_unwatch_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_issues_issue_id_watch.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await issues.unwatch(mock_client, "ws", "slug", 1)
    assert result is None


async def test_comments_returns_list(mock_client, make_page):
    item = MagicMock(spec=IssueComment)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues_issue_id_comments.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await issues.comments(mock_client, "ws", "slug", 1)
    assert result == [item]


async def test_changes_returns_list(mock_client, make_page):
    item = MagicMock(spec=IssueChange)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_issues_issue_id_changes.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await issues.changes(mock_client, "ws", "slug", 1)
    assert result == [item]


async def test_milestones_returns_list(mock_client, make_page):
    item = MagicMock(spec=Milestone)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_milestones.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await issues.milestones(mock_client, "ws", "slug")
    assert result == [item]


async def test_versions_returns_list(mock_client, make_page):
    item = MagicMock(spec=Version)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_versions.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await issues.versions(mock_client, "ws", "slug")
    assert result == [item]


async def test_components_returns_list(mock_client, make_page):
    item = MagicMock(spec=Component)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_components.asyncio", new=AsyncMock(return_value=make_page([item]))
    ):
        result = await issues.components(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await issues.list(bad_auth_client, "ws", "slug")
