from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pipeline import Pipeline
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    body: Pipeline,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/pipelines".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Pipeline
type ParseResult = Error | Pipeline | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Pipeline.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Pipeline,
) -> Response[ParsedPayload]:
    r""" Run a pipeline

     Endpoint to create and initiate a pipeline.
    There are a number of different options to initiate a pipeline, where the payload of the request
    will determine which type of pipeline will be instantiated.

    ## Trigger a pipeline for a branch

    One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.
    The specified branch will be used to determine which pipeline definition from the `bitbucket-
    pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of
    the repository and checkout the latest revision of the specified branch.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a pipeline for a commit on a branch or tag

    You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g.
    a branch, tag or bookmark).
    The specified reference will be used to determine which pipeline definition from the bitbucket-
    pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository
    and then do a checkout the specified reference.

    The following reference types are supported:

    * `branch`
    * `named_branch`
    * `bookmark`
     * `tag`

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"type\": \"commit\",
                \"hash\": \"ce5b7431602f7cbba007062eeb55225c6e18e956\"
              },
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\":\"custom\",
                \"pattern\":\"Deploy to production\"
              },
              \"type\":\"pipeline_commit_target\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit on a branch or tag

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit in the context of a specified reference.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition, as well as the reference information. The resulting pipeline will then
    clone the repository a checkout the specified reference.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              },
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\",
              \"ref_type\": \"branch\"
            }
          }'
    ```

    ## Trigger a custom pipeline with variables

    In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file
    as shown in the examples above, you can specify variables that will be available for your build. In
    the request, provide a list of variables, specifying the following for each variable: key, value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_ref_target\",
              \"ref_type\": \"branch\",
              \"ref_name\": \"master\",
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              }
            },
            \"variables\": [
              {
                \"key\": \"var1key\",
                \"value\": \"var1value\",
                \"secured\": true
              },
              {
                \"key\": \"var2key\",
                \"value\": \"var2value\"
              }
            ]
          }'
    ```

    ## Trigger a pull request pipeline

    You can also initiate a pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_pullrequest_target\",
              \"source\": \"pull-request-branch\",
              \"destination\": \"master\",
              \"destination_commit\": {
                \"hash\": \"9f848b7\"
              },
              \"commit\": {
                \"hash\": \"1a372fc\"
              },
              \"pullrequest\": {
                \"id\": \"3\"
              },
              \"selector\": {
                \"type\": \"pull-requests\",
                \"pattern\": \"**\"
              }
            }
          }'
    ```

    # On-demand pipeline

    By default, pipelines run using the YAML in the repository’s `bitbucket-pipelines.yml` configuration
    file.
    With an _on-demand_ pipeline, you include the pipeline’s YAML in the request body. That YAML applies
    only
    to that run and overrides the YAML in `bitbucket-pipelines.yml`.

    Just like with regular pipelines, there is a number of different options to initiate an on-demand
    pipeline.
    However, since the payload contains YAML configuration in this case, _query parameters_ are used to
    supply
    the necessary metadata to determine which type of pipeline will be instantiated. These query
    parameters
    are derived from the JSON equivalent by turning each property into a key-value pair with the JSON
    path
    of the property as the new key.

    ## Trigger on-demand pipeline for a branch

    You can initiate an on-demand pipeline for a specific branch. This branch will be used to determine
    which pipeline definition from the supplied YAML configuration will be applied to initiate the
    pipeline.
    The pipeline will then do a clone of the repository and check out the latest revision of the
    specified branch.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger on-demand pipeline for a commit on a branch or tag

    You can initiate an on-demand pipeline for a specific commit and in the context of a specified
    reference
    (branch or tag). The specified reference will be used to determine which pipeline definition from
    the supplied
    YAML configuration will be applied to initiate the pipeline. The pipeline will clone the repository
    and
    check out the specified reference.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.commit.hash=ce5b7431602f7cbba007
    062eeb55225c6e18e956 \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger a specific on-demand pipeline definition for a commit

    You can trigger a specific pipeline that is defined in the supplied YAML configuration for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_commit_target&target.commit.hash=a3c4e02c9a3755eccdc3764e6ea13facdf30f923&target.selector.type=c
    ustom&target.selector.pattern=security-scan \
          -d '
    pipelines:
      custom:
        security-scan:
          - step:
              script:
                - echo Run on-demand security scan
    ```

    ## Trigger a custom on-demand pipeline with variables

    In addition to triggering a custom on-demand pipeline that is defined in the supplied YAML
    configuration
    as shown in the examples above, you can specify variables that will be available for your build.
    In the request, provide each variable as an indexed set of query parameters representing its key,
    value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.selector.type=custom&target.sele
    ctor.pattern=security-scan&variables[0].key=var1key&variables[0].value=var1value&variables[0].secure
    d=true&variables[1].key=var2key&variables[1].value=var2value \
          -d '
    pipelines:
      custom:
        security-scan:
          - variables:
              - name: var1key
              - name: var2key
          - step:
              script:
                - echo Run on-demand security scan'
    ```

    ## Trigger a pull request pipeline

    You can also initiate an on-demand pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_pullrequest_target&target.source=pull-request-branch&target.destination=destination&target.desti
    nation_commit.hash=9f848b7&target.commit.hash=1a372fc&target.pullrequest.id=3&target.selector.type=p
    ull-requests&target.selector.pattern=** \
          -d '
    pipelines:
      pull-requests:
        \"**\":
          - step:
              script:
                - echo This is an on-demand pipeline'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        body (Pipeline):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pipeline]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Pipeline,
) -> ParsedPayload | None:
    r""" Run a pipeline

     Endpoint to create and initiate a pipeline.
    There are a number of different options to initiate a pipeline, where the payload of the request
    will determine which type of pipeline will be instantiated.

    ## Trigger a pipeline for a branch

    One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.
    The specified branch will be used to determine which pipeline definition from the `bitbucket-
    pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of
    the repository and checkout the latest revision of the specified branch.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a pipeline for a commit on a branch or tag

    You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g.
    a branch, tag or bookmark).
    The specified reference will be used to determine which pipeline definition from the bitbucket-
    pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository
    and then do a checkout the specified reference.

    The following reference types are supported:

    * `branch`
    * `named_branch`
    * `bookmark`
     * `tag`

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"type\": \"commit\",
                \"hash\": \"ce5b7431602f7cbba007062eeb55225c6e18e956\"
              },
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\":\"custom\",
                \"pattern\":\"Deploy to production\"
              },
              \"type\":\"pipeline_commit_target\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit on a branch or tag

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit in the context of a specified reference.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition, as well as the reference information. The resulting pipeline will then
    clone the repository a checkout the specified reference.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              },
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\",
              \"ref_type\": \"branch\"
            }
          }'
    ```

    ## Trigger a custom pipeline with variables

    In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file
    as shown in the examples above, you can specify variables that will be available for your build. In
    the request, provide a list of variables, specifying the following for each variable: key, value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_ref_target\",
              \"ref_type\": \"branch\",
              \"ref_name\": \"master\",
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              }
            },
            \"variables\": [
              {
                \"key\": \"var1key\",
                \"value\": \"var1value\",
                \"secured\": true
              },
              {
                \"key\": \"var2key\",
                \"value\": \"var2value\"
              }
            ]
          }'
    ```

    ## Trigger a pull request pipeline

    You can also initiate a pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_pullrequest_target\",
              \"source\": \"pull-request-branch\",
              \"destination\": \"master\",
              \"destination_commit\": {
                \"hash\": \"9f848b7\"
              },
              \"commit\": {
                \"hash\": \"1a372fc\"
              },
              \"pullrequest\": {
                \"id\": \"3\"
              },
              \"selector\": {
                \"type\": \"pull-requests\",
                \"pattern\": \"**\"
              }
            }
          }'
    ```

    # On-demand pipeline

    By default, pipelines run using the YAML in the repository’s `bitbucket-pipelines.yml` configuration
    file.
    With an _on-demand_ pipeline, you include the pipeline’s YAML in the request body. That YAML applies
    only
    to that run and overrides the YAML in `bitbucket-pipelines.yml`.

    Just like with regular pipelines, there is a number of different options to initiate an on-demand
    pipeline.
    However, since the payload contains YAML configuration in this case, _query parameters_ are used to
    supply
    the necessary metadata to determine which type of pipeline will be instantiated. These query
    parameters
    are derived from the JSON equivalent by turning each property into a key-value pair with the JSON
    path
    of the property as the new key.

    ## Trigger on-demand pipeline for a branch

    You can initiate an on-demand pipeline for a specific branch. This branch will be used to determine
    which pipeline definition from the supplied YAML configuration will be applied to initiate the
    pipeline.
    The pipeline will then do a clone of the repository and check out the latest revision of the
    specified branch.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger on-demand pipeline for a commit on a branch or tag

    You can initiate an on-demand pipeline for a specific commit and in the context of a specified
    reference
    (branch or tag). The specified reference will be used to determine which pipeline definition from
    the supplied
    YAML configuration will be applied to initiate the pipeline. The pipeline will clone the repository
    and
    check out the specified reference.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.commit.hash=ce5b7431602f7cbba007
    062eeb55225c6e18e956 \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger a specific on-demand pipeline definition for a commit

    You can trigger a specific pipeline that is defined in the supplied YAML configuration for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_commit_target&target.commit.hash=a3c4e02c9a3755eccdc3764e6ea13facdf30f923&target.selector.type=c
    ustom&target.selector.pattern=security-scan \
          -d '
    pipelines:
      custom:
        security-scan:
          - step:
              script:
                - echo Run on-demand security scan
    ```

    ## Trigger a custom on-demand pipeline with variables

    In addition to triggering a custom on-demand pipeline that is defined in the supplied YAML
    configuration
    as shown in the examples above, you can specify variables that will be available for your build.
    In the request, provide each variable as an indexed set of query parameters representing its key,
    value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.selector.type=custom&target.sele
    ctor.pattern=security-scan&variables[0].key=var1key&variables[0].value=var1value&variables[0].secure
    d=true&variables[1].key=var2key&variables[1].value=var2value \
          -d '
    pipelines:
      custom:
        security-scan:
          - variables:
              - name: var1key
              - name: var2key
          - step:
              script:
                - echo Run on-demand security scan'
    ```

    ## Trigger a pull request pipeline

    You can also initiate an on-demand pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_pullrequest_target&target.source=pull-request-branch&target.destination=destination&target.desti
    nation_commit.hash=9f848b7&target.commit.hash=1a372fc&target.pullrequest.id=3&target.selector.type=p
    ull-requests&target.selector.pattern=** \
          -d '
    pipelines:
      pull-requests:
        \"**\":
          - step:
              script:
                - echo This is an on-demand pipeline'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        body (Pipeline):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pipeline
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Pipeline,
) -> Response[ParsedPayload]:
    r""" Run a pipeline

     Endpoint to create and initiate a pipeline.
    There are a number of different options to initiate a pipeline, where the payload of the request
    will determine which type of pipeline will be instantiated.

    ## Trigger a pipeline for a branch

    One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.
    The specified branch will be used to determine which pipeline definition from the `bitbucket-
    pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of
    the repository and checkout the latest revision of the specified branch.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a pipeline for a commit on a branch or tag

    You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g.
    a branch, tag or bookmark).
    The specified reference will be used to determine which pipeline definition from the bitbucket-
    pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository
    and then do a checkout the specified reference.

    The following reference types are supported:

    * `branch`
    * `named_branch`
    * `bookmark`
     * `tag`

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"type\": \"commit\",
                \"hash\": \"ce5b7431602f7cbba007062eeb55225c6e18e956\"
              },
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\":\"custom\",
                \"pattern\":\"Deploy to production\"
              },
              \"type\":\"pipeline_commit_target\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit on a branch or tag

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit in the context of a specified reference.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition, as well as the reference information. The resulting pipeline will then
    clone the repository a checkout the specified reference.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              },
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\",
              \"ref_type\": \"branch\"
            }
          }'
    ```

    ## Trigger a custom pipeline with variables

    In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file
    as shown in the examples above, you can specify variables that will be available for your build. In
    the request, provide a list of variables, specifying the following for each variable: key, value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_ref_target\",
              \"ref_type\": \"branch\",
              \"ref_name\": \"master\",
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              }
            },
            \"variables\": [
              {
                \"key\": \"var1key\",
                \"value\": \"var1value\",
                \"secured\": true
              },
              {
                \"key\": \"var2key\",
                \"value\": \"var2value\"
              }
            ]
          }'
    ```

    ## Trigger a pull request pipeline

    You can also initiate a pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_pullrequest_target\",
              \"source\": \"pull-request-branch\",
              \"destination\": \"master\",
              \"destination_commit\": {
                \"hash\": \"9f848b7\"
              },
              \"commit\": {
                \"hash\": \"1a372fc\"
              },
              \"pullrequest\": {
                \"id\": \"3\"
              },
              \"selector\": {
                \"type\": \"pull-requests\",
                \"pattern\": \"**\"
              }
            }
          }'
    ```

    # On-demand pipeline

    By default, pipelines run using the YAML in the repository’s `bitbucket-pipelines.yml` configuration
    file.
    With an _on-demand_ pipeline, you include the pipeline’s YAML in the request body. That YAML applies
    only
    to that run and overrides the YAML in `bitbucket-pipelines.yml`.

    Just like with regular pipelines, there is a number of different options to initiate an on-demand
    pipeline.
    However, since the payload contains YAML configuration in this case, _query parameters_ are used to
    supply
    the necessary metadata to determine which type of pipeline will be instantiated. These query
    parameters
    are derived from the JSON equivalent by turning each property into a key-value pair with the JSON
    path
    of the property as the new key.

    ## Trigger on-demand pipeline for a branch

    You can initiate an on-demand pipeline for a specific branch. This branch will be used to determine
    which pipeline definition from the supplied YAML configuration will be applied to initiate the
    pipeline.
    The pipeline will then do a clone of the repository and check out the latest revision of the
    specified branch.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger on-demand pipeline for a commit on a branch or tag

    You can initiate an on-demand pipeline for a specific commit and in the context of a specified
    reference
    (branch or tag). The specified reference will be used to determine which pipeline definition from
    the supplied
    YAML configuration will be applied to initiate the pipeline. The pipeline will clone the repository
    and
    check out the specified reference.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.commit.hash=ce5b7431602f7cbba007
    062eeb55225c6e18e956 \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger a specific on-demand pipeline definition for a commit

    You can trigger a specific pipeline that is defined in the supplied YAML configuration for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_commit_target&target.commit.hash=a3c4e02c9a3755eccdc3764e6ea13facdf30f923&target.selector.type=c
    ustom&target.selector.pattern=security-scan \
          -d '
    pipelines:
      custom:
        security-scan:
          - step:
              script:
                - echo Run on-demand security scan
    ```

    ## Trigger a custom on-demand pipeline with variables

    In addition to triggering a custom on-demand pipeline that is defined in the supplied YAML
    configuration
    as shown in the examples above, you can specify variables that will be available for your build.
    In the request, provide each variable as an indexed set of query parameters representing its key,
    value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.selector.type=custom&target.sele
    ctor.pattern=security-scan&variables[0].key=var1key&variables[0].value=var1value&variables[0].secure
    d=true&variables[1].key=var2key&variables[1].value=var2value \
          -d '
    pipelines:
      custom:
        security-scan:
          - variables:
              - name: var1key
              - name: var2key
          - step:
              script:
                - echo Run on-demand security scan'
    ```

    ## Trigger a pull request pipeline

    You can also initiate an on-demand pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_pullrequest_target&target.source=pull-request-branch&target.destination=destination&target.desti
    nation_commit.hash=9f848b7&target.commit.hash=1a372fc&target.pullrequest.id=3&target.selector.type=p
    ull-requests&target.selector.pattern=** \
          -d '
    pipelines:
      pull-requests:
        \"**\":
          - step:
              script:
                - echo This is an on-demand pipeline'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        body (Pipeline):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pipeline]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Pipeline,
) -> ParsedPayload | None:
    r""" Run a pipeline

     Endpoint to create and initiate a pipeline.
    There are a number of different options to initiate a pipeline, where the payload of the request
    will determine which type of pipeline will be instantiated.

    ## Trigger a pipeline for a branch

    One way to trigger pipelines is by specifying the branch for which you want to trigger a pipeline.
    The specified branch will be used to determine which pipeline definition from the `bitbucket-
    pipelines.yml` file will be applied to initiate the pipeline. The pipeline will then do a clone of
    the repository and checkout the latest revision of the specified branch.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a pipeline for a commit on a branch or tag

    You can initiate a pipeline for a specific commit and in the context of a specified reference (e.g.
    a branch, tag or bookmark).
    The specified reference will be used to determine which pipeline definition from the bitbucket-
    pipelines.yml file will be applied to initiate the pipeline. The pipeline will clone the repository
    and then do a checkout the specified reference.

    The following reference types are supported:

    * `branch`
    * `named_branch`
    * `bookmark`
     * `tag`

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"type\": \"commit\",
                \"hash\": \"ce5b7431602f7cbba007062eeb55225c6e18e956\"
              },
              \"ref_type\": \"branch\",
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\":\"custom\",
                \"pattern\":\"Deploy to production\"
              },
              \"type\":\"pipeline_commit_target\"
            }
          }'
    ```

    ## Trigger a specific pipeline definition for a commit on a branch or tag

    You can trigger a specific pipeline that is defined in your `bitbucket-pipelines.yml` file for a
    specific commit in the context of a specified reference.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition, as well as the reference information. The resulting pipeline will then
    clone the repository a checkout the specified reference.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"commit\": {
                \"hash\":\"a3c4e02c9a3755eccdc3764e6ea13facdf30f923\",
                \"type\":\"commit\"
              },
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              },
              \"type\": \"pipeline_ref_target\",
              \"ref_name\": \"master\",
              \"ref_type\": \"branch\"
            }
          }'
    ```

    ## Trigger a custom pipeline with variables

    In addition to triggering a custom pipeline that is defined in your `bitbucket-pipelines.yml` file
    as shown in the examples above, you can specify variables that will be available for your build. In
    the request, provide a list of variables, specifying the following for each variable: key, value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_ref_target\",
              \"ref_type\": \"branch\",
              \"ref_name\": \"master\",
              \"selector\": {
                \"type\": \"custom\",
                \"pattern\": \"Deploy to production\"
              }
            },
            \"variables\": [
              {
                \"key\": \"var1key\",
                \"value\": \"var1value\",
                \"secured\": true
              },
              {
                \"key\": \"var2key\",
                \"value\": \"var2value\"
              }
            ]
          }'
    ```

    ## Trigger a pull request pipeline

    You can also initiate a pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/json' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines/ \
          -d '
          {
            \"target\": {
              \"type\": \"pipeline_pullrequest_target\",
              \"source\": \"pull-request-branch\",
              \"destination\": \"master\",
              \"destination_commit\": {
                \"hash\": \"9f848b7\"
              },
              \"commit\": {
                \"hash\": \"1a372fc\"
              },
              \"pullrequest\": {
                \"id\": \"3\"
              },
              \"selector\": {
                \"type\": \"pull-requests\",
                \"pattern\": \"**\"
              }
            }
          }'
    ```

    # On-demand pipeline

    By default, pipelines run using the YAML in the repository’s `bitbucket-pipelines.yml` configuration
    file.
    With an _on-demand_ pipeline, you include the pipeline’s YAML in the request body. That YAML applies
    only
    to that run and overrides the YAML in `bitbucket-pipelines.yml`.

    Just like with regular pipelines, there is a number of different options to initiate an on-demand
    pipeline.
    However, since the payload contains YAML configuration in this case, _query parameters_ are used to
    supply
    the necessary metadata to determine which type of pipeline will be instantiated. These query
    parameters
    are derived from the JSON equivalent by turning each property into a key-value pair with the JSON
    path
    of the property as the new key.

    ## Trigger on-demand pipeline for a branch

    You can initiate an on-demand pipeline for a specific branch. This branch will be used to determine
    which pipeline definition from the supplied YAML configuration will be applied to initiate the
    pipeline.
    The pipeline will then do a clone of the repository and check out the latest revision of the
    specified branch.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger on-demand pipeline for a commit on a branch or tag

    You can initiate an on-demand pipeline for a specific commit and in the context of a specified
    reference
    (branch or tag). The specified reference will be used to determine which pipeline definition from
    the supplied
    YAML configuration will be applied to initiate the pipeline. The pipeline will clone the repository
    and
    check out the specified reference.

    To trigger an on-demand pipeline for a _branch_ the requesting user must have **write permission**
    for
    that branch (which can be limited by [branch restrictions](https://support.atlassian.com/bitbucket-
    cloud/docs/use-branch-permissions/)).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.commit.hash=ce5b7431602f7cbba007
    062eeb55225c6e18e956 \
          -d '
    pipelines:
      default:
        - step:
            script:
              - echo This is an on-demand pipeline'
    ```

    ## Trigger a specific on-demand pipeline definition for a commit

    You can trigger a specific pipeline that is defined in the supplied YAML configuration for a
    specific commit.
    In addition to the commit revision, you specify the type and pattern of the selector that identifies
    the pipeline definition. The resulting pipeline will then clone the repository and checkout the
    specified revision.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_commit_target&target.commit.hash=a3c4e02c9a3755eccdc3764e6ea13facdf30f923&target.selector.type=c
    ustom&target.selector.pattern=security-scan \
          -d '
    pipelines:
      custom:
        security-scan:
          - step:
              script:
                - echo Run on-demand security scan
    ```

    ## Trigger a custom on-demand pipeline with variables

    In addition to triggering a custom on-demand pipeline that is defined in the supplied YAML
    configuration
    as shown in the examples above, you can specify variables that will be available for your build.
    In the request, provide each variable as an indexed set of query parameters representing its key,
    value,
    and whether it should be secured or not (this field is optional and defaults to not secured).

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_ref_target&target.ref_type=branch&target.ref_name=master&target.selector.type=custom&target.sele
    ctor.pattern=security-scan&variables[0].key=var1key&variables[0].value=var1value&variables[0].secure
    d=true&variables[1].key=var2key&variables[1].value=var2value \
          -d '
    pipelines:
      custom:
        security-scan:
          - variables:
              - name: var1key
              - name: var2key
          - step:
              script:
                - echo Run on-demand security scan'
    ```

    ## Trigger a pull request pipeline

    You can also initiate an on-demand pipeline for a specific pull request.

    ### Example

    ```
    $ curl -X POST -is -u '{atlassian_account_email}:{api_token}' \
          -H 'Content-Type: application/yaml' \
          https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pipelines?target.type=pipel
    ine_pullrequest_target&target.source=pull-request-branch&target.destination=destination&target.desti
    nation_commit.hash=9f848b7&target.commit.hash=1a372fc&target.pullrequest.id=3&target.selector.type=p
    ull-requests&target.selector.pattern=** \
          -d '
    pipelines:
      pull-requests:
        \"**\":
          - step:
              script:
                - echo This is an on-demand pipeline'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        body (Pipeline):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pipeline
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
