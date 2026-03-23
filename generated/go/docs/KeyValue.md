# KeyValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Building** | Pointer to [**Polygon**](Polygon.md) |  | [optional] 
**DefaultGeocode** | [**Point**](Point.md) |  | 
**Entrance** | Pointer to [**Multipoint**](Multipoint.md) |  | [optional] 
**Parking** | Pointer to [**Polygon**](Polygon.md) |  | [optional] 

## Methods

### NewKeyValue

`func NewKeyValue(defaultGeocode Point, ) *KeyValue`

NewKeyValue instantiates a new KeyValue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewKeyValueWithDefaults

`func NewKeyValueWithDefaults() *KeyValue`

NewKeyValueWithDefaults instantiates a new KeyValue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBuilding

`func (o *KeyValue) GetBuilding() Polygon`

GetBuilding returns the Building field if non-nil, zero value otherwise.

### GetBuildingOk

`func (o *KeyValue) GetBuildingOk() (*Polygon, bool)`

GetBuildingOk returns a tuple with the Building field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuilding

`func (o *KeyValue) SetBuilding(v Polygon)`

SetBuilding sets Building field to given value.

### HasBuilding

`func (o *KeyValue) HasBuilding() bool`

HasBuilding returns a boolean if a field has been set.

### GetDefaultGeocode

`func (o *KeyValue) GetDefaultGeocode() Point`

GetDefaultGeocode returns the DefaultGeocode field if non-nil, zero value otherwise.

### GetDefaultGeocodeOk

`func (o *KeyValue) GetDefaultGeocodeOk() (*Point, bool)`

GetDefaultGeocodeOk returns a tuple with the DefaultGeocode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultGeocode

`func (o *KeyValue) SetDefaultGeocode(v Point)`

SetDefaultGeocode sets DefaultGeocode field to given value.


### GetEntrance

`func (o *KeyValue) GetEntrance() Multipoint`

GetEntrance returns the Entrance field if non-nil, zero value otherwise.

### GetEntranceOk

`func (o *KeyValue) GetEntranceOk() (*Multipoint, bool)`

GetEntranceOk returns a tuple with the Entrance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntrance

`func (o *KeyValue) SetEntrance(v Multipoint)`

SetEntrance sets Entrance field to given value.

### HasEntrance

`func (o *KeyValue) HasEntrance() bool`

HasEntrance returns a boolean if a field has been set.

### GetParking

`func (o *KeyValue) GetParking() Polygon`

GetParking returns the Parking field if non-nil, zero value otherwise.

### GetParkingOk

`func (o *KeyValue) GetParkingOk() (*Polygon, bool)`

GetParkingOk returns a tuple with the Parking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParking

`func (o *KeyValue) SetParking(v Polygon)`

SetParking sets Parking field to given value.

### HasParking

`func (o *KeyValue) HasParking() bool`

HasParking returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


