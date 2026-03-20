# FeedbackRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Queries** | [**[]FeedbackQuery**](FeedbackQuery.md) |  | 

## Methods

### NewFeedbackRequest

`func NewFeedbackRequest(queries []FeedbackQuery, ) *FeedbackRequest`

NewFeedbackRequest instantiates a new FeedbackRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackRequestWithDefaults

`func NewFeedbackRequestWithDefaults() *FeedbackRequest`

NewFeedbackRequestWithDefaults instantiates a new FeedbackRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueries

`func (o *FeedbackRequest) GetQueries() []FeedbackQuery`

GetQueries returns the Queries field if non-nil, zero value otherwise.

### GetQueriesOk

`func (o *FeedbackRequest) GetQueriesOk() (*[]FeedbackQuery, bool)`

GetQueriesOk returns a tuple with the Queries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueries

`func (o *FeedbackRequest) SetQueries(v []FeedbackQuery)`

SetQueries sets Queries field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


