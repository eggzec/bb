"""Live tests for Bitbucket Data Center pull requests API."""
from __future__ import annotations

import pytest

from bb.datacenter.sdk import BBDCClient

pytestmark = pytest.mark.live


def test_list_prs(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> None:
    """Test listing pull requests in a repository."""
    prs = dc_client.prs.list(dc_project_key, dc_repo_slug)
    assert isinstance(prs, list)
    # PRs are optional — repo may not have any, so just check it's a list
    assert isinstance(prs, list)


def test_get_pr(
    dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str, dc_pr_id: int
) -> None:
    """Test getting a specific pull request by ID."""
    pr = dc_client.prs.get(dc_project_key, dc_repo_slug, dc_pr_id)
    assert pr is not None
    assert pr.id == dc_pr_id
