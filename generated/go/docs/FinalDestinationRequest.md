# FinalDestinationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | [**[]FinalDestinationQuery**](FinalDestinationQuery.md) |  | 
**Options** | Pointer to [**FinalDestinationOptions**](FinalDestinationOptions.md) |  | [optional] 

## Methods

### NewFinalDestinationRequest

`func NewFinalDestinationRequest(queries []FinalDestinationQuery, ) *FinalDestinationRequest`

NewFinalDestinationRequest instantiates a new FinalDestinationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationRequestWithDefaults

`func NewFinalDestinationRequestWithDefaults() *FinalDestinationRequest`

NewFinalDestinationRequestWithDefaults instantiates a new FinalDestinationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueries

`func (o *FinalDestinationRequest) GetQueries() []FinalDestinationQuery`

GetQueries returns the Queries field if non-nil, zero value otherwise.

### GetQueriesOk

`func (o *FinalDestinationRequest) GetQueriesOk() (*[]FinalDestinationQuery, bool)`

GetQueriesOk returns a tuple with the Queries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueries

`func (o *FinalDestinationRequest) SetQueries(v []FinalDestinationQuery)`

SetQueries sets Queries field to given value.


### GetOptions

`func (o *FinalDestinationRequest) GetOptions() FinalDestinationOptions`

GetOptions returns the Options field if non-nil, zero value otherwise.

### GetOptionsOk

`func (o *FinalDestinationRequest) GetOptionsOk() (*FinalDestinationOptions, bool)`

GetOptionsOk returns a tuple with the Options field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptions

`func (o *FinalDestinationRequest) SetOptions(v FinalDestinationOptions)`

SetOptions sets Options field to given value.

### HasOptions

`func (o *FinalDestinationRequest) HasOptions() bool`

HasOptions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


