# FinalDestinationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Responses** | [**[]FinalDestinationHits**](FinalDestinationHits.md) |  | 
**Logging** | Pointer to [**FinalDestinationLogging**](FinalDestinationLogging.md) |  | [optional] 
**Version** | **string** |  | 
**RequestId** | **string** |  | 

## Methods

### NewFinalDestinationResponse

`func NewFinalDestinationResponse(responses []FinalDestinationHits, version string, requestId string, ) *FinalDestinationResponse`

NewFinalDestinationResponse instantiates a new FinalDestinationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationResponseWithDefaults

`func NewFinalDestinationResponseWithDefaults() *FinalDestinationResponse`

NewFinalDestinationResponseWithDefaults instantiates a new FinalDestinationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResponses

`func (o *FinalDestinationResponse) GetResponses() []FinalDestinationHits`

GetResponses returns the Responses field if non-nil, zero value otherwise.

### GetResponsesOk

`func (o *FinalDestinationResponse) GetResponsesOk() (*[]FinalDestinationHits, bool)`

GetResponsesOk returns a tuple with the Responses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponses

`func (o *FinalDestinationResponse) SetResponses(v []FinalDestinationHits)`

SetResponses sets Responses field to given value.


### GetLogging

`func (o *FinalDestinationResponse) GetLogging() FinalDestinationLogging`

GetLogging returns the Logging field if non-nil, zero value otherwise.

### GetLoggingOk

`func (o *FinalDestinationResponse) GetLoggingOk() (*FinalDestinationLogging, bool)`

GetLoggingOk returns a tuple with the Logging field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogging

`func (o *FinalDestinationResponse) SetLogging(v FinalDestinationLogging)`

SetLogging sets Logging field to given value.

### HasLogging

`func (o *FinalDestinationResponse) HasLogging() bool`

HasLogging returns a boolean if a field has been set.

### GetVersion

`func (o *FinalDestinationResponse) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *FinalDestinationResponse) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *FinalDestinationResponse) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetRequestId

`func (o *FinalDestinationResponse) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *FinalDestinationResponse) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *FinalDestinationResponse) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


