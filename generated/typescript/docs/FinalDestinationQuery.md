
# FinalDestinationQuery

A single search query. It can be used to lookup a door and parking spot by: - Forward geocode - Reverse geocode - Structured geocode - Naurt ID lookup - Source ID lookup 

## Properties

Name | Type
------------ | -------------
`addressString` | string
`addressStructured` | [StructuredAddress](StructuredAddress.md)
`location` | [FinalDestinationLocation](FinalDestinationLocation.md)
`id` | string
`country` | [Country](Country.md)
`sourceId` | [FinalDestinationSourceIdRequest](FinalDestinationSourceIdRequest.md)
`additionalMatches` | boolean
`language` | [Language](Language.md)

## Example

```typescript
import type { FinalDestinationQuery } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "addressString": null,
  "addressStructured": null,
  "location": null,
  "id": null,
  "country": null,
  "sourceId": null,
  "additionalMatches": null,
  "language": null,
} satisfies FinalDestinationQuery

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationQuery
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


