# RendezvousApi

All URIs are relative to *https://api.naurt.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rendezvousOptions**](RendezvousApi.md#rendezvousoptions) | **OPTIONS** /rendezvous/v1 | Options |
| [**rendezvousPost**](RendezvousApi.md#rendezvouspost) | **POST** /rendezvous/v1 | Post |



## rendezvousOptions

> OptionsResponse rendezvousOptions()

Options

Returns the current API version and any deprecated versions. 

### Example

```ts
import {
  Configuration,
  RendezvousApi,
} from '@naurt/api';
import type { RendezvousOptionsRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new RendezvousApi(config);

  try {
    const data = await api.rendezvousOptions();
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
| **200** | Endpoint metadata |  * allow - Allowed request methods <br>  * Content-Type - Response content type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## rendezvousPost

> RendezvousResponse rendezvousPost(rendezvousRequest)

Post

Rendezvous takes a list of queries, finds delivery clusters, and returns cluster centres plus the covered addresses for each cluster.  This is not a routing tool. It does not provide delivery order or route optimisation. 

### Example

```ts
import {
  Configuration,
  RendezvousApi,
} from '@naurt/api';
import type { RendezvousPostRequest } from '@naurt/api';

async function example() {
  console.log("🚀 Testing @naurt/api SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: ApiKeyAuth
    apiKey: "YOUR API KEY",
  });
  const api = new RendezvousApi(config);

  const body = {
    // RendezvousRequest
    rendezvousRequest: {"queries":[{"address_string":"18a, Montague Place, Brighton, BN2 1JE, United Kingdom"},{"address_string":"Flat 9, Montague Court, Montague Street, Brighton, BN2 1NQ, United Kingdom"},{"address_string":"28 Hereford Street, Brighton, BN2 1JT, United Kingdom"},{"address_string":"4378twbv5934wy 9q87v3ncyq9nv eriyuib4478twtvwbeihsecfonreniren vt9nhyutrevuhtvnuhitr"},{"address_string":"27 Hereford Street, Brighton, BN2 1JT, United Kingdom"},{"address_string":"28 Essex Street, Brighton, BN2 1JW, United Kingdom"},{"address_string":"Flat 31, Martlet Court, Hereford Street, Brighton, BN2 1LQ, United Kingdom"}]},
  } satisfies RendezvousPostRequest;

  try {
    const data = await api.rendezvousPost(body);
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
| **rendezvousRequest** | [RendezvousRequest](RendezvousRequest.md) |  | |

### Return type

[**RendezvousResponse**](RendezvousResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful clustering response |  -  |
| **400** | Bad request |  -  |
| **401** | Missing or invalid API key |  -  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

