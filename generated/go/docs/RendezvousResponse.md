# RendezvousResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Responses** | [**[]RendezvousHit**](RendezvousHit.md) |  | 
**Unmatched** | [**[]RendezvousQuery**](RendezvousQuery.md) | Queries that could not be matched | 
**Version** | Pointer to **NullableString** | API version used to service the request | [optional] 
**RequestId** | Pointer to **NullableString** | Request identifier useful when reporting issues to Naurt. Mentioned in the prose docs, though not shown in the response shape block.  | [optional] 

## Methods

### NewRendezvousResponse

`func NewRendezvousResponse(responses []RendezvousHit, unmatched []RendezvousQuery, ) *RendezvousResponse`

NewRendezvousResponse instantiates a new RendezvousResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRendezvousResponseWithDefaults

`func NewRendezvousResponseWithDefaults() *RendezvousResponse`

NewRendezvousResponseWithDefaults instantiates a new RendezvousResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResponses

`func (o *RendezvousResponse) GetResponses() []RendezvousHit`

GetResponses returns the Responses field if non-nil, zero value otherwise.

### GetResponsesOk

`func (o *RendezvousResponse) GetResponsesOk() (*[]RendezvousHit, bool)`

GetResponsesOk returns a tuple with the Responses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponses

`func (o *RendezvousResponse) SetResponses(v []RendezvousHit)`

SetResponses sets Responses field to given value.


### GetUnmatched

`func (o *RendezvousResponse) GetUnmatched() []RendezvousQuery`

GetUnmatched returns the Unmatched field if non-nil, zero value otherwise.

### GetUnmatchedOk

`func (o *RendezvousResponse) GetUnmatchedOk() (*[]RendezvousQuery, bool)`

GetUnmatchedOk returns a tuple with the Unmatched field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnmatched

`func (o *RendezvousResponse) SetUnmatched(v []RendezvousQuery)`

SetUnmatched sets Unmatched field to given value.


### GetVersion

`func (o *RendezvousResponse) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *RendezvousResponse) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *RendezvousResponse) SetVersion(v string)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *RendezvousResponse) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### SetVersionNil

`func (o *RendezvousResponse) SetVersionNil(b bool)`

 SetVersionNil sets the value for Version to be an explicit nil

### UnsetVersion
`func (o *RendezvousResponse) UnsetVersion()`

UnsetVersion ensures that no value is present for Version, not even an explicit nil
### GetRequestId

`func (o *RendezvousResponse) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *RendezvousResponse) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *RendezvousResponse) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *RendezvousResponse) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.

### SetRequestIdNil

`func (o *RendezvousResponse) SetRequestIdNil(b bool)`

 SetRequestIdNil sets the value for RequestId to be an explicit nil

### UnsetRequestId
`func (o *RendezvousResponse) UnsetRequestId()`

UnsetRequestId ensures that no value is present for RequestId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


