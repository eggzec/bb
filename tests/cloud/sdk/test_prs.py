"""Tests for bb.cloud.sdk.prs."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.error_error import ErrorError
from bb.cloud.models.participant import Participant
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.models.pullrequest_comment import PullrequestComment as PullRequestComment
from bb.cloud.sdk import prs
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.pullrequests"


def _make_error(msg: str = "not found") -> Error:
    return Error(type_="error", error=ErrorError(message=msg))


async def test_list_returns_prs(mock_client, make_page):
    item = MagicMock(spec=Pullrequest)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await prs.list(mock_client, "ws", "slug")
    assert result == [item]


async def test_list_empty(mock_client, make_page):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests.asyncio", new=AsyncMock(return_value=make_page([]))
    ):
        result = await prs.list(mock_client, "ws", "slug")
    assert result == []


async def test_get_returns_pr(mock_client):
    pr = MagicMock(spec=Pullrequest)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio",
        new=AsyncMock(return_value=pr),
    ):
        result = await prs.get(mock_client, "ws", "slug", 1)
    assert result is pr


async def test_get_returns_none(mock_client):
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await prs.get(mock_client, "ws", "slug", 1)
    assert result is None


async def test_create_returns_pr(mock_client):
    pr = MagicMock(spec=Pullrequest)
    with patch(f"{_API}.post_repositories_workspace_repo_slug_pullrequests.asyncio", new=AsyncMock(return_value=pr)):
        result = await prs.create(mock_client, "ws", "slug")
    assert result is pr


async def test_update_returns_pr(mock_client):
    pr = MagicMock(spec=Pullrequest)
    with patch(
        f"{_API}.put_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio",
        new=AsyncMock(return_value=pr),
    ):
        result = await prs.update(mock_client, "ws", "slug", 1)
    assert result is pr


async def test_merge_returns_pr(mock_client):
    pr = MagicMock(spec=Pullrequest)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_pullrequests_pull_request_id_merge.asyncio",
        new=AsyncMock(return_value=pr),
    ):
        result = await prs.merge(mock_client, "ws", "slug", 1)
    assert result is pr


async def test_approve_returns_participant(mock_client):
    part = MagicMock(spec=Participant)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve.asyncio",
        new=AsyncMock(return_value=part),
    ):
        result = await prs.approve(mock_client, "ws", "slug", 1)
    assert result is part


async def test_unapprove_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_approve.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await prs.unapprove(mock_client, "ws", "slug", 1)
    assert result is None


async def test_decline_returns_pr(mock_client):
    pr = MagicMock(spec=Pullrequest)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_pullrequests_pull_request_id_decline.asyncio",
        new=AsyncMock(return_value=pr),
    ):
        result = await prs.decline(mock_client, "ws", "slug", 1)
    assert result is pr


async def test_request_changes_returns_participant(mock_client):
    part = MagicMock(spec=Participant)
    with patch(
        f"{_API}.post_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes.asyncio",
        new=AsyncMock(return_value=part),
    ):
        result = await prs.request_changes(mock_client, "ws", "slug", 1)
    assert result is part


async def test_unrequest_changes_returns_none(mock_client):
    with patch(
        f"{_API}.delete_repositories_workspace_repo_slug_pullrequests_pull_request_id_request_changes.asyncio",
        new=AsyncMock(return_value=None),
    ):
        result = await prs.unrequest_changes(mock_client, "ws", "slug", 1)
    assert result is None


async def test_comments_returns_list(mock_client, make_page):
    item = MagicMock(spec=PullRequestComment)
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id_comments.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await prs.comments(mock_client, "ws", "slug", 1)
    assert result == [item]


async def test_commits_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id_commits.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await prs.commits(mock_client, "ws", "slug", 1)
    assert result == [item]


async def test_tasks_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id_tasks.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await prs.tasks(mock_client, "ws", "slug", 1)
    assert result == [item]


async def test_default_reviewers_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_default_reviewers.asyncio",
        new=AsyncMock(return_value=make_page([item])),
    ):
        result = await prs.default_reviewers(mock_client, "ws", "slug")
    assert result == [item]


async def test_get_propagates_error(mock_client):
    err = _make_error("pr not found")
    with patch(
        f"{_API}.get_repositories_workspace_repo_slug_pullrequests_pull_request_id.asyncio",
        new=AsyncMock(return_value=err),
    ):
        result = await prs.get(mock_client, "ws", "slug", 1)
    assert result is err
    assert isinstance(result, Error)


async def test_create_propagates_error(mock_client):
    err = _make_error("invalid pull request")
    with patch(f"{_API}.post_repositories_workspace_repo_slug_pullrequests.asyncio", new=AsyncMock(return_value=err)):
        result = await prs.create(mock_client, "ws", "slug")
    assert result is err


async def test_list_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await prs.list(bad_auth_client, "ws", "slug")
