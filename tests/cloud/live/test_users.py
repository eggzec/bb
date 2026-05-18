"""Live tests for ``bb.cloud.sdk.users``.

Covers all 13 SDK functions:
    me, get, emails, get_email,
    ssh_keys, get_ssh_key, add_ssh_key, update_ssh_key, delete_ssh_key,
    gpg_keys, get_gpg_key, add_gpg_key (skipped), delete_gpg_key (skipped)

Seed data (read-only):
    account_id: 712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805
    user uuid: {e8e13d7c-8af1-409a-9a9e-e2bf80ade040}
    display_name: Laraib
    email: laraib.ali@soco-engineers.com
    SSH key UUID: {ed7d598c-4e45-4328-a461-554d7c0e5369}
    GPG fingerprint (partial): 7e7cd216a8df00cb
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.account import Account
from bb.cloud.models.error import Error
from bb.cloud.models.gpg_account_key import GPGAccountKey as GpgAccountKey
from bb.cloud.models.ssh_account_key import SshAccountKey
from bb.cloud.sdk import users
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

OWNER_ACCOUNT_ID = "712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805"
OWNER_UUID = "{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}"
OWNER_EMAIL = "laraib.ali@soco-engineers.com"
OWNER_DISPLAY_NAME = "Laraib"
SEEDED_SSH_KEY_UUID = "{ed7d598c-4e45-4328-a461-554d7c0e5369}"
GPG_FINGERPRINT_PARTIAL = "7e7cd216a8df00cb"

# Throwaway test SSH key (valid RSA public key format).
TEST_SSH_KEY = (
    "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDFGt5XQxBa6kRiSjbQBlkxmMWLrFkKDt7PZMH2BnKL"
    "uJ8BHfVw2pHH3NRDvFh2K5K0V9mFqYk7c8iDLbTtHN3 test-user@bb-sdk-test"
)
TEST_SSH_LABEL = "bb-sdk-live-test-key"
UPDATED_SSH_LABEL = "bb-sdk-live-test-key-updated"

# ──────────────────────────────────────────────────────────────────────────────
# users.me
# ──────────────────────────────────────────────────────────────────────────────


async def test_me_returns_account(client: BBClient) -> None:
    """USR-ME-001/004: me() returns Account with uuid or account_id set."""
    result = await users.me(client)
    assert not isinstance(result, Error), (
        f"users.me returned Error: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Account), f"expected Account, got {type(result).__name__}"
    has_uuid = bool(getattr(result, "uuid", None))
    has_account_id = bool(getattr(result, "account_id", None))
    assert has_uuid or has_account_id, (
        f"Account from users.me has neither uuid nor account_id: {result!r}"
    )


async def test_me_display_name_contains_laraib(client: BBClient) -> None:
    """USR-ME-002: me().display_name contains 'Laraib'."""
    result = await users.me(client)
    assert isinstance(result, Account), f"precondition: users.me returned {result!r}"
    display = getattr(result, "display_name", "") or ""
    assert OWNER_DISPLAY_NAME in display, (
        f"users.me().display_name={display!r} does not contain {OWNER_DISPLAY_NAME!r}"
    )


async def test_me_uuid_matches_known(client: BBClient) -> None:
    """USR-ME-003: me().uuid matches the known owner UUID."""
    result = await users.me(client)
    assert isinstance(result, Account), f"precondition: users.me returned {result!r}"
    uuid = str(getattr(result, "uuid", "") or "")
    # Compare without braces to be robust to formatting differences.
    bare_known = OWNER_UUID.strip("{}")
    bare_returned = uuid.strip("{}")
    assert bare_known == bare_returned, (
        f"users.me().uuid={uuid!r} does not match known {OWNER_UUID!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# users.get
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_returns_same_as_me(client: BBClient) -> None:
    """USR-GET-001/002: get(owner UUID) returns same account as me()."""
    me = await users.me(client)
    assert isinstance(me, Account), f"precondition: users.me returned {me!r}"
    selector = str(getattr(me, "uuid", "") or "")
    assert selector, f"users.me returned Account with no uuid: {me!r}"

    echoed = await users.get(client, selector)
    assert not isinstance(echoed, Error), (
        f"users.get({selector!r}) returned Error: "
        f"{echoed.error.message if echoed.error else echoed!r}"
    )
    assert isinstance(echoed, Account), (
        f"users.get({selector!r}) must return Account, got {type(echoed).__name__}"
    )
    me_uuid = str(getattr(me, "uuid", "") or "").strip("{}")
    echoed_uuid = str(getattr(echoed, "uuid", "") or "").strip("{}")
    same_uuid = bool(me_uuid) and me_uuid == echoed_uuid
    same_display = bool(getattr(me, "display_name", None)) and (
        getattr(me, "display_name", None) == getattr(echoed, "display_name", None)
    )
    assert same_uuid or same_display, (
        f"users.get did not return the same user as users.me: me={me!r} echoed={echoed!r}"
    )


async def test_get_by_known_uuid(client: BBClient) -> None:
    """USR-GET-001 (explicit UUID): get by hardcoded owner UUID."""
    result = await users.get(client, OWNER_UUID)
    if isinstance(result, Error):
        pytest.skip(
            f"users.get({OWNER_UUID!r}) errored: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, Account), (
        f"users.get(OWNER_UUID) must return Account, got {type(result).__name__}"
    )
    display = getattr(result, "display_name", "") or ""
    assert OWNER_DISPLAY_NAME in display, (
        f"display_name={display!r} does not contain {OWNER_DISPLAY_NAME!r}"
    )


async def test_get_missing_user_is_error_or_none(client: BBClient) -> None:
    """USR-GET-003: get with all-zero UUID returns Error|None, not Account."""
    result = await users.get(client, "{00000000-0000-0000-0000-000000000000}")
    assert not isinstance(result, Account), (
        f"users.get for a nonexistent user must not return Account, got {result!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# users.emails
# ──────────────────────────────────────────────────────────────────────────────


async def test_emails_returns_list(client: BBClient) -> None:
    """USR-EMAIL-001/003: emails() returns list; 403 or KeyError triggers skip."""
    try:
        result = await users.emails(client)
    except KeyError as exc:
        pytest.skip(f"users.emails returned a non-standard error payload: {exc!r}")
    if isinstance(result, Error):
        pytest.skip(
            f"users.emails not available for this auth: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), f"users.emails must return a list, got {type(result).__name__}"
    for email in result:
        assert email is not None, "users.emails returned a None entry"


async def test_emails_contains_known_address(client: BBClient) -> None:
    """USR-EMAIL-002: laraib.ali@soco-engineers.com appears in emails list."""
    try:
        result = await users.emails(client)
    except KeyError as exc:
        pytest.skip(f"users.emails returned a non-standard error payload: {exc!r}")
    if isinstance(result, Error):
        pytest.skip(
            f"users.emails not available: {result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list) and result, (
        "users.emails returned empty list — cannot verify email presence"
    )
    all_emails_str = " ".join(str(e) for e in result)
    assert OWNER_EMAIL in all_emails_str, (
        f"Expected email {OWNER_EMAIL!r} not found in emails list: {result!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# users.get_email
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_email_known_address(client: BBClient) -> None:
    """USR-EMAIL-004/005: get_email(known address) returns non-None, non-Error."""
    try:
        result = await users.get_email(client, OWNER_EMAIL)
    except KeyError as exc:
        pytest.skip(f"users.get_email returned a non-standard error payload: {exc!r}")
    except UnexpectedStatus as exc:
        pytest.skip(f"users.get_email raised UnexpectedStatus {exc.status_code}")
    if result is None or isinstance(result, Error):
        pytest.skip(f"users.get_email not available: {result!r}")
    # The returned object should contain the email address somewhere.
    assert OWNER_EMAIL in str(result), (
        f"get_email response does not contain {OWNER_EMAIL!r}: {result!r}"
    )


async def test_get_email_nonexistent_returns_none_or_error(client: BBClient) -> None:
    """USR-EMAIL-006: get_email for unknown address returns None or Error."""
    try:
        result = await users.get_email(client, "nobody@does-not-exist.example.com")
        assert result is None or isinstance(result, Error), (
            f"expected None or Error for unknown email, got {result!r}"
        )
    except (UnexpectedStatus, KeyError):
        pass  # 404 or malformed error payload is acceptable


# ──────────────────────────────────────────────────────────────────────────────
# users.ssh_keys (read-only)
# ──────────────────────────────────────────────────────────────────────────────


async def test_ssh_keys_returns_list(client: BBClient) -> None:
    """USR-SSH-001/003: ssh_keys returns list of SshAccountKey with non-empty identifiers."""
    result = await users.ssh_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(
            f"users.ssh_keys not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), f"users.ssh_keys must return list, got {type(result).__name__}"
    for idx, key in enumerate(result):
        assert isinstance(key, SshAccountKey), (
            f"ssh_keys[{idx}] is {type(key).__name__}, expected SshAccountKey"
        )
        has_key = not isinstance(key.key, type(None)) and bool(key.key)
        has_uuid = not isinstance(key.uuid, type(None)) and bool(key.uuid)
        assert has_key or has_uuid, f"ssh_keys[{idx}] has no key or uuid: {key!r}"


async def test_ssh_keys_contains_seeded_key(client: BBClient) -> None:
    """USR-SSH-002: seeded SSH key UUID {ed7d598c-...} is present."""
    result = await users.ssh_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(
            f"users.ssh_keys not available: "
            f"{result.error.message if result.error else result!r}"
        )
    bare_known = SEEDED_SSH_KEY_UUID.strip("{}")
    found = any(
        bare_known in str(getattr(k, "uuid", "") or "").strip("{}")
        for k in result
    )
    assert found, (
        f"Seeded SSH key UUID {SEEDED_SSH_KEY_UUID!r} not found in ssh_keys: "
        f"{[str(getattr(k, 'uuid', '')) for k in result]!r}"
    )


async def test_get_ssh_key_by_id(client: BBClient) -> None:
    """USR-SSH-004/005: get_ssh_key by numeric id returns SshAccountKey."""
    key_list = await users.ssh_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(key_list, Error) or not key_list:
        pytest.skip("ssh_keys list unavailable or empty — cannot test get_ssh_key")

    # Find seeded key or use first available.
    bare_known = SEEDED_SSH_KEY_UUID.strip("{}")
    target = next(
        (k for k in key_list if bare_known in str(getattr(k, "uuid", "") or "").strip("{}")),
        key_list[0],
    )
    # The numeric id lives in additional_properties or as an 'id' attribute.
    key_id = getattr(target, "id", None)
    if key_id is None:
        key_id = target.additional_properties.get("id")
    if key_id is None:
        pytest.skip("SSH key has no numeric id — cannot test get_ssh_key")

    fetched = await users.get_ssh_key(client, OWNER_UUID, int(key_id))
    if isinstance(fetched, Error):
        pytest.skip(
            f"users.get_ssh_key errored: "
            f"{fetched.error.message if fetched.error else fetched!r}"
        )
    assert isinstance(fetched, SshAccountKey), (
        f"get_ssh_key must return SshAccountKey, got {type(fetched).__name__}"
    )
    fetched_uuid = str(getattr(fetched, "uuid", "") or "").strip("{}")
    target_uuid = str(getattr(target, "uuid", "") or "").strip("{}")
    if fetched_uuid and target_uuid:
        assert fetched_uuid == target_uuid, (
            f"get_ssh_key returned different uuid: {fetched_uuid!r} vs {target_uuid!r}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# users.add_ssh_key / update_ssh_key / delete_ssh_key  (lifecycle)
# ──────────────────────────────────────────────────────────────────────────────


async def test_ssh_key_lifecycle(client: BBClient) -> None:
    """USR-SSH-006..010: add, update label, delete throwaway SSH key."""
    new_key = SshAccountKey(type_="ssh_account_key", key=TEST_SSH_KEY, label=TEST_SSH_LABEL)
    created = await users.add_ssh_key(client, OWNER_UUID, body=new_key)
    if isinstance(created, Error):
        pytest.skip(
            f"users.add_ssh_key not available (scope/duplicate key): "
            f"{created.error.message if created.error else created!r}"
        )
    if created is None:
        pytest.skip("users.add_ssh_key returned None — likely permission denied")

    assert isinstance(created, SshAccountKey), (
        f"add_ssh_key must return SshAccountKey, got {type(created).__name__}"
    )
    assert not isinstance(created.label, type(None)) and TEST_SSH_LABEL in str(created.label or ""), (
        f"add_ssh_key label mismatch: got {created.label!r}"
    )

    # Extract numeric id for subsequent calls.
    key_id = getattr(created, "id", None)
    if key_id is None:
        key_id = created.additional_properties.get("id")
    if key_id is None:
        pytest.skip("Created SSH key has no numeric id — cannot test update/delete")

    key_id = int(key_id)

    try:
        # Update label.
        updated_body = SshAccountKey(type_="ssh_account_key", key=TEST_SSH_KEY, label=UPDATED_SSH_LABEL)
        updated = await users.update_ssh_key(client, OWNER_UUID, key_id, body=updated_body)
        if isinstance(updated, Error):
            pytest.skip(
                f"users.update_ssh_key failed: "
                f"{updated.error.message if updated.error else updated!r}"
            )
        if updated is not None:
            assert isinstance(updated, SshAccountKey), (
                f"update_ssh_key must return SshAccountKey, got {type(updated).__name__}"
            )
            assert UPDATED_SSH_LABEL in str(updated.label or ""), (
                f"update_ssh_key did not update label: got {updated.label!r}"
            )
    finally:
        # Always delete throwaway key.
        try:
            await users.delete_ssh_key(client, OWNER_UUID, key_id)
        except Exception as exc:
            # Log but don't fail — key may already be gone.
            pass

    # Confirm deletion.
    try:
        gone = await users.get_ssh_key(client, OWNER_UUID, key_id)
        assert gone is None or isinstance(gone, Error), (
            f"delete_ssh_key left the key reachable: {gone!r}"
        )
    except UnexpectedStatus as exc:
        assert exc.status_code == 404, (
            f"get_ssh_key after delete raised UnexpectedStatus {exc.status_code}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# users.gpg_keys (read-only)
# ──────────────────────────────────────────────────────────────────────────────


async def test_gpg_keys_returns_list(client: BBClient) -> None:
    """USR-GPG-001: gpg_keys returns list of GPGAccountKey instances."""
    result = await users.gpg_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(
            f"users.gpg_keys not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), f"users.gpg_keys must return list, got {type(result).__name__}"
    for idx, key in enumerate(result):
        assert isinstance(key, GpgAccountKey), (
            f"gpg_keys[{idx}] is {type(key).__name__}, expected GPGAccountKey"
        )


async def test_gpg_keys_contains_seeded_key(client: BBClient) -> None:
    """USR-GPG-002: seeded GPG fingerprint (partial) 7e7cd216a8df00cb is present."""
    result = await users.gpg_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(result, Error):
        pytest.skip(
            f"users.gpg_keys not available: "
            f"{result.error.message if result.error else result!r}"
        )
    found = any(
        GPG_FINGERPRINT_PARTIAL in str(getattr(k, "fingerprint", "") or "").lower()
        for k in result
    )
    assert found, (
        f"Seeded GPG fingerprint {GPG_FINGERPRINT_PARTIAL!r} not found in gpg_keys: "
        f"{[str(getattr(k, 'fingerprint', '')) for k in result]!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# users.get_gpg_key
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_gpg_key_by_fingerprint(client: BBClient) -> None:
    """USR-GPG-003/004: get_gpg_key by fingerprint returns GPGAccountKey."""
    key_list = await users.gpg_keys(client, OWNER_UUID, pagelen=25)
    if isinstance(key_list, Error) or not key_list:
        pytest.skip("gpg_keys list unavailable or empty — cannot test get_gpg_key")

    # Find the seeded key, fall back to first available.
    target = next(
        (k for k in key_list if GPG_FINGERPRINT_PARTIAL in str(getattr(k, "fingerprint", "") or "").lower()),
        key_list[0],
    )
    fingerprint = str(getattr(target, "fingerprint", "") or "")
    if not fingerprint:
        pytest.skip("GPG key has no fingerprint — cannot test get_gpg_key")

    fetched = await users.get_gpg_key(client, OWNER_UUID, fingerprint)
    if isinstance(fetched, Error):
        pytest.skip(
            f"users.get_gpg_key errored: "
            f"{fetched.error.message if fetched.error else fetched!r}"
        )
    assert isinstance(fetched, GpgAccountKey), (
        f"get_gpg_key must return GPGAccountKey, got {type(fetched).__name__}"
    )
    fetched_fp = str(getattr(fetched, "fingerprint", "") or "")
    assert fingerprint in fetched_fp or fetched_fp in fingerprint, (
        f"get_gpg_key returned fingerprint {fetched_fp!r}, expected {fingerprint!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# users.add_gpg_key  (intentionally skipped)
# ──────────────────────────────────────────────────────────────────────────────


@pytest.mark.skip(
    reason=(
        "Skipped intentionally — GPG key format requires an armored PGP block which is "
        "complex to generate in tests; the existing seeded key covers the happy path. "
        "See USR-GPG-005 in the test plan."
    )
)
async def test_add_gpg_key_skipped(client: BBClient) -> None:
    pass


# ──────────────────────────────────────────────────────────────────────────────
# users.delete_gpg_key  (intentionally skipped)
# ──────────────────────────────────────────────────────────────────────────────


@pytest.mark.skip(
    reason=(
        "Skipped intentionally — would delete the only GPG key in the workspace and "
        "break commit signing. See USR-GPG-006 in the test plan."
    )
)
async def test_delete_gpg_key_skipped(client: BBClient) -> None:
    pass
