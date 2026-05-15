# Test Data Seeding Strategy — bb.cloud.sdk (Full Coverage)

**Goal:** reach testable coverage for all ~407 public functions across 19 modules in `bb.cloud.sdk`.  
**Workspace:** `beaverish` (UUID `{8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5}`)  
**User:** Laraib — account_id `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805`  
**Probe date:** 2026-05-14 (re-run: `make probe-workspace`)  
**Current state:** 3/38 resource categories present (8%). All 3 repos are empty.  
**Workspace members:** 3 already present → `workspaces.members / get_member` works today.

---

## Coverage summary by module

| Module | Functions | Testable? | Blocker |
|---|---|---|---|
| `addon` | 10 | ⚪ Untestable | Requires installed Connect app |
| `branch_restrictions` | 5 | ✅ With seed | Need commits + 1 branch restriction rule |
| `branching_model` | 7 | ✅ Partial today (3/7) | Need commits for project variant |
| `branches` | 8 | ✅ With seed | Need commits |
| `commit_statuses` | 4 | ✅ With seed | Need commits + 1 seeded status |
| `commits` | 3 | ✅ With seed | Need commits |
| `deployments` | 17 | ✅ With seed | Need environments + pipeline deploy step |
| `downloads` | 4 | ✅ With seed | Need 1 uploaded file |
| `issues` | 34 | ✅ With seed | Need issue tracker enabled + 1 issue |
| `_pagination` | 4 | ✅ With seed | Need any list with >1 item |
| `pipelines` | 56 | ✅ With seed (50) / ⚪ partial | runners + test-reports need special setup |
| `projects` | 18 | ✅ Partial today (2/18) | Need project group/user perms + default reviewers |
| `properties` | 12 | ⚪ Untestable | Requires installed Connect app |
| `prs` | 33 | ✅ With seed | Need open PR + comment + task |
| `reports` | 9 | ✅ With seed | Need commits + seeded Code Insights report |
| `repos` | 19 | ✅ Partial today (4/19) | Need group/user perms |
| `search` | 3 | ✅ With seed | Need commits + BB_SEARCH_QUERY |
| `snippets` | 24 | ✅ With seed | Need 1 snippet with a file |
| `source` | 4 | ✅ With seed | Need commits |
| `users` | 13 | ✅ Partial today (3/13) | Need SSH key + GPG key on account |
| `webhooks` | 11 | ✅ With seed | Need repo + workspace webhook |
| `workspaces` | 12 | ✅ Partial today (5/12) | Need repo permission record |

---

## Dedicated probe repo

Create **`bb-probe`** and configure `.env`:

```dotenv
BB_REPO_SLUG=bb-probe
BB_PROJECT_KEY=PROJ
BB_SEARCH_QUERY=def
```

The existing `test-repo-20260409*` repos are lifecycle-test leftovers and can stay as-is
(lifecycle tests create/delete their own throwaway repos independently).

---

## Phase 1 — BLOCKERS (nothing else works without these)

### 1.1  Create and initialise `bb-probe`

```bash
# Create via API (assign to existing project)
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe" \
  -H "Content-Type: application/json" \
  -d '{"scm":"git","is_private":true,"project":{"key":"PROJ"},"has_issues":true}'

# Clone and seed content (the search.code test needs a matching token in BB_SEARCH_QUERY)
git clone "https://$(python3 -c 'import urllib.parse,os; print(urllib.parse.quote(os.environ[\"BB_EMAIL\"]))')":"$BB_TOKEN"@bitbucket.org/beaverish/bb-probe
cd bb-probe

cat > README.md << 'EOF'
# bb-probe
Fixture repo for bb SDK live tests.
EOF

cat > greet.py << 'EOF'
def greet(name: str) -> str:
    """Return a greeting string."""
    return f"hello {name}"


def farewell(name: str) -> str:
    """Return a farewell string."""
    return f"goodbye {name}"
EOF

git add . && git commit -m "chore: initial commit — seed for bb SDK tests"
git push origin main
```

