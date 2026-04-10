from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_insight_report import RestInsightReport
from ...models.rest_set_insight_report_request import RestSetInsightReportRequest
from ...models.set_a_code_insights_report_response_400 import SetACodeInsightsReportResponse400
from ...models.set_a_code_insights_report_response_401 import SetACodeInsightsReportResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    body: RestSetInsightReportRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/reports/{key}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401 | None:
    if response.status_code == 200:
        response_200 = RestInsightReport.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetACodeInsightsReportResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetACodeInsightsReportResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSetInsightReportRequest | Unset = UNSET,
) -> Response[RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401]:
    r"""Create a Code Insights report

     Create a new insight report, or replace the existing one if a report already exists for the given
    repository, commit, and report key. A request to replace an existing report will be rejected if the
    authenticated user was not the creator of the specified report.

    The report key should be a unique string chosen by the reporter and should be unique enough not to
    potentially clash with report keys from other reporters. We recommend using reverse DNS namespacing
    or a similar standard to ensure that collision is avoided.<h1>Report parameters</h1><table
    summary=\"Report parameters\">    <tr>        <th>Parameter</th>        <th>Description</th>
    <th>Required?</th>        <th>Restrictions</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A short string representing the name of the report</td>
    <td>Yes</td>        <td>Max length: 450 characters (but we recommend that it is shorter so that the
    display is nicer)</td>        <td>String</td>    </tr>    <tr>        <td>details</td>        <td>
    A string to describe the purpose of the report. This string may contain             escaped newlines
    and if it does it will display the content accordingly.        </td>        <td>No</td>
    <td>Max length: 2000 characters</td>        <td>String</td>    </tr>    <tr>        <td>result</td>
    <td>Indicates whether the report is in a passed or failed state</td>        <td>No</td>
    <td>One of: PASS, FAIL</td>        <td>String</td>    </tr>    <tr>        <td>data</td>
    <td>An array of data fields (described below) to display information on the report</td>
    <td>No</td>        <td>Maximum 6 data fields</td>        <td>Array</td>    </tr>    <tr>
    <td>reporter</td>        <td>A string to describe the tool or company who created the report</td>
    <td>No</td>        <td>Max length: 450 characters</td>        <td>String</td>    </tr>    <tr>
    <td>link</td>        <td>A URL linking to the results of the report in an external tool.</td>
    <td>No</td>        <td>Must be a valid http or https URL</td>        <td>String</td>    </tr>
    <tr>        <td>logoUrl</td>        <td>A URL to the report logo. If none is provided, the default
    insights logo will be used.</td>        <td>No</td>        <td>Must be a valid http or https
    URL</td>        <td>String</td>    </tr></table><h1>Data parameters</h1>The data field on the report
    is an array with at most 6 data fields (JSON maps) containing information that is to be displayed on
    the report (see the request example).<table summary=\"Data parameters\">    <tr>
    <th>Parameter</th>        <th>Description</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A string describing what this data field represents</td>
    <td>String</td>    </tr>    <tr>        <td>type</td>        <td>             The type of data
    contained in the value field. If not provided,             then the value will be detected as a
    boolean, number or string.             One of: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE,
    TEXT        </td>        <td>String</td>    </tr>    <tr>        <td>value</td>        <td>
    A value based on the type provided. Either a raw value             (string, number or boolean) or a
    map. See below.        </td>    </tr></table><table summary=\"Types\">    <tr>        <th>Type
    Field</th>        <th>Value Field Type</th>        <th>Value Field Display</th>    </tr>    <tr>
    <td>None/Omitted</td>        <td>Number, String or Boolean (not an array or object)</td>
    <td>Plain text</td>    </tr>    <tr>        <td>BOOLEAN</td>        <td>Boolean</td>        <td>The
    value will be read as a JSON boolean and displayed as 'Yes' or 'No'.</td>    </tr>    <tr>
    <td>DATE</td>        <td>Number</td>        <td>             The value will be read as a JSON number
    in the form of a Unix timestamp              (milliseconds) and will be displayed as a relative date
    if the date is less             than one week ago, otherwise it will be displayed as an absolute
    date.        </td>    </tr>    <tr>        <td>DURATION</td>        <td>Number</td>        <td>
    The value will be read as a JSON number in milliseconds and             will be displayed in a human
    readable duration format.        </td>    </tr>    <tr>        <td>LINK</td>        <td>Object:
    {\"linktext\": \"Link text here\", \"href\": \"https://link.to.annotation/in/external/tool\"}</td>
    <td>             The value will be read as a JSON object containing the fields \"linktext\"
    and \"href\" and will be displayed as a clickable link on the report.        </td>    </tr>    <tr>
    <td>NUMBER</td>        <td>Number</td>        <td>             The value will be read as a JSON
    number and large numbers will             be displayed in a human readable format (e.g. 14.3k).
    </td>    </tr>    <tr>        <td>PERCENTAGE</td>        <td>Number (between 0 and 100)</td>
    <td>             The value will be read as a JSON number between 0 and 100              and will be
    displayed with a percentage sign.        </td>    </tr>    <tr>        <td>TEXT</td>
    <td>String</td>        <td>The value will be read as a JSON string and will be displayed as-is</td>
    </tr></table>

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestSetInsightReportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSetInsightReportRequest | Unset = UNSET,
) -> RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401 | None:
    r"""Create a Code Insights report

     Create a new insight report, or replace the existing one if a report already exists for the given
    repository, commit, and report key. A request to replace an existing report will be rejected if the
    authenticated user was not the creator of the specified report.

    The report key should be a unique string chosen by the reporter and should be unique enough not to
    potentially clash with report keys from other reporters. We recommend using reverse DNS namespacing
    or a similar standard to ensure that collision is avoided.<h1>Report parameters</h1><table
    summary=\"Report parameters\">    <tr>        <th>Parameter</th>        <th>Description</th>
    <th>Required?</th>        <th>Restrictions</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A short string representing the name of the report</td>
    <td>Yes</td>        <td>Max length: 450 characters (but we recommend that it is shorter so that the
    display is nicer)</td>        <td>String</td>    </tr>    <tr>        <td>details</td>        <td>
    A string to describe the purpose of the report. This string may contain             escaped newlines
    and if it does it will display the content accordingly.        </td>        <td>No</td>
    <td>Max length: 2000 characters</td>        <td>String</td>    </tr>    <tr>        <td>result</td>
    <td>Indicates whether the report is in a passed or failed state</td>        <td>No</td>
    <td>One of: PASS, FAIL</td>        <td>String</td>    </tr>    <tr>        <td>data</td>
    <td>An array of data fields (described below) to display information on the report</td>
    <td>No</td>        <td>Maximum 6 data fields</td>        <td>Array</td>    </tr>    <tr>
    <td>reporter</td>        <td>A string to describe the tool or company who created the report</td>
    <td>No</td>        <td>Max length: 450 characters</td>        <td>String</td>    </tr>    <tr>
    <td>link</td>        <td>A URL linking to the results of the report in an external tool.</td>
    <td>No</td>        <td>Must be a valid http or https URL</td>        <td>String</td>    </tr>
    <tr>        <td>logoUrl</td>        <td>A URL to the report logo. If none is provided, the default
    insights logo will be used.</td>        <td>No</td>        <td>Must be a valid http or https
    URL</td>        <td>String</td>    </tr></table><h1>Data parameters</h1>The data field on the report
    is an array with at most 6 data fields (JSON maps) containing information that is to be displayed on
    the report (see the request example).<table summary=\"Data parameters\">    <tr>
    <th>Parameter</th>        <th>Description</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A string describing what this data field represents</td>
    <td>String</td>    </tr>    <tr>        <td>type</td>        <td>             The type of data
    contained in the value field. If not provided,             then the value will be detected as a
    boolean, number or string.             One of: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE,
    TEXT        </td>        <td>String</td>    </tr>    <tr>        <td>value</td>        <td>
    A value based on the type provided. Either a raw value             (string, number or boolean) or a
    map. See below.        </td>    </tr></table><table summary=\"Types\">    <tr>        <th>Type
    Field</th>        <th>Value Field Type</th>        <th>Value Field Display</th>    </tr>    <tr>
    <td>None/Omitted</td>        <td>Number, String or Boolean (not an array or object)</td>
    <td>Plain text</td>    </tr>    <tr>        <td>BOOLEAN</td>        <td>Boolean</td>        <td>The
    value will be read as a JSON boolean and displayed as 'Yes' or 'No'.</td>    </tr>    <tr>
    <td>DATE</td>        <td>Number</td>        <td>             The value will be read as a JSON number
    in the form of a Unix timestamp              (milliseconds) and will be displayed as a relative date
    if the date is less             than one week ago, otherwise it will be displayed as an absolute
    date.        </td>    </tr>    <tr>        <td>DURATION</td>        <td>Number</td>        <td>
    The value will be read as a JSON number in milliseconds and             will be displayed in a human
    readable duration format.        </td>    </tr>    <tr>        <td>LINK</td>        <td>Object:
    {\"linktext\": \"Link text here\", \"href\": \"https://link.to.annotation/in/external/tool\"}</td>
    <td>             The value will be read as a JSON object containing the fields \"linktext\"
    and \"href\" and will be displayed as a clickable link on the report.        </td>    </tr>    <tr>
    <td>NUMBER</td>        <td>Number</td>        <td>             The value will be read as a JSON
    number and large numbers will             be displayed in a human readable format (e.g. 14.3k).
    </td>    </tr>    <tr>        <td>PERCENTAGE</td>        <td>Number (between 0 and 100)</td>
    <td>             The value will be read as a JSON number between 0 and 100              and will be
    displayed with a percentage sign.        </td>    </tr>    <tr>        <td>TEXT</td>
    <td>String</td>        <td>The value will be read as a JSON string and will be displayed as-is</td>
    </tr></table>

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestSetInsightReportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSetInsightReportRequest | Unset = UNSET,
) -> Response[RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401]:
    r"""Create a Code Insights report

     Create a new insight report, or replace the existing one if a report already exists for the given
    repository, commit, and report key. A request to replace an existing report will be rejected if the
    authenticated user was not the creator of the specified report.

    The report key should be a unique string chosen by the reporter and should be unique enough not to
    potentially clash with report keys from other reporters. We recommend using reverse DNS namespacing
    or a similar standard to ensure that collision is avoided.<h1>Report parameters</h1><table
    summary=\"Report parameters\">    <tr>        <th>Parameter</th>        <th>Description</th>
    <th>Required?</th>        <th>Restrictions</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A short string representing the name of the report</td>
    <td>Yes</td>        <td>Max length: 450 characters (but we recommend that it is shorter so that the
    display is nicer)</td>        <td>String</td>    </tr>    <tr>        <td>details</td>        <td>
    A string to describe the purpose of the report. This string may contain             escaped newlines
    and if it does it will display the content accordingly.        </td>        <td>No</td>
    <td>Max length: 2000 characters</td>        <td>String</td>    </tr>    <tr>        <td>result</td>
    <td>Indicates whether the report is in a passed or failed state</td>        <td>No</td>
    <td>One of: PASS, FAIL</td>        <td>String</td>    </tr>    <tr>        <td>data</td>
    <td>An array of data fields (described below) to display information on the report</td>
    <td>No</td>        <td>Maximum 6 data fields</td>        <td>Array</td>    </tr>    <tr>
    <td>reporter</td>        <td>A string to describe the tool or company who created the report</td>
    <td>No</td>        <td>Max length: 450 characters</td>        <td>String</td>    </tr>    <tr>
    <td>link</td>        <td>A URL linking to the results of the report in an external tool.</td>
    <td>No</td>        <td>Must be a valid http or https URL</td>        <td>String</td>    </tr>
    <tr>        <td>logoUrl</td>        <td>A URL to the report logo. If none is provided, the default
    insights logo will be used.</td>        <td>No</td>        <td>Must be a valid http or https
    URL</td>        <td>String</td>    </tr></table><h1>Data parameters</h1>The data field on the report
    is an array with at most 6 data fields (JSON maps) containing information that is to be displayed on
    the report (see the request example).<table summary=\"Data parameters\">    <tr>
    <th>Parameter</th>        <th>Description</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A string describing what this data field represents</td>
    <td>String</td>    </tr>    <tr>        <td>type</td>        <td>             The type of data
    contained in the value field. If not provided,             then the value will be detected as a
    boolean, number or string.             One of: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE,
    TEXT        </td>        <td>String</td>    </tr>    <tr>        <td>value</td>        <td>
    A value based on the type provided. Either a raw value             (string, number or boolean) or a
    map. See below.        </td>    </tr></table><table summary=\"Types\">    <tr>        <th>Type
    Field</th>        <th>Value Field Type</th>        <th>Value Field Display</th>    </tr>    <tr>
    <td>None/Omitted</td>        <td>Number, String or Boolean (not an array or object)</td>
    <td>Plain text</td>    </tr>    <tr>        <td>BOOLEAN</td>        <td>Boolean</td>        <td>The
    value will be read as a JSON boolean and displayed as 'Yes' or 'No'.</td>    </tr>    <tr>
    <td>DATE</td>        <td>Number</td>        <td>             The value will be read as a JSON number
    in the form of a Unix timestamp              (milliseconds) and will be displayed as a relative date
    if the date is less             than one week ago, otherwise it will be displayed as an absolute
    date.        </td>    </tr>    <tr>        <td>DURATION</td>        <td>Number</td>        <td>
    The value will be read as a JSON number in milliseconds and             will be displayed in a human
    readable duration format.        </td>    </tr>    <tr>        <td>LINK</td>        <td>Object:
    {\"linktext\": \"Link text here\", \"href\": \"https://link.to.annotation/in/external/tool\"}</td>
    <td>             The value will be read as a JSON object containing the fields \"linktext\"
    and \"href\" and will be displayed as a clickable link on the report.        </td>    </tr>    <tr>
    <td>NUMBER</td>        <td>Number</td>        <td>             The value will be read as a JSON
    number and large numbers will             be displayed in a human readable format (e.g. 14.3k).
    </td>    </tr>    <tr>        <td>PERCENTAGE</td>        <td>Number (between 0 and 100)</td>
    <td>             The value will be read as a JSON number between 0 and 100              and will be
    displayed with a percentage sign.        </td>    </tr>    <tr>        <td>TEXT</td>
    <td>String</td>        <td>The value will be read as a JSON string and will be displayed as-is</td>
    </tr></table>

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestSetInsightReportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSetInsightReportRequest | Unset = UNSET,
) -> RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401 | None:
    r"""Create a Code Insights report

     Create a new insight report, or replace the existing one if a report already exists for the given
    repository, commit, and report key. A request to replace an existing report will be rejected if the
    authenticated user was not the creator of the specified report.

    The report key should be a unique string chosen by the reporter and should be unique enough not to
    potentially clash with report keys from other reporters. We recommend using reverse DNS namespacing
    or a similar standard to ensure that collision is avoided.<h1>Report parameters</h1><table
    summary=\"Report parameters\">    <tr>        <th>Parameter</th>        <th>Description</th>
    <th>Required?</th>        <th>Restrictions</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A short string representing the name of the report</td>
    <td>Yes</td>        <td>Max length: 450 characters (but we recommend that it is shorter so that the
    display is nicer)</td>        <td>String</td>    </tr>    <tr>        <td>details</td>        <td>
    A string to describe the purpose of the report. This string may contain             escaped newlines
    and if it does it will display the content accordingly.        </td>        <td>No</td>
    <td>Max length: 2000 characters</td>        <td>String</td>    </tr>    <tr>        <td>result</td>
    <td>Indicates whether the report is in a passed or failed state</td>        <td>No</td>
    <td>One of: PASS, FAIL</td>        <td>String</td>    </tr>    <tr>        <td>data</td>
    <td>An array of data fields (described below) to display information on the report</td>
    <td>No</td>        <td>Maximum 6 data fields</td>        <td>Array</td>    </tr>    <tr>
    <td>reporter</td>        <td>A string to describe the tool or company who created the report</td>
    <td>No</td>        <td>Max length: 450 characters</td>        <td>String</td>    </tr>    <tr>
    <td>link</td>        <td>A URL linking to the results of the report in an external tool.</td>
    <td>No</td>        <td>Must be a valid http or https URL</td>        <td>String</td>    </tr>
    <tr>        <td>logoUrl</td>        <td>A URL to the report logo. If none is provided, the default
    insights logo will be used.</td>        <td>No</td>        <td>Must be a valid http or https
    URL</td>        <td>String</td>    </tr></table><h1>Data parameters</h1>The data field on the report
    is an array with at most 6 data fields (JSON maps) containing information that is to be displayed on
    the report (see the request example).<table summary=\"Data parameters\">    <tr>
    <th>Parameter</th>        <th>Description</th>        <th>Type</th>    </tr>    <tr>
    <td>title</td>        <td>A string describing what this data field represents</td>
    <td>String</td>    </tr>    <tr>        <td>type</td>        <td>             The type of data
    contained in the value field. If not provided,             then the value will be detected as a
    boolean, number or string.             One of: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE,
    TEXT        </td>        <td>String</td>    </tr>    <tr>        <td>value</td>        <td>
    A value based on the type provided. Either a raw value             (string, number or boolean) or a
    map. See below.        </td>    </tr></table><table summary=\"Types\">    <tr>        <th>Type
    Field</th>        <th>Value Field Type</th>        <th>Value Field Display</th>    </tr>    <tr>
    <td>None/Omitted</td>        <td>Number, String or Boolean (not an array or object)</td>
    <td>Plain text</td>    </tr>    <tr>        <td>BOOLEAN</td>        <td>Boolean</td>        <td>The
    value will be read as a JSON boolean and displayed as 'Yes' or 'No'.</td>    </tr>    <tr>
    <td>DATE</td>        <td>Number</td>        <td>             The value will be read as a JSON number
    in the form of a Unix timestamp              (milliseconds) and will be displayed as a relative date
    if the date is less             than one week ago, otherwise it will be displayed as an absolute
    date.        </td>    </tr>    <tr>        <td>DURATION</td>        <td>Number</td>        <td>
    The value will be read as a JSON number in milliseconds and             will be displayed in a human
    readable duration format.        </td>    </tr>    <tr>        <td>LINK</td>        <td>Object:
    {\"linktext\": \"Link text here\", \"href\": \"https://link.to.annotation/in/external/tool\"}</td>
    <td>             The value will be read as a JSON object containing the fields \"linktext\"
    and \"href\" and will be displayed as a clickable link on the report.        </td>    </tr>    <tr>
    <td>NUMBER</td>        <td>Number</td>        <td>             The value will be read as a JSON
    number and large numbers will             be displayed in a human readable format (e.g. 14.3k).
    </td>    </tr>    <tr>        <td>PERCENTAGE</td>        <td>Number (between 0 and 100)</td>
    <td>             The value will be read as a JSON number between 0 and 100              and will be
    displayed with a percentage sign.        </td>    </tr>    <tr>        <td>TEXT</td>
    <td>String</td>        <td>The value will be read as a JSON string and will be displayed as-is</td>
    </tr></table>

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestSetInsightReportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestInsightReport | SetACodeInsightsReportResponse400 | SetACodeInsightsReportResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            key=key,
            client=client,
            body=body,
        )
    ).parsed
