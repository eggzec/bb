# Bitbucket Data Center Live Tests

Tests in this directory (`tests/datacenter/live/`) exercise the `bb.datacenter.sdk` against a running Bitbucket Data Center instance.

These tests are marked with `@pytest.mark.live` and will be **skipped** if you don't set the required environment variables.

## Prerequisites

You must have:

1. **A running Bitbucket Data Center instance** — local Docker container, docker-compose, or self-hosted
2. **Valid credentials** — either a personal access token or username+password
3. **Seed data** — at least one project, repository, branch, and commit

## Environment Variables

Add these to your `.env` file (copy from `.env.example` if needed):

### Required

```ini
# Base URL of the DC REST API (no trailing slash)
BB_DC_BASE_URL=http://localhost:7990/rest

# Authentication — choose ONE:

# Option A: Personal Access Token (recommended)
BB_DC_TOKEN=<your-personal-access-token>

# Option B: Basic auth (username + password)
# BB_DC_USERNAME=admin
# BB_DC_PASSWORD=<your-password>
```

### Optional (required for live tests)

```ini
# Project key (uppercase) — run `make schema-discover-dc` to find the best one
BB_DC_PROJECT_KEY=TEST

# Repository slug — run `make schema-discover-dc` to find the best one
BB_DC_REPO_SLUG=test-repo
```

## Getting Credentials

### Personal Access Token

Create a PAT via the Bitbucket REST API:

```bash
curl -su admin:<password> \
  -X POST http://<dc-host>:7990/rest/access-tokens/1.0/me \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "test-token",
    "permissions": ["PROJECT_ADMIN", "REPO_ADMIN"]
  }'
```

Copy the `token` field from the response and set `BB_DC_TOKEN`.

### Basic Auth

Use your Bitbucket username and password directly:
- `BB_DC_USERNAME=admin`
- `BB_DC_PASSWORD=<admin-password>`

## Seeding Data

The live tests require a project and repository with at least:
- One commit (on the default branch)
- One branch
- Optionally: one pull request

Run the seed script to create them automatically:

```bash
uv run python3 scripts/seed_dc.py
```

Then discover the best project/repo:

```bash
make schema-discover-dc
```

This prints `BB_DC_PROJECT_KEY` and `BB_DC_REPO_SLUG` suggestions — add them to your `.env`.

## Running Tests

With all environment variables set:

```bash
# Run all live tests
uv run pytest tests/datacenter/live/ -m live -v

# Run just one test file
uv run pytest tests/datacenter/live/test_projects.py -m live -v

# Run with detailed output
uv run pytest tests/datacenter/live/ -m live -vv
```

If any env var is missing, tests are skipped with a clear message:

```
SKIPPED tests/datacenter/live/test_projects.py::test_list_projects - BB_DC_TOKEN (or BB_DC_USERNAME+BB_DC_PASSWORD) not set in .env
```

## Test Fixtures

The `conftest.py` provides session-scoped fixtures:

| Fixture | Type | Source |
|---------|------|--------|
| `dc_client` | `BBDCClient` | `BBDCClient.from_env()` |
| `dc_project_key` | `str` | `os.environ["BB_DC_PROJECT_KEY"]` |
| `dc_repo_slug` | `str` | `os.environ["BB_DC_REPO_SLUG"]` |
| `dc_branch_name` | `str` | First branch in the probe repo |
| `dc_commit_hash` | `str` | First commit in the probe repo |
| `dc_pr_id` | `int` | First PR in the probe repo (optional) |

## Test Coverage

Currently covered:
- Projects: list, get
- Repositories: list (per-project), list_all, get
- Branches: list, get_default, lookup by name
- Commits: list, get
- Pull Requests: list, get

## Troubleshooting

### 403 Forbidden on API calls

- Verify the token/credentials are correct
- Check that the token has `PROJECT_ADMIN` and `REPO_ADMIN` permissions
- Ensure `BB_DC_BASE_URL` points to the correct instance

### 404 on project/repo endpoints

- Verify `BB_DC_PROJECT_KEY` and `BB_DC_REPO_SLUG` exist in the instance
- Run `make schema-discover-dc` to find valid values

### Fixtures skip with "no commits found"

- Run `scripts/seed_dc.py` to create seed data
- Or manually push a commit to the repo via git

## See Also

- [`schema-test-dc` Makefile target](../../Makefile) — schemathesis conformance tests against all 365 DC API paths
- [`discover_dc_probe.py`](../../scripts/discover_dc_probe.py) — workspace probe script
- [`seed_dc.py`](../../scripts/seed_dc.py) — seed script for creating test data
