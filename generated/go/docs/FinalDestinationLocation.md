# FinalDestinationLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Latitude** | **float32** |  | 
**Longitude** | **float32** |  | 
**DistanceFilter** | Pointer to **float32** |  | [optional] [default to 5000]

## Methods

### NewFinalDestinationLocation

`func NewFinalDestinationLocation(latitude float32, longitude float32, ) *FinalDestinationLocation`

NewFinalDestinationLocation instantiates a new FinalDestinationLocation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationLocationWithDefaults

`func NewFinalDestinationLocationWithDefaults() *FinalDestinationLocation`

NewFinalDestinationLocationWithDefaults instantiates a new FinalDestinationLocation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLatitude

`func (o *FinalDestinationLocation) GetLatitude() float32`

GetLatitude returns the Latitude field if non-nil, zero value otherwise.

### GetLatitudeOk

`func (o *FinalDestinationLocation) GetLatitudeOk() (*float32, bool)`

GetLatitudeOk returns a tuple with the Latitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLatitude

`func (o *FinalDestinationLocation) SetLatitude(v float32)`

SetLatitude sets Latitude field to given value.


### GetLongitude

`func (o *FinalDestinationLocation) GetLongitude() float32`

GetLongitude returns the Longitude field if non-nil, zero value otherwise.

### GetLongitudeOk

`func (o *FinalDestinationLocation) GetLongitudeOk() (*float32, bool)`

GetLongitudeOk returns a tuple with the Longitude field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLongitude

`func (o *FinalDestinationLocation) SetLongitude(v float32)`

SetLongitude sets Longitude field to given value.


### GetDistanceFilter

`func (o *FinalDestinationLocation) GetDistanceFilter() float32`

GetDistanceFilter returns the DistanceFilter field if non-nil, zero value otherwise.

### GetDistanceFilterOk

`func (o *FinalDestinationLocation) GetDistanceFilterOk() (*float32, bool)`

GetDistanceFilterOk returns a tuple with the DistanceFilter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistanceFilter

`func (o *FinalDestinationLocation) SetDistanceFilter(v float32)`

SetDistanceFilter sets DistanceFilter field to given value.

### HasDistanceFilter

`func (o *FinalDestinationLocation) HasDistanceFilter() bool`

HasDistanceFilter returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


