# FeatureProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NaurtType** | **string** |  | 
**Accuracy** | Pointer to [**Accuracy**](Accuracy.md) |  | [optional] 
**MinimumParkingToDoorDistance** | Pointer to **float64** |  | [optional] 

## Methods

### NewFeatureProperties

`func NewFeatureProperties(naurtType string, ) *FeatureProperties`

NewFeatureProperties instantiates a new FeatureProperties object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeaturePropertiesWithDefaults

`func NewFeaturePropertiesWithDefaults() *FeatureProperties`

NewFeaturePropertiesWithDefaults instantiates a new FeatureProperties object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNaurtType

`func (o *FeatureProperties) GetNaurtType() string`

GetNaurtType returns the NaurtType field if non-nil, zero value otherwise.

### GetNaurtTypeOk

`func (o *FeatureProperties) GetNaurtTypeOk() (*string, bool)`

GetNaurtTypeOk returns a tuple with the NaurtType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNaurtType

`func (o *FeatureProperties) SetNaurtType(v string)`

SetNaurtType sets NaurtType field to given value.


### GetAccuracy

`func (o *FeatureProperties) GetAccuracy() Accuracy`

GetAccuracy returns the Accuracy field if non-nil, zero value otherwise.

### GetAccuracyOk

`func (o *FeatureProperties) GetAccuracyOk() (*Accuracy, bool)`

GetAccuracyOk returns a tuple with the Accuracy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccuracy

`func (o *FeatureProperties) SetAccuracy(v Accuracy)`

SetAccuracy sets Accuracy field to given value.

### HasAccuracy

`func (o *FeatureProperties) HasAccuracy() bool`

HasAccuracy returns a boolean if a field has been set.

### GetMinimumParkingToDoorDistance

`func (o *FeatureProperties) GetMinimumParkingToDoorDistance() float64`

GetMinimumParkingToDoorDistance returns the MinimumParkingToDoorDistance field if non-nil, zero value otherwise.

### GetMinimumParkingToDoorDistanceOk

`func (o *FeatureProperties) GetMinimumParkingToDoorDistanceOk() (*float64, bool)`

GetMinimumParkingToDoorDistanceOk returns a tuple with the MinimumParkingToDoorDistance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimumParkingToDoorDistance

`func (o *FeatureProperties) SetMinimumParkingToDoorDistance(v float64)`

SetMinimumParkingToDoorDistance sets MinimumParkingToDoorDistance field to given value.

### HasMinimumParkingToDoorDistance

`func (o *FeatureProperties) HasMinimumParkingToDoorDistance() bool`

HasMinimumParkingToDoorDistance returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


