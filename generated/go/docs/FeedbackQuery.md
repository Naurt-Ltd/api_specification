# FeedbackQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | Existing Naurt ID for the address being updated | [optional] 
**AddressString** | Pointer to **string** | Address text for a new feedback item. Address strings are not matched with current data, so existing addresses should use &#x60;id&#x60; instead.  | [optional] 
**ParkingLocation** | Pointer to [**FeedbackLocation**](FeedbackLocation.md) |  | [optional] 
**DoorLocation** | Pointer to [**FeedbackLocation**](FeedbackLocation.md) |  | [optional] 

## Methods

### NewFeedbackQuery

`func NewFeedbackQuery() *FeedbackQuery`

NewFeedbackQuery instantiates a new FeedbackQuery object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackQueryWithDefaults

`func NewFeedbackQueryWithDefaults() *FeedbackQuery`

NewFeedbackQueryWithDefaults instantiates a new FeedbackQuery object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FeedbackQuery) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FeedbackQuery) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FeedbackQuery) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *FeedbackQuery) HasId() bool`

HasId returns a boolean if a field has been set.

### GetAddressString

`func (o *FeedbackQuery) GetAddressString() string`

GetAddressString returns the AddressString field if non-nil, zero value otherwise.

### GetAddressStringOk

`func (o *FeedbackQuery) GetAddressStringOk() (*string, bool)`

GetAddressStringOk returns a tuple with the AddressString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddressString

`func (o *FeedbackQuery) SetAddressString(v string)`

SetAddressString sets AddressString field to given value.

### HasAddressString

`func (o *FeedbackQuery) HasAddressString() bool`

HasAddressString returns a boolean if a field has been set.

### GetParkingLocation

`func (o *FeedbackQuery) GetParkingLocation() FeedbackLocation`

GetParkingLocation returns the ParkingLocation field if non-nil, zero value otherwise.

### GetParkingLocationOk

`func (o *FeedbackQuery) GetParkingLocationOk() (*FeedbackLocation, bool)`

GetParkingLocationOk returns a tuple with the ParkingLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParkingLocation

`func (o *FeedbackQuery) SetParkingLocation(v FeedbackLocation)`

SetParkingLocation sets ParkingLocation field to given value.

### HasParkingLocation

`func (o *FeedbackQuery) HasParkingLocation() bool`

HasParkingLocation returns a boolean if a field has been set.

### GetDoorLocation

`func (o *FeedbackQuery) GetDoorLocation() FeedbackLocation`

GetDoorLocation returns the DoorLocation field if non-nil, zero value otherwise.

### GetDoorLocationOk

`func (o *FeedbackQuery) GetDoorLocationOk() (*FeedbackLocation, bool)`

GetDoorLocationOk returns a tuple with the DoorLocation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDoorLocation

`func (o *FeedbackQuery) SetDoorLocation(v FeedbackLocation)`

SetDoorLocation sets DoorLocation field to given value.

### HasDoorLocation

`func (o *FeedbackQuery) HasDoorLocation() bool`

HasDoorLocation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


