"""Live integration tests for ``bb.cloud.sdk.webhooks`` (11 functions).

Seed data (beaverish/bb-probe):
  - Repo webhook UUID:      {842a6a21-5169-4b95-90c2-57337ff53e18}
    url: https://httpbin.org/post
  - Workspace webhook UUID: {b71bcb12-c9de-49e5-9d8e-e08738571d66}
    url: https://httpbin.org/post
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.hook_event import HookEvent
from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.models.webhook_subscription_events_item import WebhookSubscriptionEventsItem
from bb.cloud.sdk import webhooks
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET

pytestmark = pytest.mark.live


# ---------------------------------------------------------------------------
# Local fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def probe_repo_webhook_uid() -> str:
    return "{842a6a21-5169-4b95-90c2-57337ff53e18}"


@pytest.fixture
def probe_ws_webhook_uid() -> str:
    return "{b71bcb12-c9de-49e5-9d8e-e08738571d66}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _skip_if_error(result: object, label: str) -> None:
    if isinstance(result, Error):
        msg = result.error.message if result.error else repr(result)
        pytest.skip(f"{label} returned Error: {msg}")


def _throwaway_url() -> str:
    return f"https://example.com/test-{uuid.uuid4().hex}"


def _minimal_webhook(url: str, description: str = "bb-sdk-test") -> WebhookSubscription:
    """Return a minimal WebhookSubscription suitable for create/update calls."""
    return WebhookSubscription(
        type_="webhook_subscription",
        url=url,
        description=description,
        active=True,
        events=[WebhookSubscriptionEventsItem.REPOPUSH],
    )


# ===========================================================================
# 1. webhooks.list_repo
# ===========================================================================


async def test_list_repo_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """list_repo() must return a list of WebhookSubscription."""
    result = await webhooks.list_repo(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "webhooks.list_repo")
    assert isinstance(result, list), (
        f"webhooks.list_repo must return list, got {type(result).__name__}"
    )
    for idx, hook in enumerate(result):
        assert isinstance(hook, WebhookSubscription), (
            f"webhooks.list_repo[{idx}] is {type(hook).__name__}, expected WebhookSubscription"
        )


async def test_list_repo_contains_seed_webhook(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_repo_webhook_uid: str
) -> None:
    """list_repo() must include the seeded repo webhook."""
    result = await webhooks.list_repo(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "webhooks.list_repo")
    assert isinstance(result, list)
    uids = [h.uuid for h in result if isinstance(h, WebhookSubscription)]
    assert probe_repo_webhook_uid in uids, (
        f"Expected repo webhook {probe_repo_webhook_uid!r} in list, got uids: {uids!r}"
    )


# ===========================================================================
# 2. webhooks.get_repo
# ===========================================================================


async def test_get_repo_webhook_returns_seed(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_repo_webhook_uid: str
) -> None:
    """get_repo() must return the seeded webhook with correct URL."""
    result = await webhooks.get_repo(client, workspace, probe_repo_slug, probe_repo_webhook_uid)
    _skip_if_error(result, "webhooks.get_repo")
    assert isinstance(result, WebhookSubscription), (
        f"get_repo must return WebhookSubscription, got {type(result).__name__}"
    )
    assert result.url == "https://httpbin.org/post", (
        f"Expected url='https://httpbin.org/post', got {result.url!r}"
    )


async def test_get_repo_webhook_nonexistent_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """get_repo() on a non-existent UID must return None or Error, not raise."""
    fake_uid = "{00000000-0000-0000-0000-000000000000}"
    result = await webhooks.get_repo(client, workspace, probe_repo_slug, fake_uid)
    assert not isinstance(result, WebhookSubscription), (
        f"Expected None/Error for fake webhook uid, got WebhookSubscription: {result!r}"
    )


# ===========================================================================
# 3–5. webhooks.create_repo / update_repo / delete_repo
# ===========================================================================


async def test_create_repo_webhook_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """create_repo() → verify uuid + url → delete_repo() cleanup."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_repo(
            client, workspace, probe_repo_slug, body=_minimal_webhook(url)
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_repo not permitted: {msg}")
        assert isinstance(created, WebhookSubscription), (
            f"create_repo must return WebhookSubscription, got {type(created).__name__}"
        )
        assert created.uuid is not UNSET and created.uuid, (
            f"create_repo returned webhook with no uuid: {created!r}"
        )
        assert created.url == url, (
            f"Expected url={url!r}, got {created.url!r}"
        )
        created_uid = created.uuid
    finally:
        if created_uid:
            await webhooks.delete_repo(client, workspace, probe_repo_slug, created_uid)


