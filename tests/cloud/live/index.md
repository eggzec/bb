# Bitbucket Cloud SDK — Live Test Suite

This directory contains **live** integration tests that exercise the handwritten
Cloud SDK (`bb.cloud.sdk`) against the real Bitbucket Cloud API at
`https://api.bitbucket.org/2.0`.

Unlike the mock-based suites under `tests/cloud/sdk/` and `tests/cloud/api/`,
these tests make real HTTP requests, authenticate with real credentials, and
assert on real response shapes. They are intended to catch:

- Regressions in the SDK wrappers (union unwrapping, pagination, auth headers)
- Drift between our models and the live API
- Generator output that compiles but misbehaves at runtime
- Auth flow regressions (API token, OAuth, JWT)

---

## How the suite discovers credentials

On collection, [`conftest.py`](conftest.py) loads a `.env` file from the
**project root** (`/home/sces76/temp/bb/.env`) into `os.environ` without
overwriting any values already set. It then auto-skips every test under
`tests/cloud/live/` unless all of `BB_EMAIL`, `BB_TOKEN`, and `BB_WORKSPACE`
are present, **or** `--run-live` is passed on the pytest command line.

The client itself is built by `BBClient.from_env()`, which auto-detects the
first available auth method in this priority order:

1. **API Token**: `BB_EMAIL` + `BB_TOKEN`
2. **OAuth Client Credentials**: `BB_OAUTH_CLIENT_ID` + `BB_OAUTH_CLIENT_SECRET`
3. **OAuth Token**: `BB_OAUTH_TOKEN`
4. **JWT**: `BB_JWT_CLIENT_KEY` + `BB_JWT_CLIENT_SECRET`
5. **App Password** (deprecated, removed June 9, 2026): `BB_USERNAME` + `BB_APP_PASSWORD`

API token (option 1) is the recommended choice for running this suite.

---

## Environment variables

All variables below are read from `os.environ` (populated from `.env` at
collection time). Mark your `.env` as **gitignored** — it contains secrets.

### Required (authentication — pick ONE group)

| Variable | Scope | What it is | How to generate |
|---|---|---|---|
| `BB_EMAIL` | API Token auth | Atlassian account email address used for Basic auth. Used as the username half of the `email:token` pair. | The email on your Atlassian account (`id.atlassian.com` → Profile). |
| `BB_TOKEN` | API Token auth | Atlassian API token. Used as the password half of the Basic auth pair. | Create at <https://id.atlassian.com/manage-profile/security/api-tokens>. Click **Create API token**, give it a label (e.g. `bb-sdk-live-tests`), copy the token. Tokens are shown **once** — store securely. |
| `BB_OAUTH_CLIENT_ID` | OAuth 2.0 (CC) | OAuth 2.0 consumer key for the Client Credentials grant (server-to-server). | In Bitbucket, **Workspace settings → OAuth consumers → Add consumer**. Tick "This is a private consumer" and enable the scopes your tests need (at minimum `account:read`, `repository:read`). Copy the **Key**. |
| `BB_OAUTH_CLIENT_SECRET` | OAuth 2.0 (CC) | OAuth 2.0 consumer secret paired with `BB_OAUTH_CLIENT_ID`. | Same consumer page as the key — click **Show** next to the secret. |
| `BB_OAUTH_TOKEN` | OAuth 2.0 (AC) | An already-obtained OAuth 2.0 Bearer access token (Authorization Code grant or refresh). | Exchange an auth code or refresh token via `POST https://bitbucket.org/site/oauth2/access_token`. See [Atlassian docs](https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/). |
| `BB_JWT_CLIENT_KEY` | JWT (Connect) | Add-on client key issued when your Bitbucket Connect app is installed. | Read from the lifecycle `POST /installed` webhook payload in your Connect add-on. |
| `BB_JWT_CLIENT_SECRET` | JWT (Connect) | Shared secret issued alongside `BB_JWT_CLIENT_KEY`. | Same `POST /installed` payload. |
| `BB_USERNAME` | App password (deprecated) | Bitbucket username (not email). | Your Bitbucket account profile slug. |
| `BB_APP_PASSWORD` | App password (deprecated) | App password string. Support ends **June 9, 2026** — prefer API tokens. | <https://bitbucket.org/account/settings/app-passwords/>. |

### Required (workspace context)

