# \RendezvousApi

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rendezvous_options**](RendezvousApi.md#rendezvous_options) | **OPTIONS** /rendezvous/v1 | Options
[**rendezvous_post**](RendezvousApi.md#rendezvous_post) | **POST** /rendezvous/v1 | Post



## rendezvous_options

> models::OptionsResponse rendezvous_options()
Options

Returns the current API version and any deprecated versions. 

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


## rendezvous_post

> models::RendezvousResponse rendezvous_post(rendezvous_request)
Post

Rendezvous takes a list of queries, finds delivery clusters, and returns cluster centres plus the covered addresses for each cluster.  This is not a routing tool. It does not provide delivery order or route optimisation. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**rendezvous_request** | [**RendezvousRequest**](RendezvousRequest.md) |  | [required] |

### Return type

[**models::RendezvousResponse**](rendezvous-response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

