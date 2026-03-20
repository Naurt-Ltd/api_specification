# \FinalDestinationAPI

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**FinaldestinationOptions**](FinalDestinationAPI.md#FinaldestinationOptions) | **Options** /final-destination/v2 | Options
[**FinaldestinationPost**](FinalDestinationAPI.md#FinaldestinationPost) | **Post** /final-destination/v2 | Post



## FinaldestinationOptions

> OptionsResponse FinaldestinationOptions(ctx).Execute()

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
	resp, r, err := apiClient.FinalDestinationAPI.FinaldestinationOptions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FinalDestinationAPI.FinaldestinationOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FinaldestinationOptions`: OptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `FinalDestinationAPI.FinaldestinationOptions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiFinaldestinationOptionsRequest struct via the builder pattern


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


## FinaldestinationPost

> FinalDestinationResponse FinaldestinationPost(ctx).FinalDestinationRequest(finalDestinationRequest).Execute()

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
	finalDestinationRequest := *openapiclient.NewFinalDestinationRequest([]openapiclient.FinalDestinationQuery{*openapiclient.NewFinalDestinationQuery()}) // FinalDestinationRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FinalDestinationAPI.FinaldestinationPost(context.Background()).FinalDestinationRequest(finalDestinationRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FinalDestinationAPI.FinaldestinationPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FinaldestinationPost`: FinalDestinationResponse
	fmt.Fprintf(os.Stdout, "Response from `FinalDestinationAPI.FinaldestinationPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFinaldestinationPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finalDestinationRequest** | [**FinalDestinationRequest**](FinalDestinationRequest.md) |  | 

### Return type

[**FinalDestinationResponse**](FinalDestinationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

