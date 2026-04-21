"""Live write-path tests — create + delete a throwaway repo.

These require the same BB_EMAIL/BB_TOKEN/BB_WORKSPACE creds and sufficient
permissions to create repositories in the workspace.
"""

from __future__ import annotations

import asyncio

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.models.repository_scm import RepositoryScm
from bb.cloud.sdk import repos
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live, pytest.mark.writes]


async def test_repo_create_and_delete_roundtrip(client: BBClient, workspace: str, throwaway_repo_slug: str):
    # Bitbucket Cloud requires a project for repo creation. Pick the first
    # available project in the workspace; skip if the workspace has none.
    from bb.cloud.sdk import projects as projects_sdk

    project_list = await projects_sdk.list(client, workspace)
    if isinstance(project_list, Error) or not project_list:
        pytest.skip(f"no projects available in workspace {workspace!r}")
    project_key = project_list[0].key
    if not project_key:
        pytest.skip("first project has no key")

    from bb.cloud.models.project import Project

    body = Repository(
        type_="repository",
        scm=RepositoryScm.GIT,
        is_private=True,
        project=Project(type_="project", key=project_key),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]
    try:
        created = await repos.create(client, workspace, throwaway_repo_slug, body=body)
        if isinstance(created, Error):
            pytest.skip(f"repo create not permitted: {created.error.message}")
        if not isinstance(created, Repository):
            # Undocumented non-2xx (often 404 = insufficient project permission)
            pytest.skip(f"repo create returned {created!r} — likely missing permissions")
        # Repo creation is async on Bitbucket's side — poll until the GET succeeds.
        fetched: Repository | Error | None = None
        for _ in range(10):
            fetched = await repos.get(client, workspace, throwaway_repo_slug)
            if isinstance(fetched, Repository):
                break
            await asyncio.sleep(1.0)
        assert isinstance(fetched, Repository), f"unexpected get result: {fetched}"
        assert fetched.full_name and throwaway_repo_slug in fetched.full_name.lower()
    finally:
        await repos.delete(client, workspace, throwaway_repo_slug)
