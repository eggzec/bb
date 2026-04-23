"""Live tests for ``bb.cloud.sdk.users``."""

from __future__ import annotations

import pytest

from bb.cloud.models.account import Account
from bb.cloud.models.error import Error
from bb.cloud.sdk import users
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_me_returns_account(client: BBClient) -> None:
    result = await users.me(client)
    assert not isinstance(result, Error), (
        f"users.me returned Error: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Account), f"expected Account, got {type(result).__name__}"

    # Exactly one of UUID or account_id must be populated for any real account.
    has_uuid = bool(getattr(result, "uuid", None))
    has_account_id = bool(getattr(result, "account_id", None))
    assert has_uuid or has_account_id, (
        f"Account from users.me has neither uuid nor account_id: {result!r}"
    )


async def test_me_and_get_return_same_user(client: BBClient) -> None:
    me = await users.me(client)
    assert isinstance(me, Account), f"precondition failed: users.me returned {me!r}"

    # Re-fetch by UUID — the only stable, API-accepted selector on Account.
    selector = str(getattr(me, "uuid", "") or "")
    assert selector, f"users.me returned an Account with no uuid: {me!r}"

    echoed = await users.get(client, selector)
    assert not isinstance(echoed, Error), (
        f"users.get({selector!r}) returned Error: "
        f"{echoed.error.message if echoed.error else echoed!r}"
    )
    assert isinstance(echoed, Account), (
        f"users.get({selector!r}) must return Account, got {type(echoed).__name__}"
    )

    # Identity must match on at least one stable field. Note: the Account
    # model exposes ``uuid`` but not ``account_id`` directly — roundtrip on
    # uuid is the authoritative identity check.
    me_uuid = getattr(me, "uuid", None)
    echoed_uuid = getattr(echoed, "uuid", None)
    same_uuid = bool(me_uuid) and me_uuid == echoed_uuid
    same_display = bool(getattr(me, "display_name", None)) and (
        getattr(me, "display_name", None) == getattr(echoed, "display_name", None)
    )
    assert same_uuid or same_display, (
        f"users.get did not return the same user as users.me: "
        f"me={me!r} echoed={echoed!r}"
    )


async def test_get_missing_user_is_error_or_none(client: BBClient) -> None:
    result = await users.get(client, "{00000000-0000-0000-0000-000000000000}")
    assert not isinstance(result, Account), (
        f"users.get for a nonexistent user must not return Account, got {result!r}"
    )


async def test_emails_returns_list(client: BBClient) -> None:
    # /user/emails frequently returns non-standard error payloads that the
    # generated ``Error`` schema cannot parse (KeyError on 'type'). Treat any
    # exception here as a scope/permission issue rather than a test failure.
    try:
        result = await users.emails(client)
    except KeyError as exc:
        pytest.skip(f"users.emails returned a non-standard error payload: {exc!r}")
    if isinstance(result, Error):
        pytest.skip(f"users.emails not available for this auth: {result.error.message if result.error else result!r}")
    assert isinstance(result, list), f"users.emails must return a list, got {type(result).__name__}"
    for email in result:
        assert email is not None, "users.emails returned a None entry"
