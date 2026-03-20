# FeatureGeometry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Coordinates** | [**[][][]float64**]([][]float64.md) |  | 
**Type** | **string** |  | 

## Methods

### NewFeatureGeometry

`func NewFeatureGeometry(coordinates [][][]float64, type_ string, ) *FeatureGeometry`

NewFeatureGeometry instantiates a new FeatureGeometry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeatureGeometryWithDefaults

`func NewFeatureGeometryWithDefaults() *FeatureGeometry`

NewFeatureGeometryWithDefaults instantiates a new FeatureGeometry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCoordinates

`func (o *FeatureGeometry) GetCoordinates() [][][]float64`

GetCoordinates returns the Coordinates field if non-nil, zero value otherwise.

### GetCoordinatesOk

`func (o *FeatureGeometry) GetCoordinatesOk() (*[][][]float64, bool)`

GetCoordinatesOk returns a tuple with the Coordinates field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCoordinates

`func (o *FeatureGeometry) SetCoordinates(v [][][]float64)`

SetCoordinates sets Coordinates field to given value.


### GetType

`func (o *FeatureGeometry) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FeatureGeometry) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FeatureGeometry) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


