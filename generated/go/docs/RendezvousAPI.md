# \RendezvousAPI

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**RendezvousOptions**](RendezvousAPI.md#RendezvousOptions) | **Options** /rendezvous/v1 | Options
[**RendezvousPost**](RendezvousAPI.md#RendezvousPost) | **Post** /rendezvous/v1 | Post



## RendezvousOptions

> OptionsResponse RendezvousOptions(ctx).Execute()

Options



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Naurt-Ltd/api_specification/generated/go"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RendezvousAPI.RendezvousOptions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RendezvousAPI.RendezvousOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RendezvousOptions`: OptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `RendezvousAPI.RendezvousOptions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiRendezvousOptionsRequest struct via the builder pattern


### Return type

[**OptionsResponse**](OptionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RendezvousPost

> RendezvousResponse RendezvousPost(ctx).RendezvousRequest(rendezvousRequest).Execute()

Post



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Naurt-Ltd/api_specification/generated/go"
)

func main() {
	rendezvousRequest := *openapiclient.NewRendezvousRequest([]openapiclient.RendezvousQuery{*openapiclient.NewRendezvousQuery()}) // RendezvousRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RendezvousAPI.RendezvousPost(context.Background()).RendezvousRequest(rendezvousRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RendezvousAPI.RendezvousPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RendezvousPost`: RendezvousResponse
	fmt.Fprintf(os.Stdout, "Response from `RendezvousAPI.RendezvousPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiRendezvousPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rendezvousRequest** | [**RendezvousRequest**](RendezvousRequest.md) |  | 

### Return type

[**RendezvousResponse**](RendezvousResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

