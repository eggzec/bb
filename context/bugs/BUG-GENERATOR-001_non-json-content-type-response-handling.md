# BUG-GENERATOR-001: `_parse_response()` crashes on non-JSON content-type responses

**Status:** FIXED
**Layer:** generator (template override)
**Template:** `templates/endpoint_macros.py.jinja` — `parse_response` macro
**Severity:** High — `json.JSONDecodeError` raised at runtime whenever Bitbucket returns an HTML or plain-text error page for a JSON-schema-mapped endpoint

---

## Description

The `openapi-python-client` generator produces `_parse_response()` functions for every documented response code. When a response code is mapped to a JSON schema in the spec, the generated code unconditionally calls `response.json()` to deserialise the body. If the actual HTTP response has a non-JSON content type (e.g. `text/html`, `text/plain`), `.json()` raises a `json.JSONDecodeError` at the call site, crashing the SDK wrapper with an unhandled exception.

This matters because the Bitbucket API does not exclusively return `application/json` for error responses. Certain 404s — particularly those triggered by deeply invalid path parameters that reach Bitbucket's web layer before the API routing layer — return a full HTML error page with `Content-Type: text/html`.

---

## Root Cause

The upstream `openapi-python-client` `parse_response` macro (in the installed package template) generates code that unconditionally dereferences the response body as JSON for all responses mapped to a JSON schema:

```jinja
{# Upstream default — no content-type guard #}
{% macro parse_response(parsed_responses, response) %}
{% if parsed_responses %}{% import "property_templates/" + response.prop.template as prop_template %}
{% if prop_template.construct %}
{{ prop_template.construct(response.prop, response.source.attribute) }}
{% elif response.source.return_type == response.prop.get_type_string() %}
{{ response.prop.python_name }} = {{ response.source.attribute }}
{% else %}
{{ response.prop.python_name }} = cast({{ response.prop.get_type_string() }}, {{ response.source.attribute }})
{% endif %}
return {{ response.prop.python_name }}
{% else %}
return None
{% endif %}
{% endmacro %}
```

In the generated Python, `response.source.attribute` for a JSON-mapped response evaluates to `response.json()`. The generated `_parse_response()` therefore contains:

```python
# Generated without the fix — crashes on non-JSON body
if response.status_code == 200:
    response_200 = SomeModel.from_dict(response.json())  # raises JSONDecodeError if HTML
    return response_200
```

There is no guard checking whether the response actually carries a JSON content type before calling `.json()`.

---

## When This Triggers in Practice

Bitbucket's API infrastructure has multiple routing layers. Requests with pathological path parameters (e.g. `workspace=0`, `repo_slug=0`, `commit=0`) can be handled by the web tier rather than the API tier, producing a full HTML error page instead of a JSON error object — even for endpoints that only document JSON responses.

Confirmed endpoints that exhibit this with `workspace=0 / repo_slug=0` style parameters:

| Endpoint | Status | Content-Type |
|---|---|---|
| `GET /repositories/{workspace}/{repo_slug}/commit/{commit}` | 404 | `text/html` |
| `GET /repositories/{workspace}/{repo_slug}/commits` | 404 | `text/html` |
| `GET /repositories/{workspace}/{repo_slug}/commits/{revision}` | 404 | `text/html` |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/activity` | 404 | `text/html` |
| `GET /repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity` | 404 | `text/html` |

Verification command:

```bash
source .env
curl -s -I -u "$BB_EMAIL:$BB_TOKEN" \
  "https://api.bitbucket.org/2.0/repositories/invalid-workspace-0/invalid-repo-0/commit/0" \
  | grep -i "content-type\|http/"
