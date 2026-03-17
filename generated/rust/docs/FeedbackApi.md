# \FeedbackApi

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback_options**](FeedbackApi.md#feedback_options) | **OPTIONS** /feedback/v2 | Options
[**feedback_post**](FeedbackApi.md#feedback_post) | **POST** /feedback/v2 | Post



## feedback_options

> models::OptionsResponse feedback_options()
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


## feedback_post

> models::FeedbackResponse feedback_post(feedback_request)
Post

Submit feedback to Naurt for address, parking location, or door location data.  This endpoint can be used to: - suggest corrections to existing Naurt address data - suggest improved parking locations - suggest improved door locations - provide new address records where parking or door data is not yet available  A valid API key is required. Feedback submissions do not count against API usage. 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**feedback_request** | [**FeedbackRequest**](FeedbackRequest.md) |  | [required] |

### Return type

[**models::FeedbackResponse**](feedback-response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

