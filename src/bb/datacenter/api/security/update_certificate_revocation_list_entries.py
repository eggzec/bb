from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_certificate_revocation_list_entries_response_401 import (
    UpdateCertificateRevocationListEntriesResponse401,
)
from ...models.update_certificate_revocation_list_entries_response_404 import (
    UpdateCertificateRevocationListEntriesResponse404,
)
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/signing/x509-certificates/crl/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = UpdateCertificateRevocationListEntriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateCertificateRevocationListEntriesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404
]:
    """Update X.509 CRL entries

     Update the certificate revocation list (CRL) entries for an issuer X.509 certificate in the system,
    identified by <code>id</code>. This will add any new revoked X.509 certificates that were issued by
    the given issuer X.509 certificate.

    This endpoint will schedule a request to asynchronously perform the task. Please allow time for the
    task to complete as it will vary depending on how many CRLs there are to retrieve and process.

    Note: CRL updates are scheduled to run every 24 hours. You may wish to trigger a refresh manually
    using this endpoint, otherwise, entries will be updated daily.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404 | None:
    """Update X.509 CRL entries

     Update the certificate revocation list (CRL) entries for an issuer X.509 certificate in the system,
    identified by <code>id</code>. This will add any new revoked X.509 certificates that were issued by
    the given issuer X.509 certificate.

    This endpoint will schedule a request to asynchronously perform the task. Please allow time for the
    task to complete as it will vary depending on how many CRLs there are to retrieve and process.

    Note: CRL updates are scheduled to run every 24 hours. You may wish to trigger a refresh manually
    using this endpoint, otherwise, entries will be updated daily.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404
]:
    """Update X.509 CRL entries

     Update the certificate revocation list (CRL) entries for an issuer X.509 certificate in the system,
    identified by <code>id</code>. This will add any new revoked X.509 certificates that were issued by
    the given issuer X.509 certificate.

    This endpoint will schedule a request to asynchronously perform the task. Please allow time for the
    task to complete as it will vary depending on how many CRLs there are to retrieve and process.

    Note: CRL updates are scheduled to run every 24 hours. You may wish to trigger a refresh manually
    using this endpoint, otherwise, entries will be updated daily.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404 | None:
    """Update X.509 CRL entries

     Update the certificate revocation list (CRL) entries for an issuer X.509 certificate in the system,
    identified by <code>id</code>. This will add any new revoked X.509 certificates that were issued by
    the given issuer X.509 certificate.

    This endpoint will schedule a request to asynchronously perform the task. Please allow time for the
    task to complete as it will vary depending on how many CRLs there are to retrieve and process.

    Note: CRL updates are scheduled to run every 24 hours. You may wish to trigger a refresh manually
    using this endpoint, otherwise, entries will be updated daily.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UpdateCertificateRevocationListEntriesResponse401 | UpdateCertificateRevocationListEntriesResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
