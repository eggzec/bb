# Test Plan: issues, source, downloads, snippets

## Workspace / Plan Context

- **Workspace:** beaverish (Bitbucket Cloud Free plan)
- **Probe repo:** bb-probe
- **Known source file:** greet.py (in bb-probe, main branch)
- **Seed commit:** 84952fad87fb39e3c6d61811a93769378dd4fad7
- **Plan restrictions:**
  - Issues tracker: always 404 (Free plan — `has_issues=false`)
  - Downloads: expected 402 (Free plan — upgrade required)
  - Snippets: expected 402 (Free plan — upgrade required)
  - Source: available on all plans (no restriction expected)

---

## Module: issues (33 functions)

### Overview

Bitbucket Cloud Free plan does not enable the issue tracker (`has_issues=false`).
All 33 functions in `bb.cloud.sdk.issues` hit `/repositories/{workspace}/{repo_slug}/issues/*`
and are expected to return HTTP 404. The spec documents 404 for issue list/get endpoints.

**PASS criteria:** SDK returns `Error` or `None` (not `Issue`/`IssueComment`/etc.) without raising.
**FAIL criteria:** SDK raises `UnexpectedStatus` or returns a real Issue/Comment model.

### Functions to test

| Function | Parameters | Expected result |
|---|---|---|
| `list` | workspace, repo_slug | `Error` (404) |
| `get` | workspace, repo_slug, issue_id=1 | `Error` or `None` (404) |
| `create` | workspace, repo_slug, body=UNSET | `Error` or `None` (404) |
| `update` | workspace, repo_slug, issue_id=1 | `Error` or `None` (404) |
| `delete` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `comments` | workspace, repo_slug, issue_id=1 | `Error` (404) |
| `get_comment` | workspace, repo_slug, issue_id=1, comment_id=1 | `Error` or `None` (404) |
| `add_comment` | workspace, repo_slug, issue_id=1, body=UNSET | `Error` or `None` (404) |
| `update_comment` | workspace, repo_slug, issue_id=1, comment_id=1 | `Error` or `None` (404) |
| `delete_comment` | workspace, repo_slug, issue_id=1, comment_id=1 | returns `None` (no exception) |
| `changes` | workspace, repo_slug, issue_id=1 | `Error` (404) |
| `get_change` | workspace, repo_slug, issue_id=1, change_id=1 | `Error` or `None` (404) |
| `add_change` | workspace, repo_slug, issue_id=1, body=UNSET | `Error` or `None` (404) |
| `vote` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `unvote` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `voted` | workspace, repo_slug, issue_id=1 | `None` or `Error` (404) |
| `watch` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `unwatch` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `watching` | workspace, repo_slug, issue_id=1 | `None` or `Error` (404) |
| `milestones` | workspace, repo_slug | `Error` (404) |
| `get_milestone` | workspace, repo_slug, milestone_id=1 | `Error` or `None` (404) |
| `versions` | workspace, repo_slug | `Error` (404) |
| `get_version` | workspace, repo_slug, version_id=1 | `Error` or `None` (404) |
| `components` | workspace, repo_slug | `Error` (404) |
| `get_component` | workspace, repo_slug, component_id=1 | `Error` or `None` (404) |
| `attachments` | workspace, repo_slug, issue_id=1 | `None` or `Error` (404) |
| `get_attachment` | workspace, repo_slug, issue_id=1, path="x.txt" | `None` (404) |
| `upload_attachment` | workspace, repo_slug, issue_id=1 | returns `None` (no exception) |
| `delete_attachment` | workspace, repo_slug, issue_id=1, path="x.txt" | returns `None` (no exception) |
| `export` | workspace, repo_slug | returns `None` (no exception) |
| `export_status` | workspace, repo_slug, repo_name="bb-probe", task_id="fake" | `None` or `Error` |
| `import_status` | workspace, repo_slug | `None` or `Error` |
| `import_data` | workspace, repo_slug | returns `None` (no exception) |

### Test strategy

- For functions returning `None` (void like `delete`, `vote`, `watch`): call with valid args,
  catch `UnexpectedStatus` and mark as bug if raised, otherwise PASS.
- For functions returning typed objects: assert result is NOT the happy-path type.
- For paginated list functions (`list`, `comments`, `changes`, `milestones`, `versions`, `components`):
  result should be `Error` (since paginator returns Error on first page failure).
