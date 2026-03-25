# StructuredAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Unit** | Pointer to **string** |  | [optional] 
**HouseName** | Pointer to **string** |  | [optional] 
**StreetNumber** | Pointer to **string** |  | [optional] 
**StreetName** | Pointer to **string** |  | [optional] 
**Locality** | Pointer to **string** |  | [optional] 
**City** | Pointer to **string** |  | [optional] 
**County** | Pointer to **string** |  | [optional] 
**State** | Pointer to **string** |  | [optional] 
**Country** | Pointer to **string** |  | [optional] 
**Postalcode** | Pointer to **string** |  | [optional] 
**CountryCode** | Pointer to [**Country**](Country.md) |  | [optional] 

## Methods

### NewStructuredAddress

`func NewStructuredAddress() *StructuredAddress`

NewStructuredAddress instantiates a new StructuredAddress object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStructuredAddressWithDefaults

`func NewStructuredAddressWithDefaults() *StructuredAddress`

NewStructuredAddressWithDefaults instantiates a new StructuredAddress object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUnit

`func (o *StructuredAddress) GetUnit() string`

GetUnit returns the Unit field if non-nil, zero value otherwise.

### GetUnitOk

`func (o *StructuredAddress) GetUnitOk() (*string, bool)`

GetUnitOk returns a tuple with the Unit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnit

`func (o *StructuredAddress) SetUnit(v string)`

SetUnit sets Unit field to given value.

### HasUnit

`func (o *StructuredAddress) HasUnit() bool`

HasUnit returns a boolean if a field has been set.

### GetHouseName

`func (o *StructuredAddress) GetHouseName() string`

GetHouseName returns the HouseName field if non-nil, zero value otherwise.

### GetHouseNameOk

`func (o *StructuredAddress) GetHouseNameOk() (*string, bool)`

GetHouseNameOk returns a tuple with the HouseName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHouseName

`func (o *StructuredAddress) SetHouseName(v string)`

SetHouseName sets HouseName field to given value.

### HasHouseName

`func (o *StructuredAddress) HasHouseName() bool`

HasHouseName returns a boolean if a field has been set.

### GetStreetNumber

`func (o *StructuredAddress) GetStreetNumber() string`

GetStreetNumber returns the StreetNumber field if non-nil, zero value otherwise.

### GetStreetNumberOk

`func (o *StructuredAddress) GetStreetNumberOk() (*string, bool)`

GetStreetNumberOk returns a tuple with the StreetNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetNumber

`func (o *StructuredAddress) SetStreetNumber(v string)`

SetStreetNumber sets StreetNumber field to given value.

### HasStreetNumber

`func (o *StructuredAddress) HasStreetNumber() bool`

HasStreetNumber returns a boolean if a field has been set.

### GetStreetName

`func (o *StructuredAddress) GetStreetName() string`

GetStreetName returns the StreetName field if non-nil, zero value otherwise.

### GetStreetNameOk

`func (o *StructuredAddress) GetStreetNameOk() (*string, bool)`

GetStreetNameOk returns a tuple with the StreetName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetName

`func (o *StructuredAddress) SetStreetName(v string)`

SetStreetName sets StreetName field to given value.

### HasStreetName

`func (o *StructuredAddress) HasStreetName() bool`

HasStreetName returns a boolean if a field has been set.

### GetLocality

`func (o *StructuredAddress) GetLocality() string`

GetLocality returns the Locality field if non-nil, zero value otherwise.

### GetLocalityOk

`func (o *StructuredAddress) GetLocalityOk() (*string, bool)`

GetLocalityOk returns a tuple with the Locality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocality

`func (o *StructuredAddress) SetLocality(v string)`

SetLocality sets Locality field to given value.

### HasLocality

`func (o *StructuredAddress) HasLocality() bool`

HasLocality returns a boolean if a field has been set.

### GetCity

`func (o *StructuredAddress) GetCity() string`

GetCity returns the City field if non-nil, zero value otherwise.

### GetCityOk

`func (o *StructuredAddress) GetCityOk() (*string, bool)`

GetCityOk returns a tuple with the City field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCity

`func (o *StructuredAddress) SetCity(v string)`

SetCity sets City field to given value.

### HasCity

`func (o *StructuredAddress) HasCity() bool`

HasCity returns a boolean if a field has been set.

### GetCounty

`func (o *StructuredAddress) GetCounty() string`

GetCounty returns the County field if non-nil, zero value otherwise.

### GetCountyOk

`func (o *StructuredAddress) GetCountyOk() (*string, bool)`

GetCountyOk returns a tuple with the County field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCounty

`func (o *StructuredAddress) SetCounty(v string)`

SetCounty sets County field to given value.

### HasCounty

`func (o *StructuredAddress) HasCounty() bool`

HasCounty returns a boolean if a field has been set.

### GetState

`func (o *StructuredAddress) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *StructuredAddress) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *StructuredAddress) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *StructuredAddress) HasState() bool`

HasState returns a boolean if a field has been set.

### GetCountry

`func (o *StructuredAddress) GetCountry() string`

GetCountry returns the Country field if non-nil, zero value otherwise.

### GetCountryOk

`func (o *StructuredAddress) GetCountryOk() (*string, bool)`

GetCountryOk returns a tuple with the Country field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountry

`func (o *StructuredAddress) SetCountry(v string)`

SetCountry sets Country field to given value.

### HasCountry

`func (o *StructuredAddress) HasCountry() bool`

HasCountry returns a boolean if a field has been set.

### GetPostalcode

`func (o *StructuredAddress) GetPostalcode() string`

GetPostalcode returns the Postalcode field if non-nil, zero value otherwise.

### GetPostalcodeOk

`func (o *StructuredAddress) GetPostalcodeOk() (*string, bool)`

GetPostalcodeOk returns a tuple with the Postalcode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPostalcode

`func (o *StructuredAddress) SetPostalcode(v string)`

SetPostalcode sets Postalcode field to given value.

### HasPostalcode

`func (o *StructuredAddress) HasPostalcode() bool`

HasPostalcode returns a boolean if a field has been set.

### GetCountryCode

`func (o *StructuredAddress) GetCountryCode() Country`

GetCountryCode returns the CountryCode field if non-nil, zero value otherwise.

### GetCountryCodeOk

`func (o *StructuredAddress) GetCountryCodeOk() (*Country, bool)`

GetCountryCodeOk returns a tuple with the CountryCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCountryCode

`func (o *StructuredAddress) SetCountryCode(v Country)`

SetCountryCode sets CountryCode field to given value.

### HasCountryCode

`func (o *StructuredAddress) HasCountryCode() bool`

HasCountryCode returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


