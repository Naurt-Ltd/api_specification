# FinalDestinationHits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BestMatch** | [**NullableFinalDestinationHit**](FinalDestinationHit.md) |  | 
**AdditionalMatches** | [**[]FinalDestinationHit**](FinalDestinationHit.md) |  | 
**Status** | [**FinalDestinationStatus**](FinalDestinationStatus.md) |  | 
**OriginalRequest** | Pointer to [**FinalDestinationQuery**](FinalDestinationQuery.md) |  | [optional] 

## Methods

### NewFinalDestinationHits

`func NewFinalDestinationHits(bestMatch NullableFinalDestinationHit, additionalMatches []FinalDestinationHit, status FinalDestinationStatus, ) *FinalDestinationHits`

NewFinalDestinationHits instantiates a new FinalDestinationHits object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFinalDestinationHitsWithDefaults

`func NewFinalDestinationHitsWithDefaults() *FinalDestinationHits`

NewFinalDestinationHitsWithDefaults instantiates a new FinalDestinationHits object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBestMatch

`func (o *FinalDestinationHits) GetBestMatch() FinalDestinationHit`

GetBestMatch returns the BestMatch field if non-nil, zero value otherwise.

### GetBestMatchOk

`func (o *FinalDestinationHits) GetBestMatchOk() (*FinalDestinationHit, bool)`

GetBestMatchOk returns a tuple with the BestMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBestMatch

`func (o *FinalDestinationHits) SetBestMatch(v FinalDestinationHit)`

SetBestMatch sets BestMatch field to given value.


### SetBestMatchNil

`func (o *FinalDestinationHits) SetBestMatchNil(b bool)`

 SetBestMatchNil sets the value for BestMatch to be an explicit nil

### UnsetBestMatch
`func (o *FinalDestinationHits) UnsetBestMatch()`

UnsetBestMatch ensures that no value is present for BestMatch, not even an explicit nil
### GetAdditionalMatches

`func (o *FinalDestinationHits) GetAdditionalMatches() []FinalDestinationHit`

GetAdditionalMatches returns the AdditionalMatches field if non-nil, zero value otherwise.

### GetAdditionalMatchesOk

`func (o *FinalDestinationHits) GetAdditionalMatchesOk() (*[]FinalDestinationHit, bool)`

GetAdditionalMatchesOk returns a tuple with the AdditionalMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAdditionalMatches

`func (o *FinalDestinationHits) SetAdditionalMatches(v []FinalDestinationHit)`

SetAdditionalMatches sets AdditionalMatches field to given value.


### GetStatus

`func (o *FinalDestinationHits) GetStatus() FinalDestinationStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *FinalDestinationHits) GetStatusOk() (*FinalDestinationStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *FinalDestinationHits) SetStatus(v FinalDestinationStatus)`

SetStatus sets Status field to given value.


### GetOriginalRequest

`func (o *FinalDestinationHits) GetOriginalRequest() FinalDestinationQuery`

GetOriginalRequest returns the OriginalRequest field if non-nil, zero value otherwise.

### GetOriginalRequestOk

`func (o *FinalDestinationHits) GetOriginalRequestOk() (*FinalDestinationQuery, bool)`

GetOriginalRequestOk returns a tuple with the OriginalRequest field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOriginalRequest

`func (o *FinalDestinationHits) SetOriginalRequest(v FinalDestinationQuery)`

SetOriginalRequest sets OriginalRequest field to given value.

### HasOriginalRequest

`func (o *FinalDestinationHits) HasOriginalRequest() bool`

HasOriginalRequest returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


