"""Live tests for ``bb.cloud.sdk.webhooks``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.hook_event import HookEvent
from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.sdk import webhooks
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_list_repo_returns_subscriptions(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    result = await webhooks.list_repo(client, workspace, probe_repo_slug, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"webhooks.list_repo not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"webhooks.list_repo must return list, got {type(result).__name__}"
    )
    for idx, hook in enumerate(result):
        assert isinstance(hook, WebhookSubscription), (
            f"webhooks.list_repo[{idx}] is {type(hook).__name__}, expected WebhookSubscription"
        )


async def test_list_workspace_returns_subscriptions(
    client: BBClient, workspace: str
) -> None:
    result = await webhooks.list_workspace(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"webhooks.list_workspace not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"webhooks.list_workspace must return list, got {type(result).__name__}"
    )
    for idx, hook in enumerate(result):
        assert isinstance(hook, WebhookSubscription), (
            f"webhooks.list_workspace[{idx}] is {type(hook).__name__}, expected WebhookSubscription"
        )


async def test_events_for_repository_subject_type(client: BBClient) -> None:
    result = await webhooks.events(client, subject_type=webhooks.HookSubjectType.REPOSITORY)
    if isinstance(result, Error):
        pytest.skip(
            f"webhooks.events not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"webhooks.events must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "webhooks.events for REPOSITORY must return at least one event type"
    for idx, event in enumerate(result):
        assert isinstance(event, HookEvent), (
            f"webhooks.events[{idx}] is {type(event).__name__}, expected HookEvent"
        )
        assert event.event, f"webhooks.events[{idx}] has empty event name: {event!r}"
