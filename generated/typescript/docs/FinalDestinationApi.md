# FinalDestinationApi

All URIs are relative to *https://api.naurt.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**finaldestinationOptions**](FinalDestinationApi.md#finaldestinationoptions) | **OPTIONS** /final-destination/v2 | Options |
| [**finaldestinationPost**](FinalDestinationApi.md#finaldestinationpost) | **POST** /final-destination/v2 | Post |



## finaldestinationOptions

> OptionsResponse finaldestinationOptions()

Options

### Example

```ts
import {
  Configuration,
  FinalDestinationApi,
} from '@naurt/api';
import type { FinaldestinationOptionsRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new FinalDestinationApi(config);

  try {
    const data = await api.finaldestinationOptions();
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


## finaldestinationPost

> FinalDestinationResponse finaldestinationPost(finalDestinationRequest)

Post

Query the Naurt Final Destination dataset to retrieve precise destination locations for addresses, buildings, entrances, and parking locations.  Each request contains one or more &#x60;queries&#x60;. A query can represent several different search types supported by the Final Destination API:  • Forward geocoding — supply an &#x60;address_string&#x60; or &#x60;address_structured&#x60;   • Reverse geocoding — supply a &#x60;location&#x60; with latitude and longitude   • Naurt ID lookup — supply an &#x60;id&#x60; returned from a previous query   • Source ID lookup — supply identifiers such as &#x60;os_uprn&#x60;    The API returns a best match for each query along with optional additional matches. Results may include multiple destination geometries such as building entrances, delivery doors, or parking locations depending on available data.  The geometry format returned by the API is controlled by &#x60;options.geojson_type&#x60;:  • &#x60;geojson&#x60; (default) — results are returned as standard GeoJSON   FeatureCollections with geometries and properties.  • &#x60;key_value&#x60; — results are returned as a simplified key/value representation   where each destination type contains latitude and longitude coordinates.  Each query result includes a status, the best match, optional additional matches, and metadata such as distance from the search location when applicable. 

### Example

```ts
import {
  Configuration,
  FinalDestinationApi,
} from '@naurt/api';
import type { FinaldestinationPostRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new FinalDestinationApi(config);

  const body = {
    // FinalDestinationRequest
    finalDestinationRequest: {"queries":[{"address_string":"32 Thames St, Windsor SL4 1PS","country":"GB"}]},
  } satisfies FinaldestinationPostRequest;

  try {
    const data = await api.finaldestinationPost(body);
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
| **finalDestinationRequest** | [FinalDestinationRequest](FinalDestinationRequest.md) |  | |

### Return type

[**FinalDestinationResponse**](FinalDestinationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful lookup |  -  |
| **4XX** | Bad request or validation errors |  -  |
| **5XX** | Internal server errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