**Unlocks:** `commits.*`, `branches.*`, `source.*`, `branching_model.get/effective/settings`,
`search.code` (set `BB_SEARCH_QUERY=def`), `commit_statuses.create`, `reports.create_or_update`

### 1.2  Create a feature branch and open a PR

```bash
git checkout -b feature/add-farewell
echo "" >> greet.py  # trivial change to make diff non-empty
git commit -am "feat: extend greet module"
git push origin feature/add-farewell
```

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pullrequests" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "feat: extend greet module",
    "source": {"branch": {"name": "feature/add-farewell"}},
    "destination": {"branch": {"name": "main"}},
    "description": "Seed PR for bb SDK live tests."
  }'
```

**Unlocks:** `prs.list/get/create/update`, `prs.diff/diffstat/patch/commits/activity/statuses`,
`prs.approve/unapprove/decline/request_changes`, `prs.default_reviewers/effective_default_reviewers`,
`commits.prs`, `properties.pr_get/set/delete`

---

## Phase 2 — MEDIUM priority

### 2.1  Seed a commit status

```bash
HASH=$(curl -su "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commits?pagelen=1" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['values'][0]['hash'])")

curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/$HASH/statuses/build" \
  -H "Content-Type: application/json" \
  -d "{
    \"state\": \"SUCCESSFUL\",
    \"key\": \"bb-probe-ci\",
    \"name\": \"bb SDK probe build\",
    \"url\": \"https://bitbucket.org/beaverish/bb-probe\",
    \"description\": \"Seeded by probe_workspace.py\"
  }"
```

**Unlocks:** `commit_statuses.list/get/update`

### 2.2  Seed a Code Insights report (reports.*)

```bash
HASH=$(curl -su "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commits?pagelen=1" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['values'][0]['hash'])")

# Create the report
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X PUT "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/$HASH/reports/bb-probe-report" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "bb SDK probe report",
    "details": "Seeded Code Insights report",
    "report_type": "TEST",
    "result": "PASSED",
    "data": [{"type": "PERCENTAGE", "title": "Coverage", "value": 85}]
  }'

# Add an annotation
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X PUT "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/commit/$HASH/reports/bb-probe-report/annotations/ann-001" \
  -H "Content-Type: application/json" \
  -d '{
    "annotation_type": "VULNERABILITY",
    "path": "greet.py",
    "line": 1,
    "message": "Probe annotation",
    "severity": "LOW"
  }'
```

**Unlocks:** `reports.list/get/create_or_update/delete/annotations/get_annotation/create_annotation/bulk_annotations/delete_annotation`

### 2.3  Add a PR comment and task

```bash
PR_ID=$(curl -su "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pullrequests?state=OPEN&pagelen=1" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['values'][0]['id'])")

# Comment
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pullrequests/$PR_ID/comments" \
  -H "Content-Type: application/json" \
  -d '{"content": {"raw": "Probe comment for bb SDK live tests."}}'

# Task (inline comment with task flag)
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pullrequests/$PR_ID/tasks" \
  -H "Content-Type: application/json" \
  -d '{"content": {"raw": "Probe task — do not merge"}}'
```

**Unlocks:** `prs.comments/get_comment/update_comment/delete_comment/resolve_comment/unresolve_comment`,
`prs.create_task/get_task/update_task/delete_task/merge_task_status`

### 2.4  Enable Pipelines + push config

```bash
cd bb-probe && git checkout main

cat > bitbucket-pipelines.yml << 'EOF'
image: python:3.12-alpine

pipelines:
  default:
    - step:
        name: Test
        caches:
          - pip
        script:
          - python -c "from greet import greet; assert greet('world') == 'hello world'"

  branches:
    main:
      - step:
          name: Deploy to Test
          deployment: Test
          script:
            - echo "Deploy step — probe for deployment objects"
EOF

