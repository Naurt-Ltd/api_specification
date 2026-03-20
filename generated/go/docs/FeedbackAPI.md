# \FeedbackAPI

All URIs are relative to *https://api.naurt.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**FeedbackOptions**](FeedbackAPI.md#FeedbackOptions) | **Options** /feedback/v2 | Options
[**FeedbackPost**](FeedbackAPI.md#FeedbackPost) | **Post** /feedback/v2 | Post



## FeedbackOptions

> OptionsResponse FeedbackOptions(ctx).Execute()

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
	resp, r, err := apiClient.FeedbackAPI.FeedbackOptions(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FeedbackAPI.FeedbackOptions``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FeedbackOptions`: OptionsResponse
	fmt.Fprintf(os.Stdout, "Response from `FeedbackAPI.FeedbackOptions`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiFeedbackOptionsRequest struct via the builder pattern


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


## FeedbackPost

> FeedbackResponse FeedbackPost(ctx).FeedbackRequest(feedbackRequest).Execute()

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
	feedbackRequest := *openapiclient.NewFeedbackRequest([]openapiclient.FeedbackQuery{*openapiclient.NewFeedbackQuery()}) // FeedbackRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FeedbackAPI.FeedbackPost(context.Background()).FeedbackRequest(feedbackRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FeedbackAPI.FeedbackPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `FeedbackPost`: FeedbackResponse
	fmt.Fprintf(os.Stdout, "Response from `FeedbackAPI.FeedbackPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiFeedbackPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedbackRequest** | [**FeedbackRequest**](FeedbackRequest.md) |  | 

### Return type

[**FeedbackResponse**](FeedbackResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