- For single-object getters (`get`, `get_comment`, `get_change`, `get_milestone`, `get_version`, `get_component`):
  result should be `Error` or `None`.
- For write operations that return `None` by design (`delete`, `vote`, `unvote`, `watch`, `unwatch`,
  `delete_comment`, `upload_attachment`, `delete_attachment`, `export`, `import_data`):
  assert no exception is raised (BUG if `UnexpectedStatus` raised).

---

## Module: source (4 functions)

### Overview

Source tree access is available on all Bitbucket Cloud plans. All 4 functions
should work against `bb-probe`.

**PASS criteria for happy path:** SDK returns a non-None, non-Error object.
**PASS criteria for negative tests:** SDK returns `Error` or `None` (not content).

### Functions to test

| Function | Test case | Expected |
|---|---|---|
| `root` | list root of bb-probe | non-None, non-Error object |
| `root` | missing repo slug | `Error` or `None` |
| `get` | read greet.py at seed commit | non-None, non-Error |
| `get` | read greet.py at "main" branch | non-None, non-Error |
| `get` | read nonexistent file | `Error` or `None` |
| `get` | bad commit hash | `Error` or `None` |
| `history` | file history of greet.py at seed commit | non-None, non-Error |
| `history` | nonexistent path | `Error` or `None` |
| `upload` | not tested (write op; skipped to avoid mutating repo) | n/a |

### Verification points for source.get on greet.py

The file greet.py is known to exist. The API may return:
- A raw string of file contents (if path resolves to a file)
- A JSON object / model with contents embedded

In either case the result should be not None and not Error.

---

## Module: downloads (4 functions)

### Overview

Downloads are unavailable on Free plan. The spec documents 403 for some
downloads endpoints, but the live API may return 402 (payment required).
Since 402 is not in the spec, `raise_on_unexpected_status=False` means SDK
returns `None` instead of raising — but this is a spec gap.

**PASS criteria:** SDK returns `Error` or `None` without raising `UnexpectedStatus`.
**FAIL / BUG criteria:** SDK raises `UnexpectedStatus(402)`.

### Functions to test

| Function | Test case | Expected (Free plan) |
|---|---|---|
| `list` | list downloads for bb-probe | `Error` or `None` (not a list) |
| `get` | get specific filename | `None` or `Error` (not a download object) |
| `upload` | skipped (would need file body and still fail) | n/a |
| `delete` | delete nonexistent filename | returns `None` (no exception) |

---

## Module: snippets (25 functions)

### Overview

Snippets are unavailable on Free plan. The spec documents 404 for some
snippet endpoints but does NOT document 402 for any. With `raise_on_unexpected_status=False`,
a 402 response causes the SDK to return `None`. This is a spec gap / potential bug.

**PASS criteria:** SDK returns `Error`, `None`, or `[]` (empty list) without raising.
**FAIL / BUG criteria:** SDK raises `UnexpectedStatus(402)`.

Note: `list_all` (GET /2.0/snippets) is a public endpoint and may actually return
snippets from other users. It is also subject to 402 on Free plan for the workspace.

### Functions to test

| Function | Test case | Expected |
|---|---|---|
| `list` | list snippets for beaverish workspace | `Error` or `[]` |
| `list_all` | list all public snippets | `Error`, `[]`, or list of snippets |
| `create` | create with empty body | `Error` or `None` (402) |
| `create_default` | create with empty body | `Error` or `None` (402) |
| `get` | get random fake ID "AAAAAA" | `Error` or `None` |
| `update` | update fake ID | `Error` or `None` |
| `delete` | delete fake ID | `None` (no exception) |
| `comments` | comments on fake ID | `Error` or `[]` |
| `add_comment` | add comment on fake ID | `Error` or `None` |
| `get_comment` | get fake comment | `Error` or `None` |
| `update_comment` | update fake comment | `Error` or `None` |
| `delete_comment` | delete fake comment | `None` (no exception) |
| `commits` | commits on fake snippet | `Error` or `[]` |
| `get_commit` | get fake revision | `Error` or `None` |
| `watch` | watch fake snippet | `None` (no exception) |
| `unwatch` | unwatch fake snippet | `None` (no exception) |
| `watching` | watch status of fake snippet | `None` or `Error` |
| `watchers` | watchers of fake snippet | `Error` or `[]` |
| `get_file` | get file from fake snippet | `None` or `Error` |
| `get_node` | get node of fake snippet | `None` or `Error` |
| `update_node` | update node of fake snippet | `None` or `Error` |
| `delete_node` | delete node of fake snippet | `None` (no exception) |
| `get_node_file` | get file from node of fake snippet | `None` or `Error` |
| `diff` | diff of fake snippet at revision | `None` or `Error` |
| `patch` | patch of fake snippet at revision | `None` or `Error` |