| Variable | Purpose |
|---|---|
| `BB_WORKSPACE` | Workspace slug or UUID used by every test that needs a workspace argument (e.g. `repos.list`, `workspaces.get`). The authenticated account **must** have at least read access to this workspace. Find the slug in the Bitbucket URL: `https://bitbucket.org/<BB_WORKSPACE>/…`. |

### Optional (test breadth & opt-ins)

| Variable | Default | Purpose |
|---|---|---|
| `BB_RUN_LIVE_SMOKE` | unset | Set to `1` to run the legacy smoke suite at [`tests/cloud/test_live_sdk_smoke.py`](../test_live_sdk_smoke.py). Independent of this directory's auto-discovery. |
| `BB_REPO_SLUG` | unset | Pin the "probe" repository used by read-only repo-scoped tests. If unset, tests fall back to the first repo returned by `repos.list(workspace=BB_WORKSPACE)`. Set this when the workspace contains many repos or when the first one has no commits/branches. |
| `BB_PROJECT_KEY` | unset | Pin the project used by project-scoped tests and by `test_repo_lifecycle.py`. If unset, lifecycle tests use the first project returned by `projects.list`. |
| `BB_SEARCH_QUERY` | `def` | Query string for `test_search.py::test_code_search`. Change to something that exists in your workspace for a non-empty result. |
| `BB_OAUTH_EXPIRES` | unset | Lifetime (seconds) of the OAuth access token in `BB_OAUTH_TOKEN`. Lets `OAuthTokenAuth.is_expired()` detect expiry. |
| `BB_OAUTH_REFRESH` | unset | Refresh token paired with `BB_OAUTH_TOKEN`. Stored on the auth object but not auto-refreshed by the SDK. |
| `BB_JWT_HOST` | `bitbucket.org` | `aud` claim for generated JWTs. Override only for on-prem Connect hosts. |

---

## Required token scopes / permissions

**Read-only suite** (everything except `test_*_lifecycle.py`):

- `account` — `users.me()`
- `workspace` / `repository` — `workspaces.*`, `repos.list`, `repos.get`, `branches.*`, `commits.*`, `prs.list`, `projects.*`, `pipelines.list`, `source.*`, `downloads.list`, `deployments.list`, `branch_restrictions.list`, `branching_model.*`, `commit_statuses.list`, `webhooks.list_*`
- `snippet` — `snippets.list`
- `issue:read` — *only if* `BB_REPO_SLUG` points to a repo with the issue tracker enabled (those tests skip gracefully otherwise)

API tokens created at <https://id.atlassian.com/manage-profile/security/api-tokens>
grant the authenticated user's full scope set automatically, so no scope
selection is needed for that flow. OAuth consumers must enable scopes
explicitly in the consumer's configuration page.

**Write suite** (`test_repo_lifecycle.py` and any other file marked
`@pytest.mark.writes`):

- `repository:admin` — create/delete repos
- `project:admin` (workspace-level) — create repos inside a project, create/delete projects
- `webhook` — `test_webhooks.py` create/delete tests (currently read-only, not required)

---

## Example `.env`

Store this as `/home/sces76/temp/bb/.env` (project root). It is read by
`conftest.py::_load_dotenv`.

```dotenv
# --- API Token auth (recommended) ---
BB_EMAIL=you@example.com
BB_TOKEN=ATATT3xFfGF0...                 # https://id.atlassian.com/manage-profile/security/api-tokens

# --- Workspace context ---
BB_WORKSPACE=my-workspace-slug            # from https://bitbucket.org/<slug>/

# --- Optional probes ---
BB_REPO_SLUG=my-probe-repo                # an existing repo with commits/branches/PRs
BB_PROJECT_KEY=PROJ                       # existing project key (uppercase)
BB_SEARCH_QUERY=TODO                      # code search query known to match

# --- Alternative: OAuth 2.0 Client Credentials ---
# BB_OAUTH_CLIENT_ID=Abcd1234...
# BB_OAUTH_CLIENT_SECRET=ZzZz...

# --- Alternative: OAuth 2.0 Bearer token ---
# BB_OAUTH_TOKEN=eyJhbGc...
# BB_OAUTH_EXPIRES=3600
# BB_OAUTH_REFRESH=...
```

A ready-to-copy skeleton lives at the repo root: [`.env.example`](../../../.env.example).

---

## Running the suite

