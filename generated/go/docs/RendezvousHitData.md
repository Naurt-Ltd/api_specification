# RendezvousHitData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Address** | **string** | Normalised address; may differ from the searched address | 
**Geojson** | [**FeatureCollection**](FeatureCollection.md) |  | 
**Distance** | Pointer to **float32** | Distance in metres from the searched latitude/longitude. Present only when searching with latitude and longitude.  | [optional] 

## Methods

### NewRendezvousHitData

`func NewRendezvousHitData(id string, address string, geojson FeatureCollection, ) *RendezvousHitData`

NewRendezvousHitData instantiates a new RendezvousHitData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRendezvousHitDataWithDefaults

`func NewRendezvousHitDataWithDefaults() *RendezvousHitData`

NewRendezvousHitDataWithDefaults instantiates a new RendezvousHitData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *RendezvousHitData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RendezvousHitData) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RendezvousHitData) SetId(v string)`

SetId sets Id field to given value.


### GetAddress

`func (o *RendezvousHitData) GetAddress() string`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *RendezvousHitData) GetAddressOk() (*string, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *RendezvousHitData) SetAddress(v string)`

SetAddress sets Address field to given value.


### GetGeojson

`func (o *RendezvousHitData) GetGeojson() FeatureCollection`

GetGeojson returns the Geojson field if non-nil, zero value otherwise.

### GetGeojsonOk

`func (o *RendezvousHitData) GetGeojsonOk() (*FeatureCollection, bool)`

GetGeojsonOk returns a tuple with the Geojson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeojson

`func (o *RendezvousHitData) SetGeojson(v FeatureCollection)`

SetGeojson sets Geojson field to given value.


### GetDistance

`func (o *RendezvousHitData) GetDistance() float32`

GetDistance returns the Distance field if non-nil, zero value otherwise.

### GetDistanceOk

`func (o *RendezvousHitData) GetDistanceOk() (*float32, bool)`

GetDistanceOk returns a tuple with the Distance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistance

`func (o *RendezvousHitData) SetDistance(v float32)`

SetDistance sets Distance field to given value.

### HasDistance

`func (o *RendezvousHitData) HasDistance() bool`

HasDistance returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


