# FinalDestinationQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AddressString** | Pointer to **string** |  | [optional] 
**AddressStructured** | Pointer to [**StructuredAddress**](StructuredAddress.md) |  | [optional] 
**Location** | Pointer to [**FinalDestinationLocation**](FinalDestinationLocation.md) |  | [optional] 
**Id** | Pointer to **string** |  | [optional] 
**Country** | Pointer to [**Country**](Country.md) |  | [optional] 
**SourceId** | Pointer to [**FinalDestinationSourceIdRequest**](FinalDestinationSourceIdRequest.md) |  | [optional] 
**AdditionalMatches** | Pointer to **bool** |  | [optional] [default to false]
**Language** | Pointer to [**Language**](Language.md) |  | [optional] [default to LANGUAGE_AUTO]

## Methods

### NewFinalDestinationQuery

`func NewFinalDestinationQuery() *FinalDestinationQuery`

NewFinalDestinationQuery instantiates a new FinalDestinationQuery object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationQueryWithDefaults

`func NewFinalDestinationQueryWithDefaults() *FinalDestinationQuery`

NewFinalDestinationQueryWithDefaults instantiates a new FinalDestinationQuery object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAddressString

`func (o *FinalDestinationQuery) GetAddressString() string`

GetAddressString returns the AddressString field if non-nil, zero value otherwise.

### GetAddressStringOk

`func (o *FinalDestinationQuery) GetAddressStringOk() (*string, bool)`

GetAddressStringOk returns a tuple with the AddressString field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddressString

`func (o *FinalDestinationQuery) SetAddressString(v string)`

SetAddressString sets AddressString field to given value.

### HasAddressString

`func (o *FinalDestinationQuery) HasAddressString() bool`

HasAddressString returns a boolean if a field has been set.

### GetAddressStructured

`func (o *FinalDestinationQuery) GetAddressStructured() StructuredAddress`

GetAddressStructured returns the AddressStructured field if non-nil, zero value otherwise.

### GetAddressStructuredOk

`func (o *FinalDestinationQuery) GetAddressStructuredOk() (*StructuredAddress, bool)`

GetAddressStructuredOk returns a tuple with the AddressStructured field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddressStructured

`func (o *FinalDestinationQuery) SetAddressStructured(v StructuredAddress)`

SetAddressStructured sets AddressStructured field to given value.

### HasAddressStructured

`func (o *FinalDestinationQuery) HasAddressStructured() bool`

HasAddressStructured returns a boolean if a field has been set.

### GetLocation

`func (o *FinalDestinationQuery) GetLocation() FinalDestinationLocation`

GetLocation returns the Location field if non-nil, zero value otherwise.

### GetLocationOk

`func (o *FinalDestinationQuery) GetLocationOk() (*FinalDestinationLocation, bool)`

GetLocationOk returns a tuple with the Location field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocation

`func (o *FinalDestinationQuery) SetLocation(v FinalDestinationLocation)`

SetLocation sets Location field to given value.

### HasLocation

`func (o *FinalDestinationQuery) HasLocation() bool`

HasLocation returns a boolean if a field has been set.

### GetId

`func (o *FinalDestinationQuery) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FinalDestinationQuery) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FinalDestinationQuery) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *FinalDestinationQuery) HasId() bool`

HasId returns a boolean if a field has been set.

### GetCountry

`func (o *FinalDestinationQuery) GetCountry() Country`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *FinalDestinationQuery) GetCountryOk() (*Country, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *FinalDestinationQuery) SetCountry(v Country)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *FinalDestinationQuery) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetSourceId

`func (o *FinalDestinationQuery) GetSourceId() FinalDestinationSourceIdRequest`

GetSourceId returns the SourceId field if non-nil, zero value otherwise.

### GetSourceIdOk

`func (o *FinalDestinationQuery) GetSourceIdOk() (*FinalDestinationSourceIdRequest, bool)`

GetSourceIdOk returns a tuple with the SourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceId

`func (o *FinalDestinationQuery) SetSourceId(v FinalDestinationSourceIdRequest)`

SetSourceId sets SourceId field to given value.

### HasSourceId

`func (o *FinalDestinationQuery) HasSourceId() bool`

HasSourceId returns a boolean if a field has been set.

### GetAdditionalMatches

`func (o *FinalDestinationQuery) GetAdditionalMatches() bool`

GetAdditionalMatches returns the AdditionalMatches field if non-nil, zero value otherwise.

### GetAdditionalMatchesOk

`func (o *FinalDestinationQuery) GetAdditionalMatchesOk() (*bool, bool)`

GetAdditionalMatchesOk returns a tuple with the AdditionalMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalMatches

`func (o *FinalDestinationQuery) SetAdditionalMatches(v bool)`

SetAdditionalMatches sets AdditionalMatches field to given value.

### HasAdditionalMatches

`func (o *FinalDestinationQuery) HasAdditionalMatches() bool`

HasAdditionalMatches returns a boolean if a field has been set.

### GetLanguage

`func (o *FinalDestinationQuery) GetLanguage() Language`

GetLanguage returns the Language field if non-nil, zero value otherwise.

### GetLanguageOk

`func (o *FinalDestinationQuery) GetLanguageOk() (*Language, bool)`

GetLanguageOk returns a tuple with the Language field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLanguage

`func (o *FinalDestinationQuery) SetLanguage(v Language)`

SetLanguage sets Language field to given value.

### HasLanguage

`func (o *FinalDestinationQuery) HasLanguage() bool`

HasLanguage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


