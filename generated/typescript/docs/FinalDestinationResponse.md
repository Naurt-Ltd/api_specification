
# FinalDestinationResponse

A response from the API. The `responses` are in the same order as the original  `queries` from the request. 

## Properties

Name | Type
------------ | -------------
`responses` | [Array&lt;FinalDestinationHits&gt;](FinalDestinationHits.md)
`logging` | [FinalDestinationLogging](FinalDestinationLogging.md)
`version` | string
`requestId` | string

## Example

```typescript
import type { FinalDestinationResponse } from '@naurt/api'

// TODO: Update the object below with actual values
const example = {
  "responses": null,
  "logging": null,
  "version": null,
  "requestId": null,
} satisfies FinalDestinationResponse

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FinalDestinationResponse
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


