from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.report import Report
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
    body: Report,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{report_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            report_id=quote(str(report_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Report
type ParseResult = Error | Report | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Report.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

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
    body: Report,
) -> Response[ParsedPayload]:
    r""" Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (Report):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Report]
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
    body: Report,
) -> ParsedPayload | None:
    r""" Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (Report):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Report
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
    body: Report,
) -> Response[ParsedPayload]:
    r""" Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (Report):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Report]
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
    body: Report,
) -> ParsedPayload | None:
    r""" Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        body (Report):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Report
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
