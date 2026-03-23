# OptionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrentVersion** | **string** |  | 
**DeprecatedVersions** | **[]string** |  | 

## Methods

### NewOptionsResponse

`func NewOptionsResponse(currentVersion string, deprecatedVersions []string, ) *OptionsResponse`

NewOptionsResponse instantiates a new OptionsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOptionsResponseWithDefaults

`func NewOptionsResponseWithDefaults() *OptionsResponse`

NewOptionsResponseWithDefaults instantiates a new OptionsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCurrentVersion

`func (o *OptionsResponse) GetCurrentVersion() string`

GetCurrentVersion returns the CurrentVersion field if non-nil, zero value otherwise.

### GetCurrentVersionOk

`func (o *OptionsResponse) GetCurrentVersionOk() (*string, bool)`

GetCurrentVersionOk returns a tuple with the CurrentVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrentVersion

`func (o *OptionsResponse) SetCurrentVersion(v string)`

SetCurrentVersion sets CurrentVersion field to given value.


### GetDeprecatedVersions

`func (o *OptionsResponse) GetDeprecatedVersions() []string`

GetDeprecatedVersions returns the DeprecatedVersions field if non-nil, zero value otherwise.

### GetDeprecatedVersionsOk

`func (o *OptionsResponse) GetDeprecatedVersionsOk() (*[]string, bool)`

GetDeprecatedVersionsOk returns a tuple with the DeprecatedVersions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeprecatedVersions

`func (o *OptionsResponse) SetDeprecatedVersions(v []string)`

SetDeprecatedVersions sets DeprecatedVersions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


