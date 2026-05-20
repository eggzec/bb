from __future__ import annotations
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_known_host import PipelineKnownHost
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import pipelines as _async
__all__ = ['list', 'get', 'run', 'stop', 'steps', 'step', 'step_log', 'config', 'update_config', 'variables', 'get_variable', 'create_variable', 'update_variable', 'delete_variable', 'schedules', 'get_schedule', 'create_schedule', 'update_schedule', 'delete_schedule', 'known_hosts', 'get_known_host', 'create_known_host', 'update_known_host', 'delete_known_host', 'ssh_key_pair', 'update_ssh_key_pair', 'delete_ssh_key_pair', 'caches', 'delete_cache', 'oidc_config', 'oidc_keys', 'workspace_variables', 'get_workspace_variable', 'create_workspace_variable', 'update_workspace_variable', 'delete_workspace_variable', 'runners', 'get_runner', 'create_runner', 'update_runner', 'delete_runner', 'workspace_runners', 'get_workspace_runner', 'create_workspace_runner', 'update_workspace_runner', 'delete_workspace_runner', 'test_reports', 'test_cases', 'test_case_reasons', 'container_log', 'cache_uri', 'clear_caches', 'schedule_executions', 'update_build_number']

def list(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=10) -> list[Pipeline] | Error:
    """Return all pipelines for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.list`.

Paginates automatically, collecting every page into a single list. Only
items that parse to a :class:`~bb.cloud.models.pipeline.Pipeline` instance
are included in the result.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``10``.

Returns:
    List of :class:`~bb.cloud.models.pipeline.Pipeline` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    result = pipelines.list(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> Pipeline | Error | None:
    """Return a single pipeline by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline.Pipeline` instance, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipeline = pipelines.get(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, pipeline_uuid))

def run(client: BBClient, workspace: str, repo_slug: str, *, body: Pipeline) -> Pipeline | Error | None:
    """Trigger a new pipeline run and return the created pipeline.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.run`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline.Pipeline` object describing the
        pipeline to run, including its target branch, tag, or custom target.

Returns:
    The created :class:`~bb.cloud.models.pipeline.Pipeline` instance, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline import Pipeline

    client = BBClient.from_env()
    pipeline = pipelines.run(
        client, workspace="myws", repo_slug="myrepo",
        body=Pipeline(...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.run`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.run(client, workspace, repo_slug, body=body))

