from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_certificate_response_400 import CreateCertificateResponse400
from ...models.create_certificate_response_401 import CreateCertificateResponse401
from ...models.example_certificate_multipart_form_data import ExampleCertificateMultipartFormData
from ...models.rest_x509_certificate import RestX509Certificate
from ...types import Response


def _get_kwargs(
    *,
    body: ExampleCertificateMultipartFormData,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/signing/x509-certificates",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate | None:
    if response.status_code == 201:
        response_201 = RestX509Certificate.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateCertificateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateCertificateResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExampleCertificateMultipartFormData,
) -> Response[CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate]:
    """Create an X.509 certificate

     Create an X.509 certificate. This will add the given X.509 certificate to the system. Existing
    entries will not be overridden if an X.509 certificate already exists. Once added, an X.509
    certificate cannot be updated.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (ExampleCertificateMultipartFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExampleCertificateMultipartFormData,
) -> CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate | None:
    """Create an X.509 certificate

     Create an X.509 certificate. This will add the given X.509 certificate to the system. Existing
    entries will not be overridden if an X.509 certificate already exists. Once added, an X.509
    certificate cannot be updated.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (ExampleCertificateMultipartFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExampleCertificateMultipartFormData,
) -> Response[CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate]:
    """Create an X.509 certificate

     Create an X.509 certificate. This will add the given X.509 certificate to the system. Existing
    entries will not be overridden if an X.509 certificate already exists. Once added, an X.509
    certificate cannot be updated.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (ExampleCertificateMultipartFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExampleCertificateMultipartFormData,
) -> CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate | None:
    """Create an X.509 certificate

     Create an X.509 certificate. This will add the given X.509 certificate to the system. Existing
    entries will not be overridden if an X.509 certificate already exists. Once added, an X.509
    certificate cannot be updated.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource.

    Args:
        body (ExampleCertificateMultipartFormData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCertificateResponse400 | CreateCertificateResponse401 | RestX509Certificate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
