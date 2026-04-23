"""Bitbucket Data Center secret-scanning synchronous SDK wrappers.

Synchronous wrappers around :mod:`bb.datacenter.sdk.security` using :func:`asyncio.run`.


Covers project-level secret scanning allowlist rules under:
  ``/api/latest/projects/{projectKey}/secret-scanning/allowlist``"""
from __future__ import annotations
import asyncio
from bb.datacenter.models.rest_secret_scanning_allowlist_rule import RestSecretScanningAllowlistRule
from bb.datacenter.models.rest_secret_scanning_allowlist_rule_set_request import RestSecretScanningAllowlistRuleSetRequest
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.types import UNSET, Unset
from bb.datacenter.sdk import security as _async
__all__ = ['list_allowlist_rules', 'create_allowlist_rule', 'get_allowlist_rule', 'update_allowlist_rule', 'delete_allowlist_rule']

def list_allowlist_rules(client: BBDCClient, project_key: str, *, filter_: str | Unset=UNSET, limit: int=25) -> list[RestSecretScanningAllowlistRule]:
    """List all secret-scanning allowlist rules for a project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.security.list_allowlist_rules`.

Args:
    client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
    project_key: The project key (e.g. ``"PRJ"``).
    filter_: Optional text filter to narrow results by rule name.
    limit: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.datacenter.models.rest_secret_scanning_allowlist_rule.RestSecretScanningAllowlistRule`
    objects across all pages.

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
        unrecognised or unsupported auth method.
    :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.datacenter import BBDCClient
    from bb.datacenter.sdk import security

    client = BBDCClient.from_env()
    rules = security.list_allowlist_rules(client, project_key="PRJ")
    ```

References:
    `GET /api/latest/projects/{projectKey}/secret-scanning/allowlist
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-security/#api-api-latest-projects-projectkey-secret-scanning-allowlist-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.security.list_allowlist_rules`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list_allowlist_rules(client, project_key, filter_=filter_, limit=limit))

def create_allowlist_rule(client: BBDCClient, project_key: str, *, body: RestSecretScanningAllowlistRuleSetRequest) -> RestSecretScanningAllowlistRule | None:
    """Create a secret-scanning allowlist rule for a project.

Synchronous wrapper around :func:`~bb.datacenter.sdk.security.create_allowlist_rule`.

Args:
    client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
    project_key: The project key (e.g. ``"PRJ"``).
    body: :class:`~bb.datacenter.models.rest_secret_scanning_allowlist_rule_set_request.RestSecretScanningAllowlistRuleSetRequest`
        with ``name`` and ``pattern``.

Returns:
    The created :class:`~bb.datacenter.models.rest_secret_scanning_allowlist_rule.RestSecretScanningAllowlistRule`,
    or ``None`` on error.

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
        unrecognised or unsupported auth method.
    :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.datacenter import BBDCClient
    from bb.datacenter.models.rest_secret_scanning_allowlist_rule_set_request import (
        RestSecretScanningAllowlistRuleSetRequest,
    )
    from bb.datacenter.sdk import security

    client = BBDCClient.from_env()
    rule = security.create_allowlist_rule(
        client,
        project_key="PRJ",
        body=RestSecretScanningAllowlistRuleSetRequest(name="ci-token", pattern="CI_TOKEN=.*"),
    )
    ```

References:
    `POST /api/latest/projects/{projectKey}/secret-scanning/allowlist
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-security/#api-api-latest-projects-projectkey-secret-scanning-allowlist-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.security.create_allowlist_rule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_allowlist_rule(client, project_key, body=body))

def get_allowlist_rule(client: BBDCClient, project_key: str, rule_id: str) -> RestSecretScanningAllowlistRule | None:
    """Fetch a single secret-scanning allowlist rule by ID.

Synchronous wrapper around :func:`~bb.datacenter.sdk.security.get_allowlist_rule`.

Args:
    client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
    project_key: The project key (e.g. ``"PRJ"``).
    rule_id: The rule ID.

Returns:
    The :class:`~bb.datacenter.models.rest_secret_scanning_allowlist_rule.RestSecretScanningAllowlistRule`,
    or ``None`` if not found.

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
        unrecognised or unsupported auth method.
    :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

References:
    `GET /api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-security/#api-api-latest-projects-projectkey-secret-scanning-allowlist-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.security.get_allowlist_rule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_allowlist_rule(client, project_key, rule_id))

def update_allowlist_rule(client: BBDCClient, project_key: str, rule_id: str, *, body: RestSecretScanningAllowlistRuleSetRequest) -> RestSecretScanningAllowlistRule | None:
    """Update an existing secret-scanning allowlist rule.

Synchronous wrapper around :func:`~bb.datacenter.sdk.security.update_allowlist_rule`.

Args:
    client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
    project_key: The project key (e.g. ``"PRJ"``).
    rule_id: The rule ID.
    body: Updated rule details.

Returns:
    The updated :class:`~bb.datacenter.models.rest_secret_scanning_allowlist_rule.RestSecretScanningAllowlistRule`,
    or ``None`` on error.

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
        unrecognised or unsupported auth method.
    :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

References:
    `PUT /api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-security/#api-api-latest-projects-projectkey-secret-scanning-allowlist-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.security.update_allowlist_rule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_allowlist_rule(client, project_key, rule_id, body=body))

def delete_allowlist_rule(client: BBDCClient, project_key: str, rule_id: str) -> None:
    """Delete a secret-scanning allowlist rule.

Synchronous wrapper around :func:`~bb.datacenter.sdk.security.delete_allowlist_rule`.

Args:
    client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
    project_key: The project key (e.g. ``"PRJ"``).
    rule_id: The rule ID.

Returns:
    ``None``.

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
        unrecognised or unsupported auth method.
    :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

References:
    `DELETE /api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-security/#api-api-latest-projects-projectkey-secret-scanning-allowlist-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.security.delete_allowlist_rule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_allowlist_rule(client, project_key, rule_id))