---

## Known Spec Gaps

1. **Downloads 402 not in spec** — spec documents 403 for downloads but Bitbucket returns 402
   on Free plan. SDK returns `None` silently. Should document 402 and map to `Error`.

2. **Snippets 402 not in spec** — spec documents 404 for most snippet endpoints but not 402.
   SDK returns `None` silently for 402. Should document 402 and map to `Error`.

3. **Issues 404 in spec for list** — spec correctly documents 404 for issue list.
   SDK should surface as `Error` (handled correctly by paginator).

---

## Checklist

### issues
- [ ] list — returns Error/None, no exception
- [ ] get — returns Error/None, no exception
- [ ] create — returns Error/None, no exception
- [ ] update — returns Error/None, no exception
- [ ] delete — no exception
- [ ] comments — returns Error/None, no exception
- [ ] get_comment — returns Error/None, no exception
- [ ] add_comment — returns Error/None, no exception
- [ ] update_comment — returns Error/None, no exception
- [ ] delete_comment — no exception
- [ ] changes — returns Error/None, no exception
- [ ] get_change — returns Error/None, no exception
- [ ] add_change — returns Error/None, no exception
- [ ] vote — no exception
- [ ] unvote — no exception
- [ ] voted — returns Error/None, no exception
- [ ] watch — no exception
- [ ] unwatch — no exception
- [ ] watching — returns Error/None, no exception
- [ ] milestones — returns Error/None, no exception
- [ ] get_milestone — returns Error/None, no exception
- [ ] versions — returns Error/None, no exception
- [ ] get_version — returns Error/None, no exception
- [ ] components — returns Error/None, no exception
- [ ] get_component — returns Error/None, no exception
- [ ] attachments — returns Error/None, no exception
- [ ] get_attachment — returns Error/None, no exception
- [ ] upload_attachment — no exception
- [ ] delete_attachment — no exception
- [ ] export — no exception
- [ ] export_status — returns Error/None, no exception
- [ ] import_status — returns Error/None, no exception
- [ ] import_data — no exception

### source
- [ ] root — returns non-None, non-Error object
- [ ] root missing repo — returns Error or None
- [ ] get greet.py at seed commit — returns non-None, non-Error
- [ ] get greet.py at main — returns non-None, non-Error
- [ ] get nonexistent file — returns Error or None
- [ ] get bad commit — returns Error or None
- [ ] history greet.py — returns non-None, non-Error
- [ ] history nonexistent — returns Error or None

### downloads
- [ ] list — returns Error/None (not list), no exception
- [ ] get specific filename — returns None/Error, no exception
- [ ] delete nonexistent — no exception

### snippets
- [ ] list — returns Error/None/[], no exception
- [ ] list_all — no exception
- [ ] create — returns Error/None, no exception
- [ ] create_default — returns Error/None, no exception
- [ ] get — returns Error/None, no exception
- [ ] update — returns Error/None, no exception
- [ ] delete — no exception
- [ ] comments — returns Error/None/[], no exception
- [ ] add_comment — returns Error/None, no exception
- [ ] get_comment — returns Error/None, no exception
- [ ] update_comment — returns Error/None, no exception
- [ ] delete_comment — no exception
- [ ] commits — returns Error/None/[], no exception
- [ ] get_commit — returns Error/None, no exception
- [ ] watch — no exception
- [ ] unwatch — no exception
- [ ] watching — returns None/Error, no exception
- [ ] watchers — returns Error/None/[], no exception
- [ ] get_file — returns None/Error, no exception
- [ ] get_node — returns None/Error, no exception
- [ ] update_node — returns None/Error, no exception
- [ ] delete_node — no exception
- [ ] get_node_file — returns None/Error, no exception
- [ ] diff — returns None/Error, no exception
- [ ] patch — returns None/Error, no exception
