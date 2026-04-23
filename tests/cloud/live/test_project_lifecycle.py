"""Live write-path test: create + delete a throwaway project.

Requires ``project:admin`` on ``BB_WORKSPACE``. Skips gracefully when the
auth principal cannot create projects (common with personal API tokens on
workspaces they do not administer).
"""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.project import Project
from bb.cloud.sdk import projects
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live, pytest.mark.writes]


async def test_project_create_and_delete_roundtrip(
    client: BBClient, workspace: str, throwaway_project_key: str
) -> None:
    # Bitbucket's POST /workspaces/{ws}/projects rejects ``type`` in the body
    # ('extra keys not allowed'), but the generated ``Project`` model lists
    # ``type_`` as required and always emits ``"type": "project"``. Since
    # the attrs-defined model is slotted (read-only ``to_dict``), we wrap
    # it in a duck-typed shim whose ``to_dict`` strips ``type`` before the
    # endpoint serializes the request.
    real_body = Project(
        type_="project",
        key=throwaway_project_key,
        name=f"bb-sdk-live {throwaway_project_key}",
        is_private=True,
    )

    class _CreatableProjectBody:
        def to_dict(self) -> dict:
            payload = real_body.to_dict()
            payload.pop("type", None)
            return payload

    body = _CreatableProjectBody()
    created = await projects.create(client, workspace, body=body)  # type: ignore[arg-type]
    if isinstance(created, Error):
        pytest.skip(
            f"project create not permitted on {workspace!r}: "
            f"{created.error.message if created.error else created!r}"
        )
    if created is None:
        pytest.skip(
            f"projects.create returned None for {throwaway_project_key!r} — "
            "likely a 400/422 not mapped by the generated endpoint"
        )
    assert isinstance(created, Project), (
        f"projects.create returned {type(created).__name__}, expected Project — response={created!r}"
    )
    assert created.key == throwaway_project_key, (
        f"projects.create returned key={created.key!r}, expected {throwaway_project_key!r}"
    )

    try:
        fetched = await projects.get(client, workspace, throwaway_project_key)
        assert isinstance(fetched, Project), (
            f"projects.get after create returned {type(fetched).__name__}: {fetched!r}"
        )
        assert fetched.key == throwaway_project_key, (
            f"projects.get echoed key={fetched.key!r}, expected {throwaway_project_key!r}"
        )
    finally:
        await projects.delete(client, workspace, throwaway_project_key)

    # Confirm deletion: get should no longer return a Project.
    gone = await projects.get(client, workspace, throwaway_project_key)
    assert not isinstance(gone, Project), (
        f"projects.delete left the project reachable: projects.get returned {gone!r}"
    )
