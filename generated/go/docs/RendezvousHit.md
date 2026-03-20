# RendezvousHit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Centre** | [**RendezvousHitData**](RendezvousHitData.md) |  | 
**Covers** | [**[]RendezvousHitData**](RendezvousHitData.md) |  | 

## Methods

### NewRendezvousHit

`func NewRendezvousHit(centre RendezvousHitData, covers []RendezvousHitData, ) *RendezvousHit`

NewRendezvousHit instantiates a new RendezvousHit object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRendezvousHitWithDefaults

`func NewRendezvousHitWithDefaults() *RendezvousHit`

NewRendezvousHitWithDefaults instantiates a new RendezvousHit object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCentre

`func (o *RendezvousHit) GetCentre() RendezvousHitData`

GetCentre returns the Centre field if non-nil, zero value otherwise.

### GetCentreOk

`func (o *RendezvousHit) GetCentreOk() (*RendezvousHitData, bool)`

GetCentreOk returns a tuple with the Centre field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCentre

`func (o *RendezvousHit) SetCentre(v RendezvousHitData)`

SetCentre sets Centre field to given value.


### GetCovers

`func (o *RendezvousHit) GetCovers() []RendezvousHitData`

GetCovers returns the Covers field if non-nil, zero value otherwise.

### GetCoversOk

`func (o *RendezvousHit) GetCoversOk() (*[]RendezvousHitData, bool)`

GetCoversOk returns a tuple with the Covers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCovers

`func (o *RendezvousHit) SetCovers(v []RendezvousHitData)`

SetCovers sets Covers field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


