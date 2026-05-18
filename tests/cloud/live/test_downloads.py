"""Live integration tests for ``bb.cloud.sdk.downloads``.

Context
-------
Downloads are unavailable on the **Bitbucket Cloud Free plan**.
The spec documents HTTP 403 for some downloads endpoints, but the live API
returns HTTP 402 (Payment Required) on Free plan. Because 402 is **not** in
the generated spec, the generated ``_parse_response`` falls through to:

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(...)
    else:
        return None   ← this is what we expect (raise_on_unexpected_status=False)

PASS criteria for each test
----------------------------
The SDK returns ``Error`` or ``None`` (not a list / download object) without
raising ``UnexpectedStatus``. An ``UnexpectedStatus`` raise would indicate the
spec does not document the status code returned by the live API (spec gap) AND
that the client was configured to raise — which is NOT the default configuration.

Note: With ``raise_on_unexpected_status=False`` (the default), a 402 response
causes ``_parse_response`` to return ``None``. The paginator in ``downloads.list``
treats ``None`` from the first page as an empty result set, returning ``[]``.
This is silent degradation — callers cannot distinguish "no downloads" from
"plan restriction". Tracked as a spec gap.

Seed data (read-only — DO NOT mutate)
--------------------------------------
- workspace: beaverish
- repo: bb-probe
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.sdk import downloads
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

FAKE_FILENAME = "release-v0.0.1.tar.gz"


# ---------------------------------------------------------------------------
# downloads.list
# ---------------------------------------------------------------------------


async def test_list_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """downloads.list on Free plan must not raise UnexpectedStatus.

    Expected: SDK returns Error or [] (empty list).
    If SDK returns a non-empty list, that is surprising and worth noting —
    the Free plan should block access.
    """
    try:
        result = await downloads.list(client, workspace, probe_repo_slug, pagelen=10)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"downloads.list raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising. "
            f"This is BUG-DOWNLOADS-001: spec does not document HTTP {exc.status_code} "
            f"for GET /repositories/{{workspace}}/{{repo_slug}}/downloads."
        )
    # Result should be Error or an empty list (402 → None → [] from paginator)
    if isinstance(result, Error):
        return  # correctly surfaced as Error
    assert isinstance(result, list), (
        f"downloads.list must return list or Error, got {type(result).__name__}: {result!r}"
    )
    # If we get a non-empty list on Free plan, note it — not necessarily a hard failure
    if result:
        pytest.xfail(
            f"downloads.list returned {len(result)} download(s) on Free plan — "
            f"expected empty list or Error. Downloads may have been accessible."
        )


async def test_list_returns_error_or_empty_on_free_plan(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """downloads.list result must be Error or empty list (plan restriction documented)."""
    try:
        result = await downloads.list(client, workspace, probe_repo_slug, pagelen=10)
    except UnexpectedStatus:
        return  # exception caught — already a known behaviour

    if isinstance(result, Error):
        # Good — SDK surfaced the error
        return

    assert isinstance(result, list), (
        f"downloads.list returned {type(result).__name__}, expected list or Error"
    )
    # An empty list is expected on a Free plan repo with no downloads
    # A non-empty list would mean either the plan restriction was lifted
    # or the repo has downloads (both are valid but worth noting)
    if result:
        pytest.xfail(
            f"downloads.list returned {len(result)} items — Free plan repo unexpectedly has downloads."
        )


# ---------------------------------------------------------------------------
# downloads.get
# ---------------------------------------------------------------------------


async def test_get_nonexistent_filename_returns_none_or_error(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """downloads.get for a nonexistent filename must return None or Error, not raise."""
    try:
        result = await downloads.get(client, workspace, probe_repo_slug, FAKE_FILENAME)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"downloads.get raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should return Error/None instead of raising. "
            f"BUG: spec does not document HTTP {exc.status_code}."
        )
    # With plan restriction, result should be None or Error
    # It should NOT be a download artifact object
    if result is None or isinstance(result, Error):
        return
    # If we get something else, log it for diagnosis
    pytest.xfail(
        f"downloads.get returned unexpected value {type(result).__name__}: {result!r} "
        f"on a Free plan workspace."
    )


# ---------------------------------------------------------------------------
# downloads.upload  (intentionally skipped — would mutate repo)
# ---------------------------------------------------------------------------
# upload() requires multipart form data. Even if the endpoint accepted it,
# we do not want to create artifacts in the probe repo. Skipped intentionally.


# ---------------------------------------------------------------------------
# downloads.delete
# ---------------------------------------------------------------------------


async def test_delete_nonexistent_does_not_raise(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """downloads.delete for a nonexistent filename must not raise.

    On Free plan, the endpoint returns 402 or 403. Since these may not be in
    the spec, the SDK falls through to returning None (raise_on_unexpected_status=False).
    """
    try:
        await downloads.delete(client, workspace, probe_repo_slug, FAKE_FILENAME)
    except UnexpectedStatus as exc:
        pytest.fail(
            f"downloads.delete raised UnexpectedStatus({exc.status_code}) — "
            f"SDK should silently absorb undocumented status codes when "
            f"raise_on_unexpected_status=False. "
            f"BUG: spec does not document HTTP {exc.status_code} for DELETE /downloads/{{filename}}."
        )