# HTTP/2 404
# content-type: text/html; charset=utf-8
```

---

## Fix Applied

A project-local override of the `parse_response` macro was added in `templates/endpoint_macros.py.jinja` (lines 201–218). The fix inserts a content-type guard immediately before any `response.json()` dereference:

```jinja
{# Patched macro — guards against non-JSON content-type #}
{% macro parse_response(parsed_responses, response) %}
{% if parsed_responses %}{% import "property_templates/" + response.prop.template as prop_template %}
{% if response.source.attribute == "response.json()" %}
if "application/json" not in response.headers.get("content-type", ""):
    return None
{% endif %}
{% if prop_template.construct %}
{{ prop_template.construct(response.prop, response.source.attribute) }}
{% elif response.source.return_type == response.prop.get_type_string() %}
{{ response.prop.python_name }} = {{ response.source.attribute }}
{% else %}
{{ response.prop.python_name }} = cast({{ response.prop.get_type_string() }}, {{ response.source.attribute }})
{% endif %}
return {{ response.prop.python_name }}
{% else %}
return None
{% endif %}
{% endmacro %}
```

The condition `response.source.attribute == "response.json()"` targets only JSON-mapped responses. Responses that use `response.text`, `response.content`, or other attributes are not affected. The guard is rendered into the generated Python output as:

```python
# Generated with the fix — safe for non-JSON bodies
if response.status_code == 200:
    if "application/json" not in response.headers.get("content-type", ""):
        return None
    response_200 = SomeModel.from_dict(response.json())
    return response_200
```

When a non-JSON content-type is detected, `_parse_response()` returns `None` rather than crashing. The SDK wrapper (which calls `asyncio()` or `sync()`) receives `None` and propagates it to the caller cleanly.

---

## Impact (Before Fix)

- Any SDK call to an affected endpoint that received an HTML error page raised `json.JSONDecodeError` at the `response.json()` call site inside the generated `_parse_response()`.
- The exception propagated uncaught through `asyncio()` / `sync()` to the SDK wrapper and ultimately to user code.
- This was especially likely to surface during schemathesis conformance runs (random `0`-valued path params) and in any integration environment where auth/routing issues cause Bitbucket to serve HTML errors.
- The bug affects every generated endpoint module, not just the confirmed list above — any endpoint where the live API can return a non-JSON body for a JSON-schema-mapped status code is vulnerable.

---

## Related Bugs

- **BUG-SOURCE-001**: `source.get` returned `None` for `text/plain` files — a different manifestation of the same generator limitation (no non-JSON support), fixed at the SDK-wrapper layer instead.
- **BUG-PIPELINES-007**: `step_log` always returned `None` for `text/plain` pipeline log responses — also fixed at the SDK-wrapper layer.

The generator template fix (this bug) addresses the crash case (non-JSON body where JSON is expected). The SDK-wrapper fixes address the silent-None case (non-JSON body where the endpoint legitimately serves non-JSON content).

---

## Files Changed

| File | Change |
|---|---|
| `templates/endpoint_macros.py.jinja` | Added project-local override of `parse_response` macro with content-type guard |

The fix was introduced in commit `687b0c2` (fix other issues and added handling of the 403 missing cases) alongside the 403 spec additions. After this template is in place, every subsequent `make generate-cloud` or `make generate-dc` bakes the guard into all generated `_parse_response()` functions automatically.

---

## Spec-Side Assessment

The `text/html` responses that triggered this bug are **not intentional Bitbucket API responses** — they are produced by Bitbucket's CDN/WAF infrastructure when path parameters are so malformed (e.g. `workspace=0`, `repo_slug=0`) that the request never reaches the API routing layer. Adding `text/html` as a documented content type for any JSON-schema endpoint would be a lie about the API contract: it would cause the generator to emit `response.text` deserialization paths for HTML error pages that no real client should ever parse. The spec already correctly documents the legitimate non-JSON content types: `text/plain` appears only in the descriptions of diff and patch endpoints (which return a 302 redirect, not a direct 200 with plain text), and those endpoints already use `asyncio_detailed()` plus manual content-type branching in the SDK wrappers (`prs.diff`, `prs.patch`, `pipelines.step_log`). There is no spec-side fix that accurately represents this class of CDN/WAF-layer HTML errors; the template patch at `templates/endpoint_macros.py.jinja` line 204 is the correct approach — it is a defensive runtime guard that returns `None` gracefully instead of crashing, without adding false documentation to the spec.
