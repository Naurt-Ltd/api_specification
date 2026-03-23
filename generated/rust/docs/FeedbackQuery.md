# FeedbackQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | Option<**uuid::Uuid**> | Existing Naurt ID for the address being updated | [optional]
**address_string** | Option<**String**> | Address text for a new feedback item. Address strings are not matched with current data, so existing addresses should use `id` instead.  | [optional]
**parking_location** | Option<[**models::FeedbackLocation**](FeedbackLocation.md)> |  | [optional]
**door_location** | Option<[**models::FeedbackLocation**](FeedbackLocation.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