git add bitbucket-pipelines.yml && git commit -m "ci: add Bitbucket Pipelines config"
git push origin main
```

Then enable Pipelines in Repository settings and trigger a run from the UI.

**Unlocks:** `pipelines.list/get/run/stop/steps/step/step_log/config/update_config`,
`pipelines.caches` (after first run with cache), `pipelines.clear_caches/cache_uri/delete_cache`

### 2.5  Add deployment environments

UI: Repository settings → Deployments → Add environment: **Test**, **Staging**, **Production**

Then re-push or re-run the pipeline to trigger the `deployment: Test` step.

**Unlocks:** `deployments.envs/get_env/create_env/update_env/delete_env`, `deployments.list/get` (after a deploy run)

### 2.6  Create a snippet

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/snippets/beaverish" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "bb-probe snippet",
    "is_private": false,
    "scm": "git",
    "files": {
      "probe.py": {"content": "def hello():\n    return \"hello from snippet\"\n"}
    }
  }'
```

**Unlocks:** `snippets.list/list_all/get/create/update/delete`, `snippets.commits/get_commit`,
`snippets.get_file`, `snippets.diff/patch`, `snippets.watch/unwatch/watching/watchers`

### 2.7  Enable issue tracker and create an issue

Ensure issue tracker is enabled: Repository settings → Issue tracker → Public (or Private).

```bash
# Create issue
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/issues" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Probe issue for bb SDK live tests",
    "content": {"raw": "This issue is a data fixture. Do not close."},
    "priority": "minor",
    "type": "task"
  }'

# Comment on it
ISSUE_ID=1
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/issues/$ISSUE_ID/comments" \
  -H "Content-Type: application/json" \
  -d '{"content": {"raw": "Probe comment on probe issue."}}'
```

**Unlocks:** `issues.list/get/create/update/delete/comments/add_comment/get_comment/changes/vote/watch/export`,
`issues.attachments/upload_attachment`

---

## Phase 3 — LOW priority (fills remaining gaps)

### 3.1  Create a git tag

```bash
cd bb-probe
git tag v0.1.0
git push origin v0.1.0
```

**Unlocks:** `branches.tags/get_tag/create_tag/delete_tag`

### 3.2  Add pipeline repository variable

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pipelines_config/variables" \
  -H "Content-Type: application/json" \
  -d '{"key": "PROBE_VAR", "value": "probe_value", "secured": false}'
```

**Unlocks:** `pipelines.variables/get_variable/update_variable/delete_variable`

### 3.3  Add pipeline schedule

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pipelines_config/schedules" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": false,
    "cron_pattern": "0 0 * * 0",
    "target": {
      "type": "pipeline_ref_target",
      "ref_type": "branch", "ref_name": "main",
      "selector": {"type": "default"}
    }
  }'
```

**Unlocks:** `pipelines.schedules/get_schedule/update_schedule/delete_schedule/schedule_executions`

### 3.4  Add pipeline known host

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/pipelines_config/ssh/known_hosts" \
  -H "Content-Type: application/json" \
  -d '{"hostname": "github.com"}'
```

**Unlocks:** `pipelines.known_hosts/get_known_host/create_known_host/update_known_host/delete_known_host`

### 3.5  Generate pipeline SSH key pair

UI: Repository settings → Pipelines → SSH keys → Generate keys

**Unlocks:** `pipelines.ssh_key_pair/update_ssh_key_pair/delete_ssh_key_pair`

### 3.6  Add pipeline caches (requires a pipeline run with `caches:` in config — already in the yml above)

After the pipeline runs with `caches: [pip]`, caches appear automatically.

**Unlocks:** `pipelines.caches/delete_cache/cache_uri/clear_caches`

### 3.7  Add repo webhook

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/hooks" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "bb SDK probe webhook",
    "url": "https://httpbin.org/post",
    "active": true,
    "events": ["repo:push", "pullrequest:created", "pullrequest:fulfilled"]
  }'
```

**Unlocks:** `webhooks.list_repo/get_repo/update_repo/delete_repo`

### 3.8  Add workspace webhook

