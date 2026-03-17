# \FinalDestinationApi

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finaldestination_options**](FinalDestinationApi.md#finaldestination_options) | **OPTIONS** /final-destination/v2 | Options
[**finaldestination_post**](FinalDestinationApi.md#finaldestination_post) | **POST** /final-destination/v2 | Post



## finaldestination_options

> models::OptionsResponse finaldestination_options()
Options

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::OptionsResponse**](options-response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## finaldestination_post

> models::FinalDestinationResponse finaldestination_post(final_destination_request)
Post

Query the Naurt Final Destination dataset to retrieve precise destination locations for addresses, buildings, entrances, and parking locations.  Each request contains one or more `queries`. A query can represent several different search types supported by the Final Destination API:  • Forward geocoding — supply an `address_string` or `address_structured`   • Reverse geocoding — supply a `location` with latitude and longitude   • Naurt ID lookup — supply an `id` returned from a previous query   • Source ID lookup — supply identifiers such as `os_uprn`    The API returns a best match for each query along with optional additional matches. Results may include multiple destination geometries such as building entrances, delivery doors, or parking locations depending on available data.  The geometry format returned by the API is controlled by `options.geojson_type`:  • `geojson` (default) — results are returned as standard GeoJSON   FeatureCollections with geometries and properties.  • `key_value` — results are returned as a simplified key/value representation   where each destination type contains latitude and longitude coordinates.  Each query result includes a status, the best match, optional additional matches, and metadata such as distance from the search location when applicable. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**final_destination_request** | [**FinalDestinationRequest**](FinalDestinationRequest.md) |  | [required] |

### Return type

[**models::FinalDestinationResponse**](final-destination-response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