async def test_create_repo_webhook_visible_via_get(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Created repo webhook must be visible via get_repo immediately."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_repo(
            client, workspace, probe_repo_slug, body=_minimal_webhook(url)
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_repo not permitted: {msg}")
        assert isinstance(created, WebhookSubscription)
        created_uid = created.uuid
        assert created_uid

        fetched = await webhooks.get_repo(client, workspace, probe_repo_slug, created_uid)
        assert isinstance(fetched, WebhookSubscription), (
            f"get_repo after create should return WebhookSubscription, got {type(fetched).__name__}"
        )
        assert fetched.url == url, (
            f"Expected url={url!r} via get_repo, got {fetched.url!r}"
        )
    finally:
        if created_uid:
            await webhooks.delete_repo(client, workspace, probe_repo_slug, created_uid)


async def test_update_repo_webhook_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """update_repo() must return a WebhookSubscription with updated description."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_repo(
            client, workspace, probe_repo_slug, body=_minimal_webhook(url, "original desc")
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_repo not permitted: {msg}")
        assert isinstance(created, WebhookSubscription)
        created_uid = created.uuid
        assert created_uid

        updated = await webhooks.update_repo(
            client,
            workspace,
            probe_repo_slug,
            created_uid,
            body=_minimal_webhook(url, "updated desc"),
        )
        if isinstance(updated, Error):
            msg = updated.error.message if updated.error else repr(updated)
            pytest.skip(f"update_repo not permitted: {msg}")
        assert isinstance(updated, WebhookSubscription), (
            f"update_repo must return WebhookSubscription, got {type(updated).__name__}"
        )
        assert updated.description == "updated desc", (
            f"Expected description='updated desc', got {updated.description!r}"
        )
    finally:
        if created_uid:
            await webhooks.delete_repo(client, workspace, probe_repo_slug, created_uid)


async def test_delete_repo_webhook_removes_it(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """delete_repo() must remove webhook so get_repo returns None or Error."""
    url = _throwaway_url()

    created = await webhooks.create_repo(
        client, workspace, probe_repo_slug, body=_minimal_webhook(url)
    )
    if isinstance(created, Error):
        msg = created.error.message if created.error else repr(created)
        pytest.skip(f"create_repo not permitted: {msg}")
    assert isinstance(created, WebhookSubscription)
    created_uid = created.uuid
    assert created_uid

    await webhooks.delete_repo(client, workspace, probe_repo_slug, created_uid)

    after = await webhooks.get_repo(client, workspace, probe_repo_slug, created_uid)
    assert not isinstance(after, WebhookSubscription), (
        f"get_repo after delete returned WebhookSubscription — should be None/Error: {after!r}"
    )


# ===========================================================================
# 6. webhooks.list_workspace
# ===========================================================================


async def test_list_workspace_returns_list(
    client: BBClient, workspace: str
) -> None:
    """list_workspace() must return a list of WebhookSubscription."""
    result = await webhooks.list_workspace(client, workspace, pagelen=25)
    _skip_if_error(result, "webhooks.list_workspace")
    assert isinstance(result, list), (
        f"webhooks.list_workspace must return list, got {type(result).__name__}"
    )
    for idx, hook in enumerate(result):
        assert isinstance(hook, WebhookSubscription), (
            f"webhooks.list_workspace[{idx}] is {type(hook).__name__}, expected WebhookSubscription"
        )


async def test_list_workspace_contains_seed_webhook(
    client: BBClient, workspace: str, probe_ws_webhook_uid: str
) -> None:
    """list_workspace() must include the seeded workspace webhook."""
    result = await webhooks.list_workspace(client, workspace, pagelen=25)
    _skip_if_error(result, "webhooks.list_workspace")
    assert isinstance(result, list)
    uids = [h.uuid for h in result if isinstance(h, WebhookSubscription)]
    assert probe_ws_webhook_uid in uids, (
        f"Expected workspace webhook {probe_ws_webhook_uid!r} in list, got uids: {uids!r}"
    )


# ===========================================================================
# 7. webhooks.get_workspace
# ===========================================================================


async def test_get_workspace_webhook_returns_seed(
    client: BBClient, workspace: str, probe_ws_webhook_uid: str
) -> None:
    """get_workspace() must return the seeded workspace webhook with correct URL."""
    result = await webhooks.get_workspace(client, workspace, probe_ws_webhook_uid)
    _skip_if_error(result, "webhooks.get_workspace")
    assert isinstance(result, WebhookSubscription), (
        f"get_workspace must return WebhookSubscription, got {type(result).__name__}"
    )
    assert result.url == "https://httpbin.org/post", (
        f"Expected url='https://httpbin.org/post', got {result.url!r}"
    )


async def test_get_workspace_webhook_nonexistent_is_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """get_workspace() on a non-existent UID must return None or Error, not raise."""
    fake_uid = "{00000000-0000-0000-0000-000000000000}"
    result = await webhooks.get_workspace(client, workspace, fake_uid)
    assert not isinstance(result, WebhookSubscription), (
        f"Expected None/Error for fake workspace webhook uid, got WebhookSubscription: {result!r}"
    )


# ===========================================================================
# 8–10. webhooks.create_workspace / update_workspace / delete_workspace
# ===========================================================================


async def test_create_workspace_webhook_roundtrip(
    client: BBClient, workspace: str
) -> None:
    """create_workspace() → verify uuid + url → delete_workspace() cleanup."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_workspace(
            client, workspace, body=_minimal_webhook(url)
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_workspace not permitted: {msg}")
        assert isinstance(created, WebhookSubscription), (
            f"create_workspace must return WebhookSubscription, got {type(created).__name__}"
        )
        assert created.uuid is not UNSET and created.uuid, (
            f"create_workspace returned webhook with no uuid: {created!r}"
        )
        assert created.url == url, (
            f"Expected url={url!r}, got {created.url!r}"
        )
        created_uid = created.uuid
    finally:
        if created_uid:
            await webhooks.delete_workspace(client, workspace, created_uid)


async def test_create_workspace_webhook_visible_via_get(
    client: BBClient, workspace: str
) -> None:
    """Created workspace webhook must be visible via get_workspace immediately."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_workspace(
            client, workspace, body=_minimal_webhook(url)
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_workspace not permitted: {msg}")
        assert isinstance(created, WebhookSubscription)
        created_uid = created.uuid
        assert created_uid

        fetched = await webhooks.get_workspace(client, workspace, created_uid)
        assert isinstance(fetched, WebhookSubscription), (
            f"get_workspace after create should return WebhookSubscription, got {type(fetched).__name__}"
        )
        assert fetched.url == url, (
            f"Expected url={url!r} via get_workspace, got {fetched.url!r}"
        )
    finally:
        if created_uid:
            await webhooks.delete_workspace(client, workspace, created_uid)


async def test_update_workspace_webhook_roundtrip(
    client: BBClient, workspace: str
) -> None:
    """update_workspace() must return a WebhookSubscription with updated description."""
    url = _throwaway_url()
    created_uid: str | None = None
    try:
        created = await webhooks.create_workspace(
            client, workspace, body=_minimal_webhook(url, "original ws desc")
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_workspace not permitted: {msg}")
        assert isinstance(created, WebhookSubscription)
        created_uid = created.uuid
        assert created_uid

        updated = await webhooks.update_workspace(
            client,
            workspace,
            created_uid,
            body=_minimal_webhook(url, "updated ws desc"),
        )
        if isinstance(updated, Error):
            msg = updated.error.message if updated.error else repr(updated)
            pytest.skip(f"update_workspace not permitted: {msg}")
        assert isinstance(updated, WebhookSubscription), (
            f"update_workspace must return WebhookSubscription, got {type(updated).__name__}"
        )
        assert updated.description == "updated ws desc", (
            f"Expected description='updated ws desc', got {updated.description!r}"
        )
    finally:
        if created_uid:
            await webhooks.delete_workspace(client, workspace, created_uid)


async def test_delete_workspace_webhook_removes_it(
    client: BBClient, workspace: str
) -> None:
    """delete_workspace() must remove webhook so get_workspace returns None or Error."""
    url = _throwaway_url()

    created = await webhooks.create_workspace(
        client, workspace, body=_minimal_webhook(url)
    )
    if isinstance(created, Error):
        msg = created.error.message if created.error else repr(created)
        pytest.skip(f"create_workspace not permitted: {msg}")
    assert isinstance(created, WebhookSubscription)
    created_uid = created.uuid
    assert created_uid

    await webhooks.delete_workspace(client, workspace, created_uid)

    after = await webhooks.get_workspace(client, workspace, created_uid)
    assert not isinstance(after, WebhookSubscription), (
        f"get_workspace after delete returned WebhookSubscription — should be None/Error: {after!r}"
    )


# ===========================================================================
# 11. webhooks.events
# ===========================================================================


async def test_events_repository_returns_list(client: BBClient) -> None:
    """events(REPOSITORY) must return a non-empty list of HookEvent with .event set."""
    result = await webhooks.events(client, subject_type=webhooks.HookSubjectType.REPOSITORY)
    _skip_if_error(result, "webhooks.events(REPOSITORY)")
    assert isinstance(result, list), (
        f"webhooks.events must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "webhooks.events(REPOSITORY) must return at least one event type"
    for idx, event in enumerate(result):
        assert isinstance(event, HookEvent), (
            f"webhooks.events[{idx}] is {type(event).__name__}, expected HookEvent"
        )
        assert event.event, f"webhooks.events[{idx}].event is empty: {event!r}"


async def test_events_workspace_returns_list(client: BBClient) -> None:
    """events(WORKSPACE) must return a non-empty list of HookEvent with .event set."""
    result = await webhooks.events(client, subject_type=webhooks.HookSubjectType.WORKSPACE)
    _skip_if_error(result, "webhooks.events(WORKSPACE)")
    assert isinstance(result, list), (
        f"webhooks.events must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "webhooks.events(WORKSPACE) must return at least one event type"
    for idx, event in enumerate(result):
        assert isinstance(event, HookEvent), (
            f"webhooks.events[{idx}] is {type(event).__name__}, expected HookEvent"
        )
        assert event.event, f"webhooks.events[{idx}].event is empty: {event!r}"
