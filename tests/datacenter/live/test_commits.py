"""Live tests for Bitbucket Data Center commits API."""
from __future__ import annotations

import pytest

from bb.datacenter.sdk import BBDCClient

pytestmark = pytest.mark.live


def test_list_commits(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> None:
    """Test listing commits in a repository."""
    commits = dc_client.commits.list(dc_project_key, dc_repo_slug)
    assert isinstance(commits, list)
    assert len(commits) > 0, "Repository should have at least one commit"


def test_get_commit(
    dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str, dc_commit_hash: str
) -> None:
    """Test getting a specific commit by hash."""
    commit = dc_client.commits.get(dc_project_key, dc_repo_slug, dc_commit_hash)
    assert commit is not None
    assert commit.id == dc_commit_hash
