# FinalDestinationOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PrettyPrint** | Pointer to **bool** | This will format the response in a more human readable way. Only recommended for debug, as it increases payload size  | [optional] [default to false]
**Verbose** | Pointer to **bool** | Returns additional debug information about request processing. Only  recommended for debug, as it increases payload size  | [optional] [default to false]
**StructuredResponse** | Pointer to **bool** | Adds the Naurt structured format of the address to the response  | [optional] [default to false]
**GeojsonType** | Pointer to [**GeojsonType**](GeojsonType.md) |  | [optional] [default to GEOJSONTYPE_GEOJSON]
**ReturnOriginal** | Pointer to **bool** | Returns your original query back in the response  | [optional] [default to false]
**InputFilter** | Pointer to [**InputFilter**](InputFilter.md) |  | [optional] [default to INPUTFILTER_LOOSE]

## Methods

### NewFinalDestinationOptions

`func NewFinalDestinationOptions() *FinalDestinationOptions`

NewFinalDestinationOptions instantiates a new FinalDestinationOptions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationOptionsWithDefaults

`func NewFinalDestinationOptionsWithDefaults() *FinalDestinationOptions`

NewFinalDestinationOptionsWithDefaults instantiates a new FinalDestinationOptions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrettyPrint

`func (o *FinalDestinationOptions) GetPrettyPrint() bool`

GetPrettyPrint returns the PrettyPrint field if non-nil, zero value otherwise.

### GetPrettyPrintOk

`func (o *FinalDestinationOptions) GetPrettyPrintOk() (*bool, bool)`

GetPrettyPrintOk returns a tuple with the PrettyPrint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrettyPrint

`func (o *FinalDestinationOptions) SetPrettyPrint(v bool)`

SetPrettyPrint sets PrettyPrint field to given value.

### HasPrettyPrint

`func (o *FinalDestinationOptions) HasPrettyPrint() bool`

HasPrettyPrint returns a boolean if a field has been set.

### GetVerbose

`func (o *FinalDestinationOptions) GetVerbose() bool`

GetVerbose returns the Verbose field if non-nil, zero value otherwise.

### GetVerboseOk

`func (o *FinalDestinationOptions) GetVerboseOk() (*bool, bool)`

GetVerboseOk returns a tuple with the Verbose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerbose

`func (o *FinalDestinationOptions) SetVerbose(v bool)`

SetVerbose sets Verbose field to given value.

### HasVerbose

`func (o *FinalDestinationOptions) HasVerbose() bool`

HasVerbose returns a boolean if a field has been set.

### GetStructuredResponse

`func (o *FinalDestinationOptions) GetStructuredResponse() bool`

GetStructuredResponse returns the StructuredResponse field if non-nil, zero value otherwise.

### GetStructuredResponseOk

`func (o *FinalDestinationOptions) GetStructuredResponseOk() (*bool, bool)`

GetStructuredResponseOk returns a tuple with the StructuredResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStructuredResponse

`func (o *FinalDestinationOptions) SetStructuredResponse(v bool)`

SetStructuredResponse sets StructuredResponse field to given value.

### HasStructuredResponse

`func (o *FinalDestinationOptions) HasStructuredResponse() bool`

HasStructuredResponse returns a boolean if a field has been set.

### GetGeojsonType

`func (o *FinalDestinationOptions) GetGeojsonType() GeojsonType`

GetGeojsonType returns the GeojsonType field if non-nil, zero value otherwise.

### GetGeojsonTypeOk

`func (o *FinalDestinationOptions) GetGeojsonTypeOk() (*GeojsonType, bool)`

GetGeojsonTypeOk returns a tuple with the GeojsonType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGeojsonType

`func (o *FinalDestinationOptions) SetGeojsonType(v GeojsonType)`

SetGeojsonType sets GeojsonType field to given value.

### HasGeojsonType

`func (o *FinalDestinationOptions) HasGeojsonType() bool`

HasGeojsonType returns a boolean if a field has been set.

### GetReturnOriginal

`func (o *FinalDestinationOptions) GetReturnOriginal() bool`

GetReturnOriginal returns the ReturnOriginal field if non-nil, zero value otherwise.

### GetReturnOriginalOk

`func (o *FinalDestinationOptions) GetReturnOriginalOk() (*bool, bool)`

GetReturnOriginalOk returns a tuple with the ReturnOriginal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReturnOriginal

`func (o *FinalDestinationOptions) SetReturnOriginal(v bool)`

SetReturnOriginal sets ReturnOriginal field to given value.

### HasReturnOriginal

`func (o *FinalDestinationOptions) HasReturnOriginal() bool`

HasReturnOriginal returns a boolean if a field has been set.

### GetInputFilter

`func (o *FinalDestinationOptions) GetInputFilter() InputFilter`

GetInputFilter returns the InputFilter field if non-nil, zero value otherwise.

### GetInputFilterOk

`func (o *FinalDestinationOptions) GetInputFilterOk() (*InputFilter, bool)`

GetInputFilterOk returns a tuple with the InputFilter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputFilter

`func (o *FinalDestinationOptions) SetInputFilter(v InputFilter)`

SetInputFilter sets InputFilter field to given value.

### HasInputFilter

`func (o *FinalDestinationOptions) HasInputFilter() bool`

HasInputFilter returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


