# RendezvousRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | [**[]RendezvousQuery**](RendezvousQuery.md) | List of Query objects. The Query object is shared across Naurt APIs. Different query types may be mixed in the same request.  | 
**Options** | Pointer to **map[string]interface{}** | Optional Rendezvous request options | [optional] 

## Methods

### NewRendezvousRequest

`func NewRendezvousRequest(queries []RendezvousQuery, ) *RendezvousRequest`

NewRendezvousRequest instantiates a new RendezvousRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRendezvousRequestWithDefaults

`func NewRendezvousRequestWithDefaults() *RendezvousRequest`

NewRendezvousRequestWithDefaults instantiates a new RendezvousRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueries

`func (o *RendezvousRequest) GetQueries() []RendezvousQuery`

GetQueries returns the Queries field if non-nil, zero value otherwise.

### GetQueriesOk

`func (o *RendezvousRequest) GetQueriesOk() (*[]RendezvousQuery, bool)`

GetQueriesOk returns a tuple with the Queries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueries

`func (o *RendezvousRequest) SetQueries(v []RendezvousQuery)`

SetQueries sets Queries field to given value.


### GetOptions

`func (o *RendezvousRequest) GetOptions() map[string]interface{}`

GetOptions returns the Options field if non-nil, zero value otherwise.

### GetOptionsOk

`func (o *RendezvousRequest) GetOptionsOk() (*map[string]interface{}, bool)`

GetOptionsOk returns a tuple with the Options field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptions

`func (o *RendezvousRequest) SetOptions(v map[string]interface{})`

SetOptions sets Options field to given value.

### HasOptions

`func (o *RendezvousRequest) HasOptions() bool`

HasOptions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


