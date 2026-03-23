
# FinalDestinationHit


## Properties

Name | Type
------------ | -------------
`id` | string
`address` | string
`geojson` | [FinalDestinationHitGeojson](FinalDestinationHitGeojson.md)
`distance` | number
`searchConfidence` | number
`structuredResponse` | [StructuredAddress](StructuredAddress.md)
`sourceId` | [FinalDestinationSourceIdResponse](FinalDestinationSourceIdResponse.md)

## Example

```typescript
import type { FinalDestinationHit } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "address": null,
  "geojson": null,
  "distance": null,
  "searchConfidence": 0.93,
  "structuredResponse": null,
  "sourceId": null,
} satisfies FinalDestinationHit

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationHit
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


