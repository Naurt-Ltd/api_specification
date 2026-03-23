# FeedbackApi

All URIs are relative to *https://api.naurt.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**feedbackOptions**](FeedbackApi.md#feedbackoptions) | **OPTIONS** /feedback/v2 | Options |
| [**feedbackPost**](FeedbackApi.md#feedbackpost) | **POST** /feedback/v2 | Post |



## feedbackOptions

> OptionsResponse feedbackOptions()

Options

### Example

```ts
import {
  Configuration,
  FeedbackApi,
} from '@naurt/api';
import type { FeedbackOptionsRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new FeedbackApi(config);

  try {
    const data = await api.feedbackOptions();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Endpoint metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## feedbackPost

> FeedbackResponse feedbackPost(feedbackRequest)

Post

Submit feedback to Naurt for address, parking location, or door location data.  This endpoint can be used to: - suggest corrections to existing Naurt address data - suggest improved parking locations - suggest improved door locations - provide new address records where parking or door data is not yet available  A valid API key is required. Feedback submissions do not count against API usage. 

### Example

```ts
import {
  Configuration,
  FeedbackApi,
} from '@naurt/api';
import type { FeedbackPostRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new FeedbackApi(config);

  const body = {
    // FeedbackRequest
    feedbackRequest: {"queries":[{"address_string":"Flat A, 49 Upper Tulse Hill, London, SW2 2SQ","door_location":{"latitude":51.448,"longitude":-0.119}}]},
  } satisfies FeedbackPostRequest;

  try {
    const data = await api.feedbackPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **feedbackRequest** | [FeedbackRequest](FeedbackRequest.md) |  | |

### Return type

[**FeedbackResponse**](FeedbackResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feedback accepted successfully |  -  |
| **400** | Bad request |  -  |
| **401** | Missing or invalid API key |  -  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