```bash
# Activate the virtualenv
source .venv/bin/activate

# Run the whole live suite (auto-loads .env)
uv run pytest tests/cloud/live/ -v

# Force execution even if credential detection fails (fixtures will still skip
# individual tests that need specific resources):
uv run pytest tests/cloud/live/ -v --run-live

# Read-only only (skip writes):
uv run pytest tests/cloud/live/ -v -m "live and not writes"

# Write lifecycle only (requires repository:admin on BB_WORKSPACE):
uv run pytest tests/cloud/live/ -v -m "writes"

# Single module:
uv run pytest tests/cloud/live/test_prs.py -v

# Keep the output on failure — don't drop to repr-truncation:
uv run pytest tests/cloud/live/ -v -s --tb=long
```

---

## Test file map

| File | Scope | Notes |
|---|---|---|
| [`test_auth.py`](test_auth.py) | `BBClient.from_env` + auth dispatch | Verifies auth method detection and that the client's `auth` property yields an `AuthenticatedClient`. |
| [`test_users.py`](test_users.py) | `bb.cloud.sdk.users` | `me`, `get`, `emails`. |
| [`test_workspaces.py`](test_workspaces.py) | `bb.cloud.sdk.workspaces` | `list`, `get`, `mine`, `permissions`, `members`, `my_permission`. |
| [`test_projects.py`](test_projects.py) | `bb.cloud.sdk.projects` | `list`, `get`, `default_reviewers`. |
| [`test_repos.py`](test_repos.py) | `bb.cloud.sdk.repos` | `list`, `get`, `forks`, `watchers`, `my_permissions`. 404 handling. |
| [`test_branches.py`](test_branches.py) | `bb.cloud.sdk.branches` | `list`, `get`, `tags`. 404 handling. |
| [`test_commits.py`](test_commits.py) | `bb.cloud.sdk.commits` | `list`, `get`. |
| [`test_prs.py`](test_prs.py) | `bb.cloud.sdk.prs` | `list` with each `PullrequestState`, `get`, `default_reviewers`, `effective_default_reviewers`. |
| [`test_pipelines.py`](test_pipelines.py) | `bb.cloud.sdk.pipelines` | `list`, `config`, `variables`, `schedules`. |
| [`test_source.py`](test_source.py) | `bb.cloud.sdk.source` | `root`, `get`, `history`. |
| [`test_branching_model.py`](test_branching_model.py) | `bb.cloud.sdk.branching_model` | `get`, `effective`, `settings`. |
| [`test_branch_restrictions.py`](test_branch_restrictions.py) | `bb.cloud.sdk.branch_restrictions` | `list`. |
| [`test_commit_statuses.py`](test_commit_statuses.py) | `bb.cloud.sdk.commit_statuses` | `list` for the latest commit. |
| [`test_deployments.py`](test_deployments.py) | `bb.cloud.sdk.deployments` | `list`, `envs`. |
| [`test_downloads.py`](test_downloads.py) | `bb.cloud.sdk.downloads` | `list`. |
| [`test_snippets.py`](test_snippets.py) | `bb.cloud.sdk.snippets` | `list`, `list_all`. |
| [`test_webhooks.py`](test_webhooks.py) | `bb.cloud.sdk.webhooks` | `list_repo`, `list_workspace`, `events`. |
| [`test_search.py`](test_search.py) | `bb.cloud.sdk.search` | `code` workspace search. |
| [`test_pagination.py`](test_pagination.py) | `bb.cloud.sdk._pagination` | Verifies `pagelen=1` and `pagelen=50` return identical counts; streaming `aiter_pages`. |
| [`test_repo_lifecycle.py`](test_repo_lifecycle.py) | Write lifecycle | `@pytest.mark.writes` — creates + deletes a throwaway repo. |
| [`test_project_lifecycle.py`](test_project_lifecycle.py) | Write lifecycle | `@pytest.mark.writes` — creates + deletes a throwaway project. |

---

## Graceful-skip policy

Because workspaces vary enormously (empty, no PRs, no pipelines, issue tracker
disabled, etc.), every test that depends on a specific resource beyond the
workspace itself uses `pytest.skip(reason=...)` rather than failing. Read the
skip reasons; they pinpoint which probe environment variable to set to unlock
that coverage.

The **only** hard failures are:

1. An SDK call returns the wrong Python type for a known response.
2. A paginated wrapper loses or duplicates items between page sizes.
3. A 404 response yields a positive model (e.g. a `Branch` for a nonexistent
   branch name) instead of `Error` / `None`.
4. Auth detection misidentifies the method present in the environment.