def stop(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> None:
    """Stop a running pipeline.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.stop`.

Issues a stop request for the given pipeline. No error is raised if the
pipeline has already completed.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.stop(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}"
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-stoppipeline-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.stop`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.stop(client, workspace, repo_slug, pipeline_uuid))

def steps(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all steps for a pipeline across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.steps`.

Paginates automatically, collecting every page into a single list.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of pipeline step objects
    (:class:`~bb.cloud.models.pipeline_step.PipelineStep`).

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    result = pipelines.steps(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.steps`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.steps(client, workspace, repo_slug, pipeline_uuid, pagelen=pagelen))

def step(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, step_uuid: str) -> Any:
    """Return a single pipeline step by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.step`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    step_uuid: Step UUID (e.g. ``{step-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_step.PipelineStep` object, or ``None``
    if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    s = pipelines.step(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}", step_uuid="{step-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.step`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.step(client, workspace, repo_slug, pipeline_uuid, step_uuid))

def step_log(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, step_uuid: str) -> str | Error | None:
    """Return the log output for a pipeline step.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.step_log`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    step_uuid: Step UUID (e.g. ``{step-uuid}``).

Returns:
    Log text as a string, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    log = pipelines.step_log(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}", step_uuid="{step-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-log-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.step_log`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.step_log(client, workspace, repo_slug, pipeline_uuid, step_uuid))

def config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the pipeline configuration for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.config`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    A :class:`~bb.cloud.models.pipelines_config.PipelinesConfig` object,
    or ``None`` if not configured.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    cfg = pipelines.config(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.config`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.config(client, workspace, repo_slug))

def update_config(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> Any:
    """Update the pipeline configuration for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_config`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: Updated :class:`~bb.cloud.models.pipelines_config.PipelinesConfig`
        request body. Omit to send an empty update.

Returns:
    The updated :class:`~bb.cloud.models.pipelines_config.PipelinesConfig` object,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    cfg = pipelines.update_config(
        client, workspace="myws", repo_slug="myrepo", body=...
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_config`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_config(client, workspace, repo_slug, body=body))

def variables(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[PipelineVariable] | Error:
    """Return all pipeline variables for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.variables`.

Paginates automatically, collecting every page into a single list. Only
items that parse to a :class:`~bb.cloud.models.pipeline_variable.PipelineVariable`
instance are included.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    vars_ = pipelines.variables(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.variables`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.variables(client, workspace, repo_slug, pagelen=pagelen))

def get_variable(client: BBClient, workspace: str, repo_slug: str, variable_uuid: str) -> PipelineVariable | Error | None:
    """Return a single pipeline variable for a repository by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    var = pipelines.get_variable(
        client, workspace="myws", repo_slug="myrepo",
        variable_uuid="{var-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_variable(client, workspace, repo_slug, variable_uuid))

def create_variable(client: BBClient, workspace: str, repo_slug: str, *, body: PipelineVariable | Unset=UNSET) -> PipelineVariable | Error | None:
    """Create a pipeline variable for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` request body
        defining the variable's key, value, and secured status.

Returns:
    The created :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_variable import PipelineVariable

    client = BBClient.from_env()
    var = pipelines.create_variable(
        client, workspace="myws", repo_slug="myrepo",
        body=PipelineVariable(key="MY_VAR", value="secret", secured=True)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_variable(client, workspace, repo_slug, body=body))

def update_variable(client: BBClient, workspace: str, repo_slug: str, variable_uuid: str, *, body: PipelineVariable | Unset=UNSET) -> PipelineVariable | Error | None:
    """Update a pipeline variable for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).
    body: :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` request body
        with updated fields.

Returns:
    The updated :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_variable import PipelineVariable

    client = BBClient.from_env()
    var = pipelines.update_variable(
        client, workspace="myws", repo_slug="myrepo",
        variable_uuid="{var-uuid}",
        body=PipelineVariable(value="new-value")
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_variable(client, workspace, repo_slug, variable_uuid, body=body))

def delete_variable(client: BBClient, workspace: str, repo_slug: str, variable_uuid: str) -> None:
    """Delete a pipeline variable for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_variable(
        client, workspace="myws", repo_slug="myrepo",
        variable_uuid="{var-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_variable(client, workspace, repo_slug, variable_uuid))

def schedules(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[PipelineSchedule] | Error:
    """Return all pipeline schedules for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.schedules`.

Paginates automatically, collecting every page into a single list. Only
items that parse to a :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule`
instance are included.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    scheds = pipelines.schedules(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.schedules`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.schedules(client, workspace, repo_slug, pagelen=pagelen))

def get_schedule(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> PipelineSchedule | Error | None:
    """Return a single pipeline schedule by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_schedule`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    schedule_uuid: Schedule UUID (e.g. ``{schedule-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` instance,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    sched = pipelines.get_schedule(
        client, workspace="myws", repo_slug="myrepo",
        schedule_uuid="{schedule-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_schedule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_schedule(client, workspace, repo_slug, schedule_uuid))

def create_schedule(client: BBClient, workspace: str, repo_slug: str, *, body: PipelineSchedule | Unset=UNSET) -> PipelineSchedule | Error | None:
    """Create a pipeline schedule for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_schedule`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` request body
        defining the schedule's cron expression and target.

Returns:
    The created :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_schedule_post_request_body import (
        PipelineSchedulePostRequestBody,
    )

    client = BBClient.from_env()
    sched = pipelines.create_schedule(
        client, workspace="myws", repo_slug="myrepo",
        body=PipelineSchedulePostRequestBody(...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_schedule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_schedule(client, workspace, repo_slug, body=body))

def update_schedule(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str, *, body: PipelineSchedule | Unset=UNSET) -> PipelineSchedule | Error | None:
    """Update a pipeline schedule for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_schedule`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    schedule_uuid: Schedule UUID (e.g. ``{schedule-uuid}``).
    body: :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` request body
        with updated fields.

Returns:
    The updated :class:`~bb.cloud.models.pipeline_schedule.PipelineSchedule` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    sched = pipelines.update_schedule(
        client, workspace="myws", repo_slug="myrepo",
        schedule_uuid="{schedule-uuid}", body=...
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_schedule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_schedule(client, workspace, repo_slug, schedule_uuid, body=body))

def delete_schedule(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> None:
    """Delete a pipeline schedule for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_schedule`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    schedule_uuid: Schedule UUID (e.g. ``{schedule-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_schedule(
        client, workspace="myws", repo_slug="myrepo",
        schedule_uuid="{schedule-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_schedule`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_schedule(client, workspace, repo_slug, schedule_uuid))

def known_hosts(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[PipelineKnownHost] | Error:
    """Return all known hosts for the repository's pipeline SSH configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.known_hosts`.

Paginates automatically, collecting every page into a single list. Only
items that parse to a :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost`
instance are included.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    hosts = pipelines.known_hosts(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.known_hosts`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.known_hosts(client, workspace, repo_slug, pagelen=pagelen))

def get_known_host(client: BBClient, workspace: str, repo_slug: str, known_host_uuid: str) -> PipelineKnownHost | Error | None:
    """Return a single known host by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_known_host`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    known_host_uuid: Known host UUID (e.g. ``{host-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` instance,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    host = pipelines.get_known_host(
        client, workspace="myws", repo_slug="myrepo",
        known_host_uuid="{host-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_known_host`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_known_host(client, workspace, repo_slug, known_host_uuid))

def create_known_host(client: BBClient, workspace: str, repo_slug: str, *, body: PipelineKnownHost | Unset=UNSET) -> PipelineKnownHost | Error | None:
    """Add a known host to the repository's pipeline SSH configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_known_host`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` request body
        specifying the host name and public key fingerprint.

Returns:
    The created :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_known_host import PipelineKnownHost

    client = BBClient.from_env()
    host = pipelines.create_known_host(
        client, workspace="myws", repo_slug="myrepo",
        body=PipelineKnownHost(hostname="github.com", ...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_known_host`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_known_host(client, workspace, repo_slug, body=body))

def update_known_host(client: BBClient, workspace: str, repo_slug: str, known_host_uuid: str, *, body: PipelineKnownHost | Unset=UNSET) -> PipelineKnownHost | Error | None:
    """Update a known host in the repository's pipeline SSH configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_known_host`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    known_host_uuid: Known host UUID (e.g. ``{host-uuid}``).
    body: :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` request body
        with updated fields.

Returns:
    The updated :class:`~bb.cloud.models.pipeline_known_host.PipelineKnownHost` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    host = pipelines.update_known_host(
        client, workspace="myws", repo_slug="myrepo",
        known_host_uuid="{host-uuid}", body=...
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_known_host`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_known_host(client, workspace, repo_slug, known_host_uuid, body=body))

def delete_known_host(client: BBClient, workspace: str, repo_slug: str, known_host_uuid: str) -> None:
    """Remove a known host from the repository's pipeline SSH configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_known_host`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    known_host_uuid: Known host UUID (e.g. ``{host-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_known_host(
        client, workspace="myws", repo_slug="myrepo",
        known_host_uuid="{host-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_known_host`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_known_host(client, workspace, repo_slug, known_host_uuid))

def ssh_key_pair(client: BBClient, workspace: str, repo_slug: str) -> PipelineSshKeyPair | Error | None:
    """Return the SSH key pair for the repository's pipeline configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.ssh_key_pair`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    A :class:`~bb.cloud.models.pipeline_ssh_key_pair.PipelineSshKeyPair` instance,
    or ``None`` if no key pair is configured.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    key_pair = pipelines.ssh_key_pair(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.ssh_key_pair`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.ssh_key_pair(client, workspace, repo_slug))

def update_ssh_key_pair(client: BBClient, workspace: str, repo_slug: str, *, body: PipelineSshKeyPair | Unset=UNSET) -> PipelineSshKeyPair | Error | None:
    """Create or update the SSH key pair for the repository's pipeline configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_ssh_key_pair`.

If no key pair exists, a new one is created. If one already exists, it is
replaced.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_ssh_key_pair.PipelineSshKeyPair`
        request body containing the private and public key strings.

Returns:
    The created or updated :class:`~bb.cloud.models.pipeline_ssh_key_pair.PipelineSshKeyPair`
    instance, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair

    client = BBClient.from_env()
    key_pair = pipelines.update_ssh_key_pair(
        client, workspace="myws", repo_slug="myrepo",
        body=PipelineSshKeyPair(private_key="...", public_key="...")
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_ssh_key_pair`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_ssh_key_pair(client, workspace, repo_slug, body=body))

def delete_ssh_key_pair(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete the SSH key pair from the repository's pipeline configuration.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_ssh_key_pair`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_ssh_key_pair(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_ssh_key_pair`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_ssh_key_pair(client, workspace, repo_slug))

def caches(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Any] | Error:
    """Return all pipeline caches for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.caches`.

Paginates automatically, collecting every page into a single list.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of pipeline cache objects
    (:class:`~bb.cloud.models.pipeline_cache.PipelineCache`).

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    result = pipelines.caches(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.caches`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.caches(client, workspace, repo_slug, pagelen=pagelen))

def delete_cache(client: BBClient, workspace: str, repo_slug: str, cache_uuid: str) -> None:
    """Delete a pipeline cache by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_cache`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    cache_uuid: Cache UUID (e.g. ``{cache-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_cache(
        client, workspace="myws", repo_slug="myrepo",
        cache_uuid="{cache-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches/{cache_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-cache-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_cache`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_cache(client, workspace, repo_slug, cache_uuid))

def oidc_config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the OIDC configuration for a workspace's pipelines.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.oidc_config`.

Retrieves the OpenID Connect well-known configuration document that
describes the OIDC endpoints and claims for the workspace.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID (passed through to the underlying API call).

Returns:
    OIDC configuration document, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    oidc = pipelines.oidc_config(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-identity-oidc-well-known-openid-configuration-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.oidc_config`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.oidc_config(client, workspace, repo_slug))

def oidc_keys(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the OIDC public key set for a workspace's pipelines.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.oidc_keys`.

Retrieves the JSON Web Key Set (JWKS) used to verify OIDC tokens issued
by Bitbucket Pipelines for the workspace.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID (passed through to the underlying API call).

Returns:
    JWKS document, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    keys = pipelines.oidc_keys(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/keys.json
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-identity-oidc-keys-json-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.oidc_keys`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.oidc_keys(client, workspace, repo_slug))

def workspace_variables(client: BBClient, workspace: str, *, pagelen: int=25) -> list[PipelineVariable] | Error:
    """Return all pipeline variables for a workspace across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.workspace_variables`.

Paginates automatically, collecting every page into a single list. Only
items that parse to a :class:`~bb.cloud.models.pipeline_variable.PipelineVariable`
instance are included.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    vars_ = pipelines.workspace_variables(client, workspace="myws")
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.workspace_variables`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.workspace_variables(client, workspace, pagelen=pagelen))

def get_workspace_variable(client: BBClient, workspace: str, variable_uuid: str) -> PipelineVariable | Error | None:
    """Return a single workspace pipeline variable by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_workspace_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    var = pipelines.get_workspace_variable(
        client, workspace="myws", variable_uuid="{var-uuid}"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_workspace_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_workspace_variable(client, workspace, variable_uuid))

def create_workspace_variable(client: BBClient, workspace: str, *, body: PipelineVariable | Unset=UNSET) -> PipelineVariable | Error | None:
    """Create a pipeline variable for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_workspace_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` request body
        defining the variable's key, value, and secured status.

Returns:
    The created :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_variable import PipelineVariable

    client = BBClient.from_env()
    var = pipelines.create_workspace_variable(
        client, workspace="myws",
        body=PipelineVariable(key="MY_VAR", value="secret", secured=True)
    )
    ```

References:
    `POST /2.0/workspaces/{workspace}/pipelines-config/variables
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_workspace_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_workspace_variable(client, workspace, body=body))

def update_workspace_variable(client: BBClient, workspace: str, variable_uuid: str, *, body: PipelineVariable | Unset=UNSET) -> PipelineVariable | Error | None:
    """Update a workspace pipeline variable.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_workspace_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).
    body: :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` request body
        with updated fields.

Returns:
    The updated :class:`~bb.cloud.models.pipeline_variable.PipelineVariable` instance,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_variable import PipelineVariable

    client = BBClient.from_env()
    var = pipelines.update_workspace_variable(
        client, workspace="myws", variable_uuid="{var-uuid}",
        body=PipelineVariable(value="new-value")
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_workspace_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_workspace_variable(client, workspace, variable_uuid, body=body))

def delete_workspace_variable(client: BBClient, workspace: str, variable_uuid: str) -> None:
    """Delete a workspace pipeline variable.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_workspace_variable`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    variable_uuid: Variable UUID (e.g. ``{var-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_workspace_variable(
        client, workspace="myws", variable_uuid="{var-uuid}"
    )
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_workspace_variable`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_workspace_variable(client, workspace, variable_uuid))

def runners(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return all self-hosted runners for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.runners`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    Paginated runner list response, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    result = pipelines.runners(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.runners`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.runners(client, workspace, repo_slug))

def get_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str) -> Any:
    """Return a single repository runner by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).

Returns:
    A runner object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.get_runner(
        client, workspace="myws", repo_slug="myrepo",
        runner_uuid="{runner-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_runner(client, workspace, repo_slug, runner_uuid))

def create_runner(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> Any:
    """Create a self-hosted runner for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: Runner request body. Omit to use defaults.

Returns:
    The created runner object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.create_runner(
        client, workspace="myws", repo_slug="myrepo", body=...
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_runner(client, workspace, repo_slug, body=body))

def update_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str, *, body: Unset=UNSET) -> Any:
    """Update a repository runner.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).
    body: Runner request body with updated fields.

Returns:
    The updated runner object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.update_runner(
        client, workspace="myws", repo_slug="myrepo",
        runner_uuid="{runner-uuid}", body=...
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_runner(client, workspace, repo_slug, runner_uuid, body=body))

def delete_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str) -> None:
    """Delete a repository runner.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_runner(
        client, workspace="myws", repo_slug="myrepo",
        runner_uuid="{runner-uuid}"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_runner(client, workspace, repo_slug, runner_uuid))

def workspace_runners(client: BBClient, workspace: str) -> Any:
    """Return all self-hosted runners for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.workspace_runners`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.

Returns:
    Paginated runner list response, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    result = pipelines.workspace_runners(client, workspace="myws")
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/runners
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.workspace_runners`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.workspace_runners(client, workspace))

def get_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> Any:
    """Return a single workspace runner by UUID.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.get_workspace_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).

Returns:
    A runner object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.get_workspace_runner(
        client, workspace="myws", runner_uuid="{runner-uuid}"
    )
    ```

References:
    `GET /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.get_workspace_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_workspace_runner(client, workspace, runner_uuid))

def create_workspace_runner(client: BBClient, workspace: str, *, body: Unset=UNSET) -> Any:
    """Create a self-hosted runner for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.create_workspace_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    body: Runner request body. Omit to use defaults.

Returns:
    The created runner object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.create_workspace_runner(
        client, workspace="myws", body=...
    )
    ```

References:
    `POST /2.0/workspaces/{workspace}/pipelines-config/runners
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.create_workspace_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create_workspace_runner(client, workspace, body=body))

def update_workspace_runner(client: BBClient, workspace: str, runner_uuid: str, *, body: Unset=UNSET) -> Any:
    """Update a workspace runner.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_workspace_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).
    body: Runner request body with updated fields.

Returns:
    The updated runner object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    runner = pipelines.update_workspace_runner(
        client, workspace="myws", runner_uuid="{runner-uuid}", body=...
    )
    ```

References:
    `PUT /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_workspace_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_workspace_runner(client, workspace, runner_uuid, body=body))

def delete_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> None:
    """Delete a workspace runner.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.delete_workspace_runner`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    runner_uuid: Runner UUID (e.g. ``{runner-uuid}``).

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.delete_workspace_runner(
        client, workspace="myws", runner_uuid="{runner-uuid}"
    )
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.delete_workspace_runner`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_workspace_runner(client, workspace, runner_uuid))

def test_reports(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> Any:
    """Return test reports for a pipeline.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.test_reports`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).

Returns:
    Test report data, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    reports = pipelines.test_reports(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.test_reports`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.test_reports(client, workspace, repo_slug, pipeline_uuid))

def test_cases(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, report_uuid: str) -> Any:
    """Return test cases for a pipeline test report.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.test_cases`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    report_uuid: Step UUID identifying the test report to retrieve cases from.

Returns:
    Test case data, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    cases = pipelines.test_cases(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}", report_uuid="{step-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports/test-cases
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-test-cases-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.test_cases`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.test_cases(client, workspace, repo_slug, pipeline_uuid, report_uuid))

def test_case_reasons(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, report_uuid: str, test_case_uuid: str) -> Any:
    """Return failure reasons for a specific test case.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.test_case_reasons`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    report_uuid: Step UUID identifying the test report.
    test_case_uuid: Test case UUID (e.g. ``{test-case-uuid}``).

Returns:
    Test case reason data, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    reasons = pipelines.test_case_reasons(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}", report_uuid="{step-uuid}",
        test_case_uuid="{test-case-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports/test-cases/{test_case_uuid}/test-case-reasons
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-test-cases-test-case-uuid-test-case-reasons-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.test_case_reasons`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.test_case_reasons(client, workspace, repo_slug, pipeline_uuid, report_uuid, test_case_uuid))

def container_log(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, step_uuid: str, service_name: str) -> Any:
    """Return the log for a pipeline container (service) within a step.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.container_log`.

Retrieves the log output for a named service container that ran as part of
a pipeline step (e.g. a Docker service defined in ``bitbucket-pipelines.yml``).

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pipeline_uuid: Pipeline UUID (e.g. ``{abc-123-uuid}``).
    step_uuid: Step UUID (e.g. ``{step-uuid}``).
    service_name: Service/container name or log UUID identifying the container log.

Returns:
    Container log content, or ``None`` if not available.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    log = pipelines.container_log(
        client, workspace="myws", repo_slug="myrepo",
        pipeline_uuid="{abc-123}", step_uuid="{step-uuid}",
        service_name="docker"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-logs-log-uuid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.container_log`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.container_log(client, workspace, repo_slug, pipeline_uuid, step_uuid, service_name))

def cache_uri(client: BBClient, workspace: str, repo_slug: str, cache_uuid: str) -> Any:
    """Return the download URI for a pipeline cache.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.cache_uri`.

The returned URI can be used to download the cache content directly.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    cache_uuid: Cache UUID (e.g. ``{cache-uuid}``).

Returns:
    A :class:`~bb.cloud.models.pipeline_cache_content_uri.PipelineCacheContentUri`
    object containing the download URL, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    uri = pipelines.cache_uri(
        client, workspace="myws", repo_slug="myrepo",
        cache_uuid="{cache-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches/{cache_uuid}/content-uri
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-cache-uuid-content-uri-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.cache_uri`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.cache_uri(client, workspace, repo_slug, cache_uuid))

def clear_caches(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete all pipeline caches for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.clear_caches`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.

Returns:
    ``None``

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    pipelines.clear_caches(
        client, workspace="myws", repo_slug="myrepo"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.clear_caches`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.clear_caches(client, workspace, repo_slug))

def schedule_executions(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> Any:
    """Return the execution history for a pipeline schedule.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.schedule_executions`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    schedule_uuid: Schedule UUID (e.g. ``{schedule-uuid}``).

Returns:
    Paginated execution history response, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines

    client = BBClient.from_env()
    history = pipelines.schedule_executions(
        client, workspace="myws", repo_slug="myrepo",
        schedule_uuid="{schedule-uuid}"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}/executions
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-executions-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.schedule_executions`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.schedule_executions(client, workspace, repo_slug, schedule_uuid))

def update_build_number(client: BBClient, workspace: str, repo_slug: str, *, body: Unset=UNSET) -> Any:
    """Update the next build number for a repository's pipelines.

Synchronous wrapper around :func:`~bb.cloud.sdk.pipelines.update_build_number`.

Sets a new minimum value for the auto-incrementing build number counter.
The value must be higher than the current build number.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: :class:`~bb.cloud.models.pipeline_build_number.PipelineBuildNumber`
        request body specifying the new ``next`` build number value.

Returns:
    The updated :class:`~bb.cloud.models.pipeline_build_number.PipelineBuildNumber`
    object, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import pipelines
    from bb.cloud.models.pipeline_build_number import PipelineBuildNumber

    client = BBClient.from_env()
    result = pipelines.update_build_number(
        client, workspace="myws", repo_slug="myrepo",
        body=PipelineBuildNumber(next=100)
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/build_number
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-build-number-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.pipelines.update_build_number`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_build_number(client, workspace, repo_slug, body=body))
