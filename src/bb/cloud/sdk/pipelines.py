from __future__ import annotations

from typing import Any

from bb.cloud.api.pipelines import (
    create_pipeline_for_repository,
    create_pipeline_variable_for_workspace,
    create_repository_pipeline_known_host,
    create_repository_pipeline_schedule,
    create_repository_pipeline_variable,
    create_repository_runner,
    delete_pipeline_variable_for_workspace,
    delete_repository_pipeline_cache,
    delete_repository_pipeline_caches,
    delete_repository_pipeline_key_pair,
    delete_repository_pipeline_known_host,
    delete_repository_pipeline_schedule,
    delete_repository_pipeline_variable,
    delete_repository_runner,
    get_oidc_configuration,
    get_oidc_keys,
    get_pipeline_container_log,
    get_pipeline_for_repository,
    get_pipeline_step_for_repository,
    get_pipeline_step_log_for_repository,
    get_pipeline_steps_for_repository,
    get_pipeline_test_report_test_case_reasons,
    get_pipeline_test_report_test_cases,
    get_pipeline_test_reports,
    get_pipeline_variable_for_workspace,
    get_pipeline_variables_for_workspace,
    get_pipelines_for_repository,
    get_repository_pipeline_cache_content_uri,
    get_repository_pipeline_caches,
    get_repository_pipeline_config,
    get_repository_pipeline_known_host,
    get_repository_pipeline_known_hosts,
    get_repository_pipeline_schedule,
    get_repository_pipeline_schedule_executions,
    get_repository_pipeline_schedules,
    get_repository_pipeline_ssh_key_pair,
    get_repository_pipeline_variable,
    get_repository_pipeline_variables,
    get_repository_runner,
    get_repository_runners,
    get_workspace_runners,
    stop_pipeline,
    update_pipeline_variable_for_workspace,
    update_repository_build_number,
    update_repository_pipeline_config,
    update_repository_pipeline_key_pair,
    update_repository_pipeline_known_host,
    update_repository_pipeline_schedule,
    update_repository_pipeline_variable,
    update_repository_runner,
)
from bb.cloud.api.pipelines import (
    create_workspace_runner as _create_workspace_runner_api,
)
from bb.cloud.api.pipelines import (
    delete_workspace_runner as _delete_workspace_runner_api,
)
from bb.cloud.api.pipelines import (
    get_workspace_runner as _get_workspace_runner_api,
)
from bb.cloud.api.pipelines import (
    update_workspace_runner as _update_workspace_runner_api,
)
from bb.cloud.models.pipeline import Pipeline
from bb.cloud.models.pipeline_known_host import PipelineKnownHost
from bb.cloud.models.pipeline_schedule import PipelineSchedule
from bb.cloud.models.pipeline_ssh_key_pair import PipelineSshKeyPair
from bb.cloud.models.pipeline_variable import PipelineVariable
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "run",
    "stop",
    "steps",
    "step",
    "step_log",
    "config",
    "update_config",
    "variables",
    "get_variable",
    "create_variable",
    "update_variable",
    "delete_variable",
    "schedules",
    "get_schedule",
    "create_schedule",
    "update_schedule",
    "delete_schedule",
    "known_hosts",
    "get_known_host",
    "create_known_host",
    "update_known_host",
    "delete_known_host",
    "ssh_key_pair",
    "update_ssh_key_pair",
    "delete_ssh_key_pair",
    "caches",
    "delete_cache",
    "oidc_config",
    "oidc_keys",
    "workspace_variables",
    "get_workspace_variable",
    "create_workspace_variable",
    "update_workspace_variable",
    "delete_workspace_variable",
    "runners",
    "get_runner",
    "create_runner",
    "update_runner",
    "delete_runner",
    "workspace_runners",
    "get_workspace_runner",
    "create_workspace_runner",
    "update_workspace_runner",
    "delete_workspace_runner",
    "test_reports",
    "test_cases",
    "test_case_reasons",
    "container_log",
    "cache_uri",
    "clear_caches",
    "schedule_executions",
    "update_build_number",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 10,
) -> list[Pipeline]:
    """Return all pipelines for a repository across all pages.

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
        result = await pipelines.list(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-get>`_
    """
    return [
        p
        async for p in async_paginate(
            get_pipelines_for_repository.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(p, Pipeline)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> Pipeline | None:
    """Return a single pipeline by UUID.

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
        pipeline = await pipelines.get(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-get>`_
    """
    result = await get_pipeline_for_repository.asyncio(workspace, repo_slug, pipeline_uuid, client=client.auth)
    return result if isinstance(result, Pipeline) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def run(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Pipeline,
) -> Pipeline | None:
    """Trigger a new pipeline run and return the created pipeline.

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
        pipeline = await pipelines.run(
            client, workspace="myws", repo_slug="myrepo",
            body=Pipeline(...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-post>`_
    """
    result = await create_pipeline_for_repository.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, Pipeline) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def stop(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> None:
    """Stop a running pipeline.

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
        await pipelines.stop(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}"
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/stopPipeline
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-stoppipeline-post>`_
    """
    await stop_pipeline.asyncio(workspace, repo_slug, pipeline_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def steps(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Return all steps for a pipeline across all pages.

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
        result = await pipelines.steps(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-get>`_
    """
    return [
        s
        async for s in async_paginate(
            get_pipeline_steps_for_repository.asyncio,
            workspace,
            repo_slug,
            pipeline_uuid,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def step(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> Any:
    """Return a single pipeline step by UUID.

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
        s = await pipelines.step(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}", step_uuid="{step-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-get>`_
    """
    result = await get_pipeline_step_for_repository.asyncio(
        workspace, repo_slug, pipeline_uuid, step_uuid, client=client.auth
    )
    return result


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def step_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
) -> str | None:
    """Return the log output for a pipeline step.

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
        log = await pipelines.step_log(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}", step_uuid="{step-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-log-get>`_
    """
    result = await get_pipeline_step_log_for_repository.asyncio(
        workspace, repo_slug, pipeline_uuid, step_uuid, client=client.auth
    )
    return result  # type: ignore[return-value]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the pipeline configuration for a repository.

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
        cfg = await pipelines.config(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-get>`_
    """
    return await get_repository_pipeline_config.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_config(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Unset = UNSET,
) -> Any:
    """Update the pipeline configuration for a repository.

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
        cfg = await pipelines.update_config(
            client, workspace="myws", repo_slug="myrepo", body=...
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-put>`_
    """
    return await update_repository_pipeline_config.asyncio(workspace, repo_slug, client=client.auth, body=body)


# --- Repository pipeline variables ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def variables(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineVariable]:
    """Return all pipeline variables for a repository across all pages.

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
        vars_ = await pipelines.variables(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-get>`_
    """
    return [
        v
        async for v in async_paginate(
            get_repository_pipeline_variables.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(v, PipelineVariable)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_variable(client: BBClient, workspace: str, repo_slug: str, variable_uuid: str) -> PipelineVariable | None:
    """Return a single pipeline variable for a repository by UUID.

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
        var = await pipelines.get_variable(
            client, workspace="myws", repo_slug="myrepo",
            variable_uuid="{var-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-get>`_
    """
    result = await get_repository_pipeline_variable.asyncio(workspace, repo_slug, variable_uuid, client=client.auth)
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | None:
    """Create a pipeline variable for a repository.

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
        var = await pipelines.create_variable(
            client, workspace="myws", repo_slug="myrepo",
            body=PipelineVariable(key="MY_VAR", value="secret", secured=True)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-post>`_
    """
    result = await create_repository_pipeline_variable.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_variable(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    variable_uuid: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | None:
    """Update a pipeline variable for a repository.

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
        var = await pipelines.update_variable(
            client, workspace="myws", repo_slug="myrepo",
            variable_uuid="{var-uuid}",
            body=PipelineVariable(value="new-value")
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-put>`_
    """
    result = await update_repository_pipeline_variable.asyncio(
        workspace, repo_slug, variable_uuid, client=client.auth, body=body
    )
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_variable(client: BBClient, workspace: str, repo_slug: str, variable_uuid: str) -> None:
    """Delete a pipeline variable for a repository.

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
        await pipelines.delete_variable(
            client, workspace="myws", repo_slug="myrepo",
            variable_uuid="{var-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-variables-variable-uuid-delete>`_
    """
    await delete_repository_pipeline_variable.asyncio(workspace, repo_slug, variable_uuid, client=client.auth)


# --- Pipeline schedules ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def schedules(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineSchedule]:
    """Return all pipeline schedules for a repository across all pages.

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
        scheds = await pipelines.schedules(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-get>`_
    """
    return [
        s
        async for s in async_paginate(
            get_repository_pipeline_schedules.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(s, PipelineSchedule)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_schedule(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> PipelineSchedule | None:
    """Return a single pipeline schedule by UUID.

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
        sched = await pipelines.get_schedule(
            client, workspace="myws", repo_slug="myrepo",
            schedule_uuid="{schedule-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-get>`_
    """
    result = await get_repository_pipeline_schedule.asyncio(workspace, repo_slug, schedule_uuid, client=client.auth)
    return result if isinstance(result, PipelineSchedule) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSchedule | Unset = UNSET,
) -> PipelineSchedule | None:
    """Create a pipeline schedule for a repository.

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
        sched = await pipelines.create_schedule(
            client, workspace="myws", repo_slug="myrepo",
            body=PipelineSchedulePostRequestBody(...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-post>`_
    """
    result = await create_repository_pipeline_schedule.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, PipelineSchedule) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_schedule(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    body: PipelineSchedule | Unset = UNSET,
) -> PipelineSchedule | None:
    """Update a pipeline schedule for a repository.

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
        sched = await pipelines.update_schedule(
            client, workspace="myws", repo_slug="myrepo",
            schedule_uuid="{schedule-uuid}", body=...
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-put>`_
    """
    result = await update_repository_pipeline_schedule.asyncio(
        workspace, repo_slug, schedule_uuid, client=client.auth, body=body
    )
    return result if isinstance(result, PipelineSchedule) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_schedule(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> None:
    """Delete a pipeline schedule for a repository.

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
        await pipelines.delete_schedule(
            client, workspace="myws", repo_slug="myrepo",
            schedule_uuid="{schedule-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-delete>`_
    """
    await delete_repository_pipeline_schedule.asyncio(workspace, repo_slug, schedule_uuid, client=client.auth)


# --- Pipeline known hosts ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def known_hosts(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[PipelineKnownHost]:
    """Return all known hosts for the repository's pipeline SSH configuration.

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
        hosts = await pipelines.known_hosts(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-get>`_
    """
    return [
        h
        async for h in async_paginate(
            get_repository_pipeline_known_hosts.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(h, PipelineKnownHost)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_known_host(
    client: BBClient, workspace: str, repo_slug: str, known_host_uuid: str
) -> PipelineKnownHost | None:
    """Return a single known host by UUID.

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
        host = await pipelines.get_known_host(
            client, workspace="myws", repo_slug="myrepo",
            known_host_uuid="{host-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-get>`_
    """
    result = await get_repository_pipeline_known_host.asyncio(workspace, repo_slug, known_host_uuid, client=client.auth)
    return result if isinstance(result, PipelineKnownHost) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineKnownHost | Unset = UNSET,
) -> PipelineKnownHost | None:
    """Add a known host to the repository's pipeline SSH configuration.

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
        host = await pipelines.create_known_host(
            client, workspace="myws", repo_slug="myrepo",
            body=PipelineKnownHost(hostname="github.com", ...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-post>`_
    """
    result = await create_repository_pipeline_known_host.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, PipelineKnownHost) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_known_host(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    known_host_uuid: str,
    *,
    body: PipelineKnownHost | Unset = UNSET,
) -> PipelineKnownHost | None:
    """Update a known host in the repository's pipeline SSH configuration.

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
        host = await pipelines.update_known_host(
            client, workspace="myws", repo_slug="myrepo",
            known_host_uuid="{host-uuid}", body=...
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-put>`_
    """
    result = await update_repository_pipeline_known_host.asyncio(
        workspace, repo_slug, known_host_uuid, client=client.auth, body=body
    )
    return result if isinstance(result, PipelineKnownHost) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_known_host(client: BBClient, workspace: str, repo_slug: str, known_host_uuid: str) -> None:
    """Remove a known host from the repository's pipeline SSH configuration.

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
        await pipelines.delete_known_host(
            client, workspace="myws", repo_slug="myrepo",
            known_host_uuid="{host-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/known_hosts/{known_host_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-known-hosts-known-host-uuid-delete>`_
    """
    await delete_repository_pipeline_known_host.asyncio(workspace, repo_slug, known_host_uuid, client=client.auth)


# --- Pipeline SSH key pair ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def ssh_key_pair(client: BBClient, workspace: str, repo_slug: str) -> PipelineSshKeyPair | None:
    """Return the SSH key pair for the repository's pipeline configuration.

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
        key_pair = await pipelines.ssh_key_pair(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-get>`_
    """
    result = await get_repository_pipeline_ssh_key_pair.asyncio(workspace, repo_slug, client=client.auth)
    return result if isinstance(result, PipelineSshKeyPair) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_ssh_key_pair(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: PipelineSshKeyPair | Unset = UNSET,
) -> PipelineSshKeyPair | None:
    """Create or update the SSH key pair for the repository's pipeline configuration.

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
        key_pair = await pipelines.update_ssh_key_pair(
            client, workspace="myws", repo_slug="myrepo",
            body=PipelineSshKeyPair(private_key="...", public_key="...")
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-put>`_
    """
    result = await update_repository_pipeline_key_pair.asyncio(workspace, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, PipelineSshKeyPair) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_ssh_key_pair(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete the SSH key pair from the repository's pipeline configuration.

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
        await pipelines.delete_ssh_key_pair(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/ssh/key_pair
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-ssh-key-pair-delete>`_
    """
    await delete_repository_pipeline_key_pair.asyncio(workspace, repo_slug, client=client.auth)


# --- Pipeline caches ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def caches(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[Any]:
    """Return all pipeline caches for a repository across all pages.

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
        result = await pipelines.caches(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-get>`_
    """
    return [
        c
        async for c in async_paginate(
            get_repository_pipeline_caches.asyncio,
            workspace,
            repo_slug,
            client=client.auth,
            pagelen=pagelen,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_cache(client: BBClient, workspace: str, repo_slug: str, cache_uuid: str) -> None:
    """Delete a pipeline cache by UUID.

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
        await pipelines.delete_cache(
            client, workspace="myws", repo_slug="myrepo",
            cache_uuid="{cache-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches/{cache_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-cache-uuid-delete>`_
    """
    await delete_repository_pipeline_cache.asyncio(workspace, repo_slug, cache_uuid, client=client.auth)


# --- OIDC ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def oidc_config(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the OIDC configuration for a workspace's pipelines.

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
        oidc = await pipelines.oidc_config(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-identity-oidc-well-known-openid-configuration-get>`_
    """
    return await get_oidc_configuration.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def oidc_keys(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return the OIDC public key set for a workspace's pipelines.

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
        keys = await pipelines.oidc_keys(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/identity/oidc/keys.json
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-identity-oidc-keys-json-get>`_
    """
    return await get_oidc_keys.asyncio(workspace, repo_slug, client=client.auth)


# --- Workspace pipeline variables ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def workspace_variables(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[PipelineVariable]:
    """Return all pipeline variables for a workspace across all pages.

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
        vars_ = await pipelines.workspace_variables(client, workspace="myws")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-get>`_
    """
    return [
        v
        async for v in async_paginate(
            get_pipeline_variables_for_workspace.asyncio,
            workspace,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(v, PipelineVariable)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_workspace_variable(client: BBClient, workspace: str, variable_uuid: str) -> PipelineVariable | None:
    """Return a single workspace pipeline variable by UUID.

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
        var = await pipelines.get_workspace_variable(
            client, workspace="myws", variable_uuid="{var-uuid}"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-get>`_
    """
    result = await get_pipeline_variable_for_workspace.asyncio(workspace, variable_uuid, client=client.auth)
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_workspace_variable(
    client: BBClient,
    workspace: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | None:
    """Create a pipeline variable for a workspace.

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
        var = await pipelines.create_workspace_variable(
            client, workspace="myws",
            body=PipelineVariable(key="MY_VAR", value="secret", secured=True)
        )
        ```

    References:
        `POST /2.0/workspaces/{workspace}/pipelines-config/variables
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-post>`_
    """
    result = await create_pipeline_variable_for_workspace.asyncio(workspace, client=client.auth, body=body)
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_workspace_variable(
    client: BBClient,
    workspace: str,
    variable_uuid: str,
    *,
    body: PipelineVariable | Unset = UNSET,
) -> PipelineVariable | None:
    """Update a workspace pipeline variable.

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
        var = await pipelines.update_workspace_variable(
            client, workspace="myws", variable_uuid="{var-uuid}",
            body=PipelineVariable(value="new-value")
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-put>`_
    """
    result = await update_pipeline_variable_for_workspace.asyncio(
        workspace, variable_uuid, client=client.auth, body=body
    )
    return result if isinstance(result, PipelineVariable) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_workspace_variable(client: BBClient, workspace: str, variable_uuid: str) -> None:
    """Delete a workspace pipeline variable.

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
        await pipelines.delete_workspace_variable(
            client, workspace="myws", variable_uuid="{var-uuid}"
        )
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-variables-variable-uuid-delete>`_
    """
    await delete_pipeline_variable_for_workspace.asyncio(workspace, variable_uuid, client=client.auth)


# --- Repository runners ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def runners(client: BBClient, workspace: str, repo_slug: str) -> Any:
    """Return all self-hosted runners for a repository.

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
        result = await pipelines.runners(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-get>`_
    """
    return await get_repository_runners.asyncio(workspace, repo_slug, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str) -> Any:
    """Return a single repository runner by UUID.

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
        runner = await pipelines.get_runner(
            client, workspace="myws", repo_slug="myrepo",
            runner_uuid="{runner-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-get>`_
    """
    return await get_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_runner(client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET) -> Any:
    """Create a self-hosted runner for a repository.

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
        runner = await pipelines.create_runner(
            client, workspace="myws", repo_slug="myrepo", body=...
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-post>`_
    """
    return await create_repository_runner.asyncio(workspace, repo_slug, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_runner(
    client: BBClient, workspace: str, repo_slug: str, runner_uuid: str, *, body: Unset = UNSET
) -> Any:
    """Update a repository runner.

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
        runner = await pipelines.update_runner(
            client, workspace="myws", repo_slug="myrepo",
            runner_uuid="{runner-uuid}", body=...
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-put>`_
    """
    return await update_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_runner(client: BBClient, workspace: str, repo_slug: str, runner_uuid: str) -> None:
    """Delete a repository runner.

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
        await pipelines.delete_runner(
            client, workspace="myws", repo_slug="myrepo",
            runner_uuid="{runner-uuid}"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-runners-runner-uuid-delete>`_
    """
    await delete_repository_runner.asyncio(workspace, repo_slug, runner_uuid, client=client.auth)


# --- Workspace runners ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def workspace_runners(client: BBClient, workspace: str) -> Any:
    """Return all self-hosted runners for a workspace.

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
        result = await pipelines.workspace_runners(client, workspace="myws")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/runners
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-get>`_
    """
    return await get_workspace_runners.asyncio(workspace, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> Any:
    """Return a single workspace runner by UUID.

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
        runner = await pipelines.get_workspace_runner(
            client, workspace="myws", runner_uuid="{runner-uuid}"
        )
        ```

    References:
        `GET /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-get>`_
    """
    return await _get_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_workspace_runner(client: BBClient, workspace: str, *, body: Unset = UNSET) -> Any:
    """Create a self-hosted runner for a workspace.

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
        runner = await pipelines.create_workspace_runner(
            client, workspace="myws", body=...
        )
        ```

    References:
        `POST /2.0/workspaces/{workspace}/pipelines-config/runners
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-post>`_
    """
    return await _create_workspace_runner_api.asyncio(workspace, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_workspace_runner(client: BBClient, workspace: str, runner_uuid: str, *, body: Unset = UNSET) -> Any:
    """Update a workspace runner.

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
        runner = await pipelines.update_workspace_runner(
            client, workspace="myws", runner_uuid="{runner-uuid}", body=...
        )
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-put>`_
    """
    return await _update_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_workspace_runner(client: BBClient, workspace: str, runner_uuid: str) -> None:
    """Delete a workspace runner.

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
        await pipelines.delete_workspace_runner(
            client, workspace="myws", runner_uuid="{runner-uuid}"
        )
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/pipelines-config/runners/{runner_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-workspaces-workspace-pipelines-config-runners-runner-uuid-delete>`_
    """
    await _delete_workspace_runner_api.asyncio(workspace, runner_uuid, client=client.auth)


# --- Test reports ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def test_reports(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str) -> Any:
    """Return test reports for a pipeline.

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
        reports = await pipelines.test_reports(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-get>`_
    """
    return await get_pipeline_test_reports.asyncio(workspace, repo_slug, pipeline_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def test_cases(client: BBClient, workspace: str, repo_slug: str, pipeline_uuid: str, report_uuid: str) -> Any:
    """Return test cases for a pipeline test report.

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
        cases = await pipelines.test_cases(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}", report_uuid="{step-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports/test-cases
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-test-cases-get>`_
    """
    return await get_pipeline_test_report_test_cases.asyncio(
        workspace, repo_slug, pipeline_uuid, report_uuid, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def test_case_reasons(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    report_uuid: str,
    test_case_uuid: str,
) -> Any:
    """Return failure reasons for a specific test case.

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
        reasons = await pipelines.test_case_reasons(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}", report_uuid="{step-uuid}",
            test_case_uuid="{test-case-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test-reports/test-cases/{test_case_uuid}/test-case-reasons
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-test-reports-test-cases-test-case-uuid-test-case-reasons-get>`_
    """
    return await get_pipeline_test_report_test_case_reasons.asyncio(
        workspace, repo_slug, pipeline_uuid, report_uuid, test_case_uuid, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def container_log(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pipeline_uuid: str,
    step_uuid: str,
    service_name: str,
) -> Any:
    """Return the log for a pipeline container (service) within a step.

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
        log = await pipelines.container_log(
            client, workspace="myws", repo_slug="myrepo",
            pipeline_uuid="{abc-123}", step_uuid="{step-uuid}",
            service_name="docker"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-pipeline-uuid-steps-step-uuid-logs-log-uuid-get>`_
    """
    return await get_pipeline_container_log.asyncio(
        workspace, repo_slug, pipeline_uuid, step_uuid, service_name, client=client.auth
    )


# --- Cache helpers ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def cache_uri(client: BBClient, workspace: str, repo_slug: str, cache_uuid: str) -> Any:
    """Return the download URI for a pipeline cache.

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
        uri = await pipelines.cache_uri(
            client, workspace="myws", repo_slug="myrepo",
            cache_uuid="{cache-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches/{cache_uuid}/content-uri
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-cache-uuid-content-uri-get>`_
    """
    return await get_repository_pipeline_cache_content_uri.asyncio(workspace, repo_slug, cache_uuid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def clear_caches(client: BBClient, workspace: str, repo_slug: str) -> None:
    """Delete all pipeline caches for a repository.

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
        await pipelines.clear_caches(
            client, workspace="myws", repo_slug="myrepo"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/caches
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-caches-delete>`_
    """
    await delete_repository_pipeline_caches.asyncio(workspace, repo_slug, client=client.auth)


# --- Schedule executions ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def schedule_executions(client: BBClient, workspace: str, repo_slug: str, schedule_uuid: str) -> Any:
    """Return the execution history for a pipeline schedule.

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
        history = await pipelines.schedule_executions(
            client, workspace="myws", repo_slug="myrepo",
            schedule_uuid="{schedule-uuid}"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/schedules/{schedule_uuid}/executions
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-schedules-schedule-uuid-executions-get>`_
    """
    return await get_repository_pipeline_schedule_executions.asyncio(
        workspace, repo_slug, schedule_uuid, client=client.auth
    )


# --- Build number ---


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_build_number(client: BBClient, workspace: str, repo_slug: str, *, body: Unset = UNSET) -> Any:
    """Update the next build number for a repository's pipelines.

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
        result = await pipelines.update_build_number(
            client, workspace="myws", repo_slug="myrepo",
            body=PipelineBuildNumber(next=100)
        )
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/pipelines/config/build_number
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pipelines/#api-repositories-workspace-repo-slug-pipelines-config-build-number-put>`_
    """
    return await update_repository_build_number.asyncio(workspace, repo_slug, client=client.auth, body=body)
