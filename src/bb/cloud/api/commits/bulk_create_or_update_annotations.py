from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.report_annotation import ReportAnnotation
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
    commit: str,
    report_id: str,
    *,
    body: list[ReportAnnotation],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{report_id}/annotations".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            report_id=quote(str(report_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = list[ReportAnnotation]
type ParseResult = list[ReportAnnotation] | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReportAnnotation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
    commit: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ReportAnnotation],
) -> Response[ParsedPayload]:
    r""" Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (list[ReportAnnotation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ReportAnnotation]]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ReportAnnotation],
) -> ParsedPayload | None:
    r""" Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (list[ReportAnnotation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ReportAnnotation]
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ReportAnnotation],
) -> Response[ParsedPayload]:
    r""" Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (list[ReportAnnotation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ReportAnnotation]]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ReportAnnotation],
) -> ParsedPayload | None:
    r""" Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (list[ReportAnnotation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ReportAnnotation]
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            report_id=report_id,
            client=client,
            body=body,
        )
    ).parsed
