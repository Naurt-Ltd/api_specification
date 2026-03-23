from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_response import ErrorResponse
from ...models.final_destination_request import FinalDestinationRequest
from ...models.final_destination_response import FinalDestinationResponse
from typing import cast



def _get_kwargs(
    *,
    body: FinalDestinationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/final-destination/v2",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | FinalDestinationResponse | None:
    if response.status_code == 200:
        response_200 = FinalDestinationResponse.from_dict(response.json())



        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = ErrorResponse.from_dict(response.json())



        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = ErrorResponse.from_dict(response.json())



        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorResponse | FinalDestinationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinalDestinationRequest,

) -> Response[ErrorResponse | FinalDestinationResponse]:
    """ Post

     Query the Naurt Final Destination dataset to retrieve precise destination
    locations for addresses, buildings, entrances, and parking locations.

    Each request contains one or more `queries`. A query can represent several
    different search types supported by the Final Destination API:

    • Forward geocoding — supply an `address_string` or `address_structured`
    • Reverse geocoding — supply a `location` with latitude and longitude
    • Naurt ID lookup — supply an `id` returned from a previous query
    • Source ID lookup — supply identifiers such as `os_uprn`

    The API returns a best match for each query along with optional additional
    matches. Results may include multiple destination geometries such as building
    entrances, delivery doors, or parking locations depending on available data.

    The geometry format returned by the API is controlled by `options.geojson_type`:

    • `geojson` (default) — results are returned as standard GeoJSON
      FeatureCollections with geometries and properties.

    • `key_value` — results are returned as a simplified key/value representation
      where each destination type contains latitude and longitude coordinates.

    Each query result includes a status, the best match, optional additional
    matches, and metadata such as distance from the search location when
    applicable.

    Args:
        body (FinalDestinationRequest): A single request to the API, which can contain up to 200
            queries. Each query
            is independent and can be of a different type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FinalDestinationResponse]
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
    body: FinalDestinationRequest,

) -> ErrorResponse | FinalDestinationResponse | None:
    """ Post

     Query the Naurt Final Destination dataset to retrieve precise destination
    locations for addresses, buildings, entrances, and parking locations.

    Each request contains one or more `queries`. A query can represent several
    different search types supported by the Final Destination API:

    • Forward geocoding — supply an `address_string` or `address_structured`
    • Reverse geocoding — supply a `location` with latitude and longitude
    • Naurt ID lookup — supply an `id` returned from a previous query
    • Source ID lookup — supply identifiers such as `os_uprn`

    The API returns a best match for each query along with optional additional
    matches. Results may include multiple destination geometries such as building
    entrances, delivery doors, or parking locations depending on available data.

    The geometry format returned by the API is controlled by `options.geojson_type`:

    • `geojson` (default) — results are returned as standard GeoJSON
      FeatureCollections with geometries and properties.

    • `key_value` — results are returned as a simplified key/value representation
      where each destination type contains latitude and longitude coordinates.

    Each query result includes a status, the best match, optional additional
    matches, and metadata such as distance from the search location when
    applicable.

    Args:
        body (FinalDestinationRequest): A single request to the API, which can contain up to 200
            queries. Each query
            is independent and can be of a different type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FinalDestinationResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FinalDestinationRequest,

) -> Response[ErrorResponse | FinalDestinationResponse]:
    """ Post

     Query the Naurt Final Destination dataset to retrieve precise destination
    locations for addresses, buildings, entrances, and parking locations.

    Each request contains one or more `queries`. A query can represent several
    different search types supported by the Final Destination API:

    • Forward geocoding — supply an `address_string` or `address_structured`
    • Reverse geocoding — supply a `location` with latitude and longitude
    • Naurt ID lookup — supply an `id` returned from a previous query
    • Source ID lookup — supply identifiers such as `os_uprn`

    The API returns a best match for each query along with optional additional
    matches. Results may include multiple destination geometries such as building
    entrances, delivery doors, or parking locations depending on available data.

    The geometry format returned by the API is controlled by `options.geojson_type`:

    • `geojson` (default) — results are returned as standard GeoJSON
      FeatureCollections with geometries and properties.

    • `key_value` — results are returned as a simplified key/value representation
      where each destination type contains latitude and longitude coordinates.

    Each query result includes a status, the best match, optional additional
    matches, and metadata such as distance from the search location when
    applicable.

    Args:
        body (FinalDestinationRequest): A single request to the API, which can contain up to 200
            queries. Each query
            is independent and can be of a different type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | FinalDestinationResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FinalDestinationRequest,

) -> ErrorResponse | FinalDestinationResponse | None:
    """ Post

     Query the Naurt Final Destination dataset to retrieve precise destination
    locations for addresses, buildings, entrances, and parking locations.

    Each request contains one or more `queries`. A query can represent several
    different search types supported by the Final Destination API:

    • Forward geocoding — supply an `address_string` or `address_structured`
    • Reverse geocoding — supply a `location` with latitude and longitude
    • Naurt ID lookup — supply an `id` returned from a previous query
    • Source ID lookup — supply identifiers such as `os_uprn`

    The API returns a best match for each query along with optional additional
    matches. Results may include multiple destination geometries such as building
    entrances, delivery doors, or parking locations depending on available data.

    The geometry format returned by the API is controlled by `options.geojson_type`:

    • `geojson` (default) — results are returned as standard GeoJSON
      FeatureCollections with geometries and properties.

    • `key_value` — results are returned as a simplified key/value representation
      where each destination type contains latitude and longitude coordinates.

    Each query result includes a status, the best match, optional additional
    matches, and metadata such as distance from the search location when
    applicable.

    Args:
        body (FinalDestinationRequest): A single request to the API, which can contain up to 200
            queries. Each query
            is independent and can be of a different type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | FinalDestinationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
