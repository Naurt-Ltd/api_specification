# FinalDestinationHit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **uuid::Uuid** |  | 
**address** | **String** |  | 
**geojson** | [**models::FinalDestinationHitGeojson**](FinalDestinationHitGeojson.md) |  | 
**distance** | Option<**f64**> |  | [optional]
**search_confidence** | Option<**f64**> | Confidence score in the range 0.0 to 1.0 indicating how well the result  matches the query. Higher is better. This is closely linked to match_level.  See: https://docs.naurt.com/reference/search-confidence  Not to be confused with Accuracy, which is how good the data itself is. This  is about the likelihood of a good match.  | [optional]
**match_level** | Option<[**models::FinalDestinationMatchLevel**](FinalDestinationMatchLevel.md)> |  | [optional]
**structured_response** | Option<[**models::StructuredAddress**](StructuredAddress.md)> |  | [optional]
**source_id** | Option<[**models::FinalDestinationSourceIdResponse**](FinalDestinationSourceIdResponse.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


