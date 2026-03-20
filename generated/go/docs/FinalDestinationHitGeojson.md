# FinalDestinationHitGeojson

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Features** | [**[]Feature**](Feature.md) |  | 
**Type** | **string** |  | [default to "FeatureCollection"]
**Building** | Pointer to [**Polygon**](Polygon.md) |  | [optional] 
**DefaultGeocode** | [**Point**](Point.md) |  | 
**Entrance** | Pointer to [**Multipoint**](Multipoint.md) |  | [optional] 
**Parking** | Pointer to [**Polygon**](Polygon.md) |  | [optional] 

## Methods

### NewFinalDestinationHitGeojson

`func NewFinalDestinationHitGeojson(features []Feature, type_ string, defaultGeocode Point, ) *FinalDestinationHitGeojson`

NewFinalDestinationHitGeojson instantiates a new FinalDestinationHitGeojson object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationHitGeojsonWithDefaults

`func NewFinalDestinationHitGeojsonWithDefaults() *FinalDestinationHitGeojson`

NewFinalDestinationHitGeojsonWithDefaults instantiates a new FinalDestinationHitGeojson object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFeatures

`func (o *FinalDestinationHitGeojson) GetFeatures() []Feature`

GetFeatures returns the Features field if non-nil, zero value otherwise.

### GetFeaturesOk

`func (o *FinalDestinationHitGeojson) GetFeaturesOk() (*[]Feature, bool)`

GetFeaturesOk returns a tuple with the Features field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFeatures

`func (o *FinalDestinationHitGeojson) SetFeatures(v []Feature)`

SetFeatures sets Features field to given value.


### GetType

`func (o *FinalDestinationHitGeojson) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *FinalDestinationHitGeojson) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *FinalDestinationHitGeojson) SetType(v string)`

SetType sets Type field to given value.


### GetBuilding

`func (o *FinalDestinationHitGeojson) GetBuilding() Polygon`

GetBuilding returns the Building field if non-nil, zero value otherwise.

### GetBuildingOk

`func (o *FinalDestinationHitGeojson) GetBuildingOk() (*Polygon, bool)`

GetBuildingOk returns a tuple with the Building field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuilding

`func (o *FinalDestinationHitGeojson) SetBuilding(v Polygon)`

SetBuilding sets Building field to given value.

### HasBuilding

`func (o *FinalDestinationHitGeojson) HasBuilding() bool`

HasBuilding returns a boolean if a field has been set.

### GetDefaultGeocode

`func (o *FinalDestinationHitGeojson) GetDefaultGeocode() Point`

GetDefaultGeocode returns the DefaultGeocode field if non-nil, zero value otherwise.

### GetDefaultGeocodeOk

`func (o *FinalDestinationHitGeojson) GetDefaultGeocodeOk() (*Point, bool)`

GetDefaultGeocodeOk returns a tuple with the DefaultGeocode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultGeocode

`func (o *FinalDestinationHitGeojson) SetDefaultGeocode(v Point)`

SetDefaultGeocode sets DefaultGeocode field to given value.


### GetEntrance

`func (o *FinalDestinationHitGeojson) GetEntrance() Multipoint`

GetEntrance returns the Entrance field if non-nil, zero value otherwise.

### GetEntranceOk

`func (o *FinalDestinationHitGeojson) GetEntranceOk() (*Multipoint, bool)`

GetEntranceOk returns a tuple with the Entrance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntrance

`func (o *FinalDestinationHitGeojson) SetEntrance(v Multipoint)`

SetEntrance sets Entrance field to given value.

### HasEntrance

`func (o *FinalDestinationHitGeojson) HasEntrance() bool`

HasEntrance returns a boolean if a field has been set.

### GetParking

`func (o *FinalDestinationHitGeojson) GetParking() Polygon`

GetParking returns the Parking field if non-nil, zero value otherwise.

### GetParkingOk

`func (o *FinalDestinationHitGeojson) GetParkingOk() (*Polygon, bool)`

GetParkingOk returns a tuple with the Parking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParking

`func (o *FinalDestinationHitGeojson) SetParking(v Polygon)`

SetParking sets Parking field to given value.

### HasParking

`func (o *FinalDestinationHitGeojson) HasParking() bool`

HasParking returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