UI: Workspace settings → Webhooks → Add webhook (URL: https://httpbin.org/post, any events)

**Unlocks:** `webhooks.list_workspace/get_workspace/update_workspace/delete_workspace`

### 3.9  Add branch restriction

```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/branch-restrictions" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "require_approvals_to_merge",
    "branch_match_kind": "glob",
    "pattern": "main",
    "value": 1,
    "users": [], "groups": []
  }'
```

**Unlocks:** `branch_restrictions.list/get/update/delete`

### 3.10  Add deploy key

```bash
ssh-keygen -t ed25519 -f /tmp/bb_probe_deploy -N "" -C "bb-probe deploy key"
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/deploy-keys" \
  -H "Content-Type: application/json" \
  -d "{
    \"key\": \"$(cat /tmp/bb_probe_deploy.pub)\",
    \"label\": \"bb SDK probe deploy key\"
  }"
```

**Unlocks:** `deployments.deploy_keys/get_deploy_key/update_deploy_key/delete_deploy_key`

### 3.11  Add deployment environment variable

```bash
# First get the environment UUID
ENV_UUID=$(curl -su "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/environments?pagelen=1" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['values'][0]['uuid'])")

curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/deployments_config/environments/$ENV_UUID/variables" \
  -H "Content-Type: application/json" \
  -d '{"key": "DEPLOY_PROBE_VAR", "value": "probe", "secured": false}'
```

**Unlocks:** `deployments.env_variables/create_env_variable/update_env_variable/delete_env_variable`

### 3.12  Issue tracker: milestones, versions, components

Create these via the Bitbucket UI under the repo's issue tracker:
- Milestone: "v1.0"
- Version: "1.0.0"
- Component: "core"

**Unlocks:** `issues.milestones/get_milestone`, `issues.versions/get_version`, `issues.components/get_component`

### 3.13  Upload a download file

```bash
echo "bb-probe test asset $(date)" > probe_asset.txt
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/downloads" \
  -F "files=@probe_asset.txt"
```

**Unlocks:** `downloads.list/get/delete`

### 3.14  Add workspace pipeline variable

UI: Workspace settings → Pipelines → Variables → Add variable (key: `WS_PROBE_VAR`, value: `probe`)

**Unlocks:** `pipelines.workspace_variables/get_workspace_variable/update_workspace_variable/delete_workspace_variable`

### 3.15  Add SSH key to account

UI: Bitbucket account settings → SSH keys → Add key (use `/tmp/bb_probe_deploy.pub` from step 3.10 or generate a new one)

**Unlocks:** `users.ssh_keys/get_ssh_key/update_ssh_key/delete_ssh_key`

### 3.16  Add GPG key to account

Generate a test GPG key:
```bash
# Non-interactive GPG key generation
gpg --batch --gen-key << 'EOF'
Key-Type: RSA
Key-Length: 2048
Subkey-Type: RSA
Subkey-Length: 2048
Name-Real: Laraib Test
Name-Email: laraib.ali@soco-engineers.com
Expire-Date: 1y
%no-passphrase
EOF
# Export public key and add via Bitbucket account settings → GPG keys
gpg --armor --export laraib.ali@soco-engineers.com
```

**Unlocks:** `users.gpg_keys/get_gpg_key/add_gpg_key/delete_gpg_key`

### 3.17  Add snippet comment

```bash
SNIPPET_ID=$(curl -su "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/snippets/beaverish?pagelen=1" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['values'][0]['id'])")

curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X POST "https://api.bitbucket.org/2.0/snippets/beaverish/$SNIPPET_ID/comments" \
  -H "Content-Type: application/json" \
  -d '{"content": {"raw": "Probe comment on probe snippet."}}'
```

**Unlocks:** `snippets.comments/add_comment/get_comment/update_comment/delete_comment`

### 3.18  Add repo group and user permissions

The workspace has groups accessible via API — check with:
```bash
curl -su "$BB_EMAIL:$BB_TOKEN" "https://api.bitbucket.org/1.0/groups/beaverish/"
```

If any groups exist, grant one access to bb-probe:
```bash
curl -su "$BB_EMAIL:$BB_TOKEN" \
  -X PUT "https://api.bitbucket.org/2.0/repositories/beaverish/bb-probe/permissions-config/groups/<group_slug>" \
  -H "Content-Type: application/json" \
  -d '{"permission": "read"}'
```

**Unlocks:** `repos.group_permissions/get_group_permission/set_group_permission/delete_group_permission`

For user permissions, grant another Bitbucket user explicit repo access.

**Unlocks:** `repos.user_permissions/get_user_permission/set_user_permission/delete_user_permission`

---

## Untestable without special infrastructure

These require capabilities not available with a standard Bitbucket Cloud account:

| Category | Required setup | SDK Functions |
|---|---|---|
| Connect add-on | A deployed Bitbucket Connect app with `linker` module and installed lifecycle | `addon.*` (10 fn) |
| Connect properties | app_key from an installed Connect add-on | `properties.*` (12 fn) |
| Self-hosted runners | A running runner agent registered with the workspace | `pipelines.runners/workspace_runners` (10 fn) |
| Pipeline test reports | A pipeline step publishing JUnit XML via Bitbucket's test-report feature | `pipelines.test_reports/test_cases/test_case_reasons` (3 fn) |
| Repo fork | Creates a new repo (use lifecycle test pattern) | `repos.fork/forks` (2 fn) |
| PR merge | Destructive — closes the PR (use throwaway PR pattern in lifecycle test) | `prs.merge` (1 fn) |

Total untestable: 38 functions (~9% of SDK)

---

## Summary table

| Priority | Action | Resource categories unlocked |
|---|---|---|
| 🔴 BLOCKER | Init `bb-probe` with commits | commits, branches, source, branching_model, search |
| 🔴 BLOCKER | Create feature branch + open PR | prs (core), commits.prs |
| 🟡 MEDIUM | Seed commit status | commit_statuses |
| 🟡 MEDIUM | Seed Code Insights report + annotation | reports |
| 🟡 MEDIUM | Add PR comment + task | prs (comments, tasks) |
| 🟡 MEDIUM | Enable Pipelines + push config + run | pipelines (runs, steps, caches) |
| 🟡 MEDIUM | Add deployment environments + deploy step | deployments (envs, objects) |
| 🟡 MEDIUM | Create snippet | snippets |
| 🟡 MEDIUM | Enable issues + create 1 issue + comment | issues |
| 🟢 LOW | Git tag | branches (tags) |
| 🟢 LOW | Pipeline variable | pipelines.variables |
| 🟢 LOW | Pipeline schedule | pipelines.schedules |
| 🟢 LOW | Pipeline known host | pipelines.known_hosts |
| 🟢 LOW | Pipeline SSH key pair (UI) | pipelines.ssh_key_pair |
| 🟢 LOW | Pipeline caches (auto after run) | pipelines.caches |
| 🟢 LOW | Repo webhook | webhooks.list_repo |
| 🟢 LOW | Workspace webhook | webhooks.list_workspace |
| 🟢 LOW | Branch restriction | branch_restrictions |
| 🟢 LOW | Deploy key | deployments.deploy_keys |
| 🟢 LOW | Deployment env variable | deployments.env_variables |
| 🟢 LOW | Issue milestones/versions/components | issues.milestones, issues.versions, issues.components |
| 🟢 LOW | Download file | downloads |
| 🟢 LOW | Workspace pipeline variable | pipelines.workspace_variables |
| 🟢 LOW | Account SSH key | users.ssh_keys |
| 🟢 LOW | Account GPG key | users.gpg_keys |
| 🟢 LOW | Snippet comment | snippets.comments |
| 🟢 LOW | Repo group/user permissions | repos.group_permissions, repos.user_permissions |

**Estimated time:** ~45 minutes (pipelines run time dominates).  
**Expected coverage after seeding:** ~34/38 resource categories (89%). Remaining 4: runner, test-reports, Connect.

---

## After seeding — `.env`

```dotenv
BB_EMAIL=laraib.ali@soco-engineers.com
BB_TOKEN=<your-token>
BB_WORKSPACE=beaverish
BB_REPO_SLUG=bb-probe
BB_PROJECT_KEY=PROJ
BB_SEARCH_QUERY=def
```

Re-run `make probe-workspace` after seeding to verify coverage.
