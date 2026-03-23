# Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Geometry** | [**FeatureGeometry**](FeatureGeometry.md) |  | 
**Properties** | [**FeatureProperties**](FeatureProperties.md) |  | 
**Type** | **string** |  | 

## Methods

### NewFeature

`func NewFeature(geometry FeatureGeometry, properties FeatureProperties, type_ string, ) *Feature`

NewFeature instantiates a new Feature object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeatureWithDefaults

`func NewFeatureWithDefaults() *Feature`

NewFeatureWithDefaults instantiates a new Feature object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGeometry

`func (o *Feature) GetGeometry() FeatureGeometry`

GetGeometry returns the Geometry field if non-nil, zero value otherwise.

### GetGeometryOk

`func (o *Feature) GetGeometryOk() (*FeatureGeometry, bool)`

GetGeometryOk returns a tuple with the Geometry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeometry

`func (o *Feature) SetGeometry(v FeatureGeometry)`

SetGeometry sets Geometry field to given value.


### GetProperties

`func (o *Feature) GetProperties() FeatureProperties`

GetProperties returns the Properties field if non-nil, zero value otherwise.

### GetPropertiesOk

`func (o *Feature) GetPropertiesOk() (*FeatureProperties, bool)`

GetPropertiesOk returns a tuple with the Properties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProperties

`func (o *Feature) SetProperties(v FeatureProperties)`

SetProperties sets Properties field to given value.


### GetType

`func (o *Feature) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Feature) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Feature) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


