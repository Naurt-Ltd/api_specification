# Multipoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Coordinates** | Pointer to **[][]float64** |  | [optional] 
**Type** | Pointer to **string** |  | [optional] 

## Methods

### NewMultipoint

`func NewMultipoint() *Multipoint`

NewMultipoint instantiates a new Multipoint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMultipointWithDefaults

`func NewMultipointWithDefaults() *Multipoint`

NewMultipointWithDefaults instantiates a new Multipoint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCoordinates

`func (o *Multipoint) GetCoordinates() [][]float64`

GetCoordinates returns the Coordinates field if non-nil, zero value otherwise.

### GetCoordinatesOk

`func (o *Multipoint) GetCoordinatesOk() (*[][]float64, bool)`

GetCoordinatesOk returns a tuple with the Coordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoordinates

`func (o *Multipoint) SetCoordinates(v [][]float64)`

SetCoordinates sets Coordinates field to given value.

### HasCoordinates

`func (o *Multipoint) HasCoordinates() bool`

HasCoordinates returns a boolean if a field has been set.

### GetType

`func (o *Multipoint) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Multipoint) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Multipoint) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *Multipoint) HasType() bool`

HasType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


