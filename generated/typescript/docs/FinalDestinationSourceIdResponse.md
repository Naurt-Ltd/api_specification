
# FinalDestinationSourceIdResponse

An object containing information on source IDs. Source IDs refer to underlying IDs from address data sets. Currently supporting UPRN and UDPRN in the UK  referring to the OrdnanceSurvey datasets 

## Properties

Name | Type
------------ | -------------
`osUprn` | string
`osUdprn` | string

## Example

```typescript
import type { FinalDestinationSourceIdResponse } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "osUprn": null,
  "osUdprn": null,
} satisfies FinalDestinationSourceIdResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationSourceIdResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


