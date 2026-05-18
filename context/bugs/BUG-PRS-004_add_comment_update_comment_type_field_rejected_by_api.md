# BUG-PRS-004: `add_comment`/`update_comment` test sends `type` field rejected by API

**Status:** FIXED
**Layer:** test (wrong request body)
**File:** `tests/cloud/live/test_prs.py`
**Tests:** `test_add_comment`, `test_update_comment` (and any test using `PullRequestComment(type_=...)`)
**Severity:** High (every `add_comment` / `update_comment` call returns `None`; API returns 400)

---

## Symptom

`prs.add_comment` returned `None`. Inspecting the raw HTTP exchange revealed:

```
HTTP 400 Bad Request
{
  "type": "error",
  "error": {
    "message": "Bad request",
    "fields": {
      "type": "extra keys not allowed"
    }
  }
}
```

The same 400 occurred for `update_comment`.

---

## Root Cause

The test constructed the comment body with an explicit `type_` argument:

```python
comment_body = PullRequestComment(type_="pullrequest_comment", content=...)
updated_body  = PullRequestComment(type_="pullrequest_comment", content=...)
```

The attrs-based generated model serializes the `type_` attribute to `"type"` in the JSON body
(the trailing underscore is a Python convention to avoid shadowing the built-in `type`). The
Bitbucket comments POST/PUT endpoints reject any request body that contains a `"type"` key,
returning `{"fields": {"type": "extra keys not allowed"}}`.

This is distinct from BUG-PRS-003 (which was a Python-layer `AttributeError` caused by passing
`UNSET` to the SDK wrapper). BUG-PRS-004 is an HTTP-layer 400 caused by sending a disallowed
field in the serialized JSON body.

---

## Evidence

**Failing request (before fix):**
```
POST /repositories/{workspace}/{repo}/pullrequests/{id}/comments
Content-Type: application/json
Body: {"type": "pullrequest_comment", "content": {"raw": "Test comment"}}
→ 400  extra keys not allowed  (field: "type")
```

**Passing request (after fix):**
```
POST /repositories/{workspace}/{repo}/pullrequests/{id}/comments
Content-Type: application/json
Body: {"content": {"raw": "Test comment"}}
→ 201 Created
```

Verified via raw `httpx.AsyncClient().post(url, json={"content": {"raw": "..."}})` without `type`.

---

## Fix Applied

Removed `type_="pullrequest_comment"` from both `comment_body` and `updated_body` constructors
in the test.

**Before:**
```python
comment_body = PullRequestComment(
    type_="pullrequest_comment",
    content=PullrequestCommentContent(raw="Test comment via SDK"),
)
updated_body = PullRequestComment(
    type_="pullrequest_comment",
    content=PullrequestCommentContent(raw="Updated comment via SDK"),
)
```

**After:**
```python
comment_body = PullRequestComment(
    content=PullrequestCommentContent(raw="Test comment via SDK"),
)
updated_body = PullRequestComment(
    content=PullrequestCommentContent(raw="Updated comment via SDK"),
)
```

---

## Related

- **BUG-PRS-003** — Python-layer `AttributeError` in the SDK wrapper (`add_comment` passed `body=UNSET` to generated code that calls `body.to_dict()` unconditionally). That bug is at the SDK layer; this bug is at the test/HTTP layer. Both affect `add_comment` but are independent failures.

---

## Status

- [x] Root cause confirmed via live API call (400 with `"type"` field present)
- [x] Fix confirmed via live API call (201 without `"type"` field)
- [x] Fix applied to `tests/cloud/live/test_prs.py`
