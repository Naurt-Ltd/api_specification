# FinalDestinationHit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Address** | **string** |  | 
**Geojson** | [**FinalDestinationHitGeojson**](FinalDestinationHitGeojson.md) |  | 
**Distance** | Pointer to **float32** |  | [optional] 
**SearchConfidence** | Pointer to **float64** | Confidence score in the range 0.0 to 1.0 indicating how well the result  matches the query. Higher is better.  See: https://docs.naurt.com/reference/search-confidence  Not to be confused with Accuracy, which is how good the data itself is. This  is about the likelihood of a good match.  | [optional] 
**StructuredResponse** | Pointer to [**StructuredAddress**](StructuredAddress.md) |  | [optional] 
**SourceId** | Pointer to [**FinalDestinationSourceIdResponse**](FinalDestinationSourceIdResponse.md) |  | [optional] 

## Methods

### NewFinalDestinationHit

`func NewFinalDestinationHit(id string, address string, geojson FinalDestinationHitGeojson, ) *FinalDestinationHit`

NewFinalDestinationHit instantiates a new FinalDestinationHit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationHitWithDefaults

`func NewFinalDestinationHitWithDefaults() *FinalDestinationHit`

NewFinalDestinationHitWithDefaults instantiates a new FinalDestinationHit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FinalDestinationHit) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FinalDestinationHit) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FinalDestinationHit) SetId(v string)`

SetId sets Id field to given value.


### GetAddress

`func (o *FinalDestinationHit) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *FinalDestinationHit) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *FinalDestinationHit) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetGeojson

`func (o *FinalDestinationHit) GetGeojson() FinalDestinationHitGeojson`

GetGeojson returns the Geojson field if non-nil, zero value otherwise.

### GetGeojsonOk

`func (o *FinalDestinationHit) GetGeojsonOk() (*FinalDestinationHitGeojson, bool)`

GetGeojsonOk returns a tuple with the Geojson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeojson

`func (o *FinalDestinationHit) SetGeojson(v FinalDestinationHitGeojson)`

SetGeojson sets Geojson field to given value.


### GetDistance

`func (o *FinalDestinationHit) GetDistance() float32`

GetDistance returns the Distance field if non-nil, zero value otherwise.

### GetDistanceOk

`func (o *FinalDestinationHit) GetDistanceOk() (*float32, bool)`

GetDistanceOk returns a tuple with the Distance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistance

`func (o *FinalDestinationHit) SetDistance(v float32)`

SetDistance sets Distance field to given value.

### HasDistance

`func (o *FinalDestinationHit) HasDistance() bool`

HasDistance returns a boolean if a field has been set.

### GetSearchConfidence

`func (o *FinalDestinationHit) GetSearchConfidence() float64`

GetSearchConfidence returns the SearchConfidence field if non-nil, zero value otherwise.

### GetSearchConfidenceOk

`func (o *FinalDestinationHit) GetSearchConfidenceOk() (*float64, bool)`

GetSearchConfidenceOk returns a tuple with the SearchConfidence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSearchConfidence

`func (o *FinalDestinationHit) SetSearchConfidence(v float64)`

SetSearchConfidence sets SearchConfidence field to given value.

### HasSearchConfidence

`func (o *FinalDestinationHit) HasSearchConfidence() bool`

HasSearchConfidence returns a boolean if a field has been set.

### GetStructuredResponse

`func (o *FinalDestinationHit) GetStructuredResponse() StructuredAddress`

GetStructuredResponse returns the StructuredResponse field if non-nil, zero value otherwise.

### GetStructuredResponseOk

`func (o *FinalDestinationHit) GetStructuredResponseOk() (*StructuredAddress, bool)`

GetStructuredResponseOk returns a tuple with the StructuredResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStructuredResponse

`func (o *FinalDestinationHit) SetStructuredResponse(v StructuredAddress)`

SetStructuredResponse sets StructuredResponse field to given value.

### HasStructuredResponse

`func (o *FinalDestinationHit) HasStructuredResponse() bool`

HasStructuredResponse returns a boolean if a field has been set.

### GetSourceId

`func (o *FinalDestinationHit) GetSourceId() FinalDestinationSourceIdResponse`

GetSourceId returns the SourceId field if non-nil, zero value otherwise.

### GetSourceIdOk

`func (o *FinalDestinationHit) GetSourceIdOk() (*FinalDestinationSourceIdResponse, bool)`

GetSourceIdOk returns a tuple with the SourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceId

`func (o *FinalDestinationHit) SetSourceId(v FinalDestinationSourceIdResponse)`

SetSourceId sets SourceId field to given value.

### HasSourceId

`func (o *FinalDestinationHit) HasSourceId() bool`

HasSourceId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


